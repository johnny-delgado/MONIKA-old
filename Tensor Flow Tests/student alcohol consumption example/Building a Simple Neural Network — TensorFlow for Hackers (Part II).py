# -*- coding: utf-8 -*-

# created 26 June 2018 0113
#https://medium.com/@curiousily/tensorflow-for-hackers-part-ii-building-simple-neural-network-2d6779d2f91b

#used to fix a decoding error
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from math import floor, ceil
from pylab import rcParams


#Some styling and making our experiments reproducible:
sns.set(style='ticks', palette='Spectral', font_scale=1.5)

material_palette = ["#4CAF50", "#2196F3", "#9E9E9E", "#FF9800", "#607D8B", "#9C27B0"]
sns.set_palette(material_palette)
rcParams['figure.figsize'] = 16, 8

plt.xkcd();
random_state = 42
np.random.seed(random_state)
tf.set_random_seed(random_state)



#load data, assign proper course attendance to each student and merge the two files into one:

math_df = pd.read_csv("student/student-mat.csv", sep=";")
port_df = pd.read_csv("student/student-por.csv", sep=";")

math_df["course"] = "math"
port_df["course"] = "portuguese"

merged_df = math_df.append(port_df)
print merged_df.shape #(1044, 34) meaning 1044 rows



#remove duplicates and do some other stuff
merge_vector = ["school","sex","age","address",
                "famsize","Pstatus","Medu","Fedu",
                "Mjob","Fjob","reason","nursery","internet"]

duplicated_mask = merged_df.duplicated(keep=False, subset=merge_vector)
duplicated_df = merged_df[duplicated_mask]
unique_df = merged_df[~duplicated_mask]
both_courses_mask = duplicated_df.duplicated(subset=merge_vector)
both_courses_df = duplicated_df[~both_courses_mask].copy()
both_courses_df["course"] = "both"
students_df = unique_df.append(both_courses_df)


#quantifying data
students_df = students_df.sample(frac=1) #shuffle data
students_df['alcohol'] = (students_df.Walc * 2 + students_df.Dalc * 5) / 7
students_df['alcohol'] = students_df.alcohol.map(lambda x: ceil(x))
students_df['drinker'] = students_df.alcohol.map(lambda x: "yes" if x > 2 else "no")


#visualize the data (only the last one made gets displayed)
#students_df.course.value_counts().plot(kind="bar", rot=0); #course distribution
#students_df.alcohol.value_counts().plot(kind="bar", rot=0); #alcohol consumption formula
#students_df.drinker.value_counts().plot(kind="bar", rot=0); #The actual variable that we are going to predict
#sns.pairplot(students_df[['age', 'absences', 'G3', 'goout', 'freetime', 'studytime', 'drinker']], hue='drinker'); #Somewhat more comprehensive overview

#a general correlations matrix:
corr_mat = students_df.corr() 
fig, ax = plt.subplots(figsize=(20, 12)) 
sns.heatmap(corr_mat, vmax=1.0, square=True, ax=ax);



#Most of our variables are categorical and we must one-hot encode them four our NN to work properly. First, let’s define a little helper function:
# *
# *** Convert categorical variable into dummy/indicator variables (use this for day of the week and my sleep state)
# *
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html
def encode(series): 
  return pd.get_dummies(series.astype(str))

#Our features and target variable using our little helper function:
train_x = pd.get_dummies(students_df.school)
train_x['age'] = students_df.age
train_x['absences'] = students_df.absences
train_x['g1'] = students_df.G1
train_x['g2'] = students_df.G2
train_x['g3'] = students_df.G3
train_x = pd.concat([train_x, encode(students_df.sex), encode(students_df.Pstatus),
	encode(students_df.Medu), encode(students_df.Fedu),
	encode(students_df.guardian), encode(students_df.studytime),
	encode(students_df.failures), encode(students_df.activities),
	encode(students_df.higher), encode(students_df.romantic),
	encode(students_df.reason), encode(students_df.paid),
	encode(students_df.goout), encode(students_df.health),
	encode(students_df.famsize), encode(students_df.course)
	], axis=1)

train_y = encode(students_df.drinker)

print train_y


#splitting the data
# Let’s allocate 90% of the data for training and use 10% for testing:
#*** for my needs I may have to randomize the order of datapoints first so it's not using the oldest 90% of data for training and the newest 10% for testing
train_size = 0.9

train_cnt = int(train_x.shape[0] * train_size)
x_train = train_x.iloc[0:train_cnt].values
y_train = train_y.iloc[0:train_cnt].values
x_test = train_x.iloc[train_cnt:].values
y_test = train_y.iloc[train_cnt:].values



#Our NN consists of input, output and 1 hidden layer.
#We are using ReLU as activation function of the hidden layer and softmax for our output layer.
#As an additional bonus we will use Dropout — simple way to reduce overfitting during the training of our network.
#Let’s wrap our model in a little helper function:
def multilayer_perceptron(x, weights, biases, keep_prob):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    layer_1 = tf.nn.dropout(layer_1, keep_prob)
    out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
    return out_layer


#set the number of neurons in the hidden layer to 38
#and randomly initialize the weights and biases considering their proper dimensions:
n_hidden_1 = 38
n_input = train_x.shape[1]
n_classes = train_y.shape[1]

weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'out': tf.Variable(tf.random_normal([n_hidden_1, n_classes]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

keep_prob = tf.placeholder("float")



#We will train our model for 5,000 epochs (training steps) with a batch size of 32.
#That is, at each step, we will train our NN using 32 rows of our data.
#Granted, in our case you can just train on the whole dataset.
#However, when the data is huge and you can’t fit it in memory,
#you would love to split it and feed it to the model at batches (chunks):
training_epochs = 5000
display_step = 1000
batch_size = 32

x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])




#Our model is created by just calling our helper function with the proper arguments:
predictions = multilayer_perceptron(x, weights, biases, keep_prob)



#In order for our model to learn, we will define what is bad and try to minimize it
#We will call the “badness” — error or cost (hence, the cost function).
#It represents how far off of the true result our model is at some point during training.
#We would love that error to be 0 for all possible inputs.
#we're using cross entropy - https://colah.github.io/posts/2015-09-Visual-Information/
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions, labels=y))


#Adam is a type of gradient descent optimization algorithm which essentially tries as hard as he can to find proper weights and biases for our network via minimizing the cost function that we specified above.
#http://ruder.io/optimizing-gradient-descent/
#Using Adam in TensorFlow is quite easy, we just have to specify learning rate (you can fiddle with that one) and pass the cost function we defined above:
optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cost) #learning_rate is our alpha value









#Evaluation
#Time to see how well our model can predict.
#During the training, we will set the keep probability of the Dropout to 0.8 and reset it to 1.0 during test time:
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_epochs):
        avg_cost = 0.0
        total_batch = int(len(x_train) / batch_size)
        x_batches = np.array_split(x_train, total_batch)
        y_batches = np.array_split(y_train, total_batch)
        for i in range(total_batch):
            batch_x, batch_y = x_batches[i], y_batches[i]
            _, c = sess.run([optimizer, cost], 
                            feed_dict={
                                x: batch_x, 
                                y: batch_y, 
                                keep_prob: 0.8
                            })
            avg_cost += c / total_batch
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", \
                "{:.9f}".format(avg_cost))
    print("Optimization Finished!")
    correct_prediction = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy:", accuracy.eval({x: x_test, y: y_test, keep_prob: 1.0}))







plt.show();

print "fin"























