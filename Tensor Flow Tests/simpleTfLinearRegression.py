# -*- coding: utf-8 -*-


# to run, activate tensor flow first with:
# source ~/tensorflow/bin/activate
# to deactivate it, run:
# deactivate
#
# created 26 June 2018 0049
#https://medium.com/@curiousily/tensorflow-for-hackers-part-i-basics-2c46bc99c930

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


#print tf.__version__



# plot a linear regression
X = np.random.rand(100).astype(np.float32)
a = 50
b = 40
Y = a * X + b





#add noise to the dependent variable
Y = np.vectorize(lambda y: y + np.random.normal(loc=0.0, scale=0.05))(Y)
a_var = tf.Variable(1.0)
b_var = tf.Variable(1.0)
y_var = a_var * X + b_var

#Our task will be to minimize the mean squared error or in TensorFlow parlance — reduce the mean.
loss = tf.reduce_mean(tf.square(y_var - Y))

#So, let’s try to minimize it using gradient descent.
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#Let’s use our optimizer for 300 steps of learning
TRAINING_STEPS = 300
results = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(TRAINING_STEPS):
        results.append(sess.run([train, a_var, b_var])[1:])


#Let’s get the final and best predictions for a and b
final_pred = results[-1]
a_hat = final_pred[0]
b_hat = final_pred[1]
y_hat = a_hat * X + b_hat

print("a:", a_hat, "b:", b_hat)


plt.plot(X, Y);
plt.plot(X, y_hat);
plt.show();











