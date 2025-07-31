# TF made EZ
import tensorflow.contrib.learn as learn
from tensorflow.contrib.learn.python.learn.estimators import estimator

# Some basics
import numpy as np
import math

# Learn more sklearn
# scikit-learn.org
import sklearn
from sklearn import metrics

# Seed the data
np.random.seed(42)

# Load data
data = np.load('data_with_labels.npz')
train = data['arr_0']/255.
labels = data['arr_1']

# Look at some data
print(train[0])
print(labels[0])

# If you have matplotlib installed
import matplotlib.pyplot as plt
plt.ion()

# Split data into training and validation
indices = np.random.permutation(train.shape[0])
valid_cnt = int(train.shape[0] * 0.1)
test_idx, training_idx = indices[:valid_cnt],\
                         indices[valid_cnt:]
test, train = train[test_idx,:],\
              train[training_idx,:]
test_labels, train_labels = labels[test_idx],\
                        labels[training_idx]

train = np.array(train,dtype=np.float32)
test = np.array(test,dtype=np.float32)
train_labels = np.array(train_labels,dtype=np.int32)
test_labels = np.array(test_labels,dtype=np.int32)

#sess = tf.InteractiveSession()

# `learn` needs to interpret the data correctly

feature_columns = learn.infer_real_valued_columns_from_input(train.reshape([-1,36*36]))

# Logistic Regression
classifier = estimator.SKCompat(learn.LinearClassifier(
            feature_columns = feature_columns,
            n_classes=5))

# One line training
# steps is number of total batches
# steps*batch_size/len(train) = num_epochs
classifier.fit(train.reshape([-1,36*36]),
               train_labels,
               steps=1024,
               batch_size=32)

# sklearn compatible accuracy
test_probs = classifier.predict(test.reshape([-1,36*36]))
sklearn.metrics.accuracy_score(test_labels,
        test_probs['classes'])

# Dense neural net
classifier = estimator.SKCompat(learn.DNNClassifier(
            feature_columns = feature_columns,
            hidden_units=[10,5],
            n_classes=5,
            optimizer='Adam'))

# Same training call
classifier.fit(train.reshape([-1,36*36]),
               train_labels,
               steps=1024,
               batch_size=32)

# simple accuracy
test_probs = classifier.predict(test.reshape([-1,36*36]))
sklearn.metrics.accuracy_score(test_labels,
        test_probs['classes'])

# confusion is easy
train_probs = classifier.predict(train.reshape([-1,36*36]))
conf = metrics.confusion_matrix(train_labels,
        train_probs['classes'])
print(conf)

### Convolutional net
# Access general TF functions
import tensorflow as tf
import tensorflow.contrib.layers as layers


def conv_learn(X, y, mode):
    # Ensure our images are 2d 
    X = tf.reshape(X, [-1, 36, 36, 1])
    # We'll need these in one-hot format
    y = tf.one_hot(tf.cast(y, tf.int32), 5, 1, 0)
    # conv layer will compute 4 kernels for each 5x5 patch
    with tf.variable_scope('conv_layer'):
        # 5x5 convolution, pad with zeros on edges
        h1 = layers.convolution2d(X, num_outputs=4,
                kernel_size=[5, 5], 
                activation_fn=tf.nn.relu)
        # 2x2 Max pooling, no padding on edges
        p1 = tf.nn.max_pool(h1, ksize=[1, 2, 2, 1],
                strides=[1, 2, 2, 1], padding='VALID')
    # Need to flatten conv output for use in dense layer
    p1_size = np.product(
              [s.value for s in p1.get_shape()[1:]])
    p1f = tf.reshape(p1, [-1, p1_size ])
    # densely connected layer with 32 neurons and dropout
    h_fc1 = layers.fully_connected(p1f,
            5,
            activation_fn=tf.nn.relu)
    drop = layers.dropout(h_fc1, keep_prob=0.5,
    is_training=mode == tf.contrib.learn.ModeKeys.TRAIN)
    # Have to handle the final linear layer and loss manually :(
    logits = layers.fully_connected(drop, 5, activation_fn=None)
    loss = tf.losses.softmax_cross_entropy(y, logits)
    # Setup the training function manually
    train_op = layers.optimize_loss(
        loss,
        tf.contrib.framework.get_global_step(),
        optimizer='Adam',
        learning_rate=0.01)
    return tf.argmax(logits, 1), loss, train_op


# Use generic estimator with our function
classifier = estimator.SKCompat(
	     learn.Estimator(
		 model_fn=conv_learn))

classifier.fit(train,train_labels,
                steps=1024,
                batch_size=32)

# simple accuracy
metrics.accuracy_score(test_labels,classifier.predict(test))

# See layer names
print(classifier._estimator.get_variable_names())

# Convolutional Layer Weights
print(classifier._estimator.get_variable_value(
        'conv_layer/Conv/weights'))
print(classifier._estimator.get_variable_value(
        'conv_layer/Conv/biases'))

# Dense Layer
print(classifier._estimator.get_variable_value(
        'fully_connected/weights'))

# Logistic weights
print(classifier._estimator.get_variable_value(
        'fully_connected_1/weights'))



