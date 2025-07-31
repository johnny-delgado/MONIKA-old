# -*- coding: utf-8 -*-

# created 26 June 2018 0113
#good ref at https://medium.com/@curiousily/tensorflow-for-hackers-part-ii-building-simple-neural-network-2d6779d2f91b

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



#load data
sleep_data = pd.read_csv("SleepTrainingData.csv", sep=";")
#print sleep_data.shape #(number of datapoints, number of values in each datapoint)

sleep_data = sleep_data.sample(frac=1) #shuffle data - The frac keyword argument specifies the fraction of rows to return in the random sample, so frac=1 means return all rows (in random order).



#visualize the data (only the last one made gets displayed)
#students_df.course.value_counts().plot(kind="bar", rot=0); #course distribution
#students_df.alcohol.value_counts().plot(kind="bar", rot=0); #alcohol consumption formula
#students_df.drinker.value_counts().plot(kind="bar", rot=0); #The actual variable that we are going to predict
#sns.pairplot(sleep_data[["control", "sin_time", "cos_time", "Sun","Mon","Tues","Wed","Thur","Fri","Sat" , "sin_doty", "cos_doty", "normalizedYear", "awake","napping","sleeping"]], hue='sleeping'); #Somewhat more comprehensive overview using the hue as our color reference
#sns.pairplot(sleep_data[["sin_time","Sun","Mon","Tues","Wed","Thur","Fri","Sat", "sleeping"]], hue='sleeping'); #Somewhat more comprehensive overview using the hue as our color reference
#plt.show();

'''
#a general correlations matrix:
corr_mat = sleep_data.corr() 
fig, ax = plt.subplots(figsize=(20, 12)) 
sns.heatmap(corr_mat, vmax=1.0, square=True, ax=ax);
plt.show();
'''



#*** encode the variables here in the future but for now I encode them at dataset creation




#split the sleep_data array into an input and output array for later usage by the trainer
#this must be after the shuffeling of data so the results don't get messed up
input_data = sleep_data[["control", "sin_time", "cos_time", "Sun","Mon","Tues","Wed","Thur","Fri","Sat" , "sin_doty", "cos_doty", "normalizedYear"]]
output_data = sleep_data[["awake", "napping","sleeping"]]


 


#splitting the data
# Let’s allocate 90% of the data for training and use 10% for testing:
#*** for my needs I may have to randomize the order of datapoints first so it's not using the oldest 90% of data for training and the newest 10% for testing
train_size = 0.9

train_cnt = int(input_data.shape[0] * train_size)
training_input_data = input_data.iloc[0:train_cnt].values
training_output_data = output_data.iloc[0:train_cnt].values
testing_input_data = input_data.iloc[train_cnt:].values
testing_output_data = output_data.iloc[train_cnt:].values
#print training_input_data.shape
#print training_output_data.shape
#print testing_input_data.shape
#print testing_output_data.shape



#Our NN consists of input, output and 1 hidden layer.
#We are using ReLU as activation function of the hidden layer and softmax for our output layer.
#As an additional bonus we will use Dropout — simple way to reduce overfitting during the training of our network.
#Let’s wrap our model in a little helper function:
def multilayer_perceptron(x, weights, biases, keep_prob):
	layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
	layer_1 = tf.nn.relu(layer_1)
	layer_1 = tf.nn.dropout(layer_1, keep_prob)
	out_layer = tf.matmul(layer_1, weights['out']) + biases['out'] #matmul = matrix multiplication
	return out_layer




#setting up the neurons
n_hidden_1 = 50 #number of neurons in the hidden layer
n_input = input_data.shape[1]
n_output = output_data.shape[1]


#randomly initialize the weights and biases considering their proper dimensions:
#I think 'h1' is the weight & bias of the synapse from the input to hidden layer 1,
# and 'out' is the weight & bias of the synapse from hidden layer 1 to the output
#tf.random_normal([n_input, n_hidden_1]) 
weights = {
	'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
	'out': tf.Variable(tf.random_normal([n_hidden_1, n_output]))
} 

biases = {
	'b1': tf.Variable(tf.random_normal([n_hidden_1])),
	'out': tf.Variable(tf.random_normal([n_output]))
}

keep_prob = tf.placeholder("float")





#We will train our model for 5,000 epochs (training steps) with a batch size of 32.
#That is, at each step, we will train our NN using batch_size number of rows of our data.
#Batching is good for large data sets
training_epochs = 3000

#siaply the cost after every display_step epochs
display_step = 10 #this can be bigger or smaller than batch_size, it doesn't matter

#a batch is number of samples that going to be propagated through the network
#batch_size 
numberOfBatches = 64 # I think this is the number of batches you split the input data into (smaller is more accurate but bigger is faster)








x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_output])





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
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost) #learning_rate is our alpha value



errorArray = np.empty([])




#Evaluation
#Time to see how well our model can predict.
#During the training, we will set the keep probability of the Dropout to 0.8 and reset it to 1.0 during test time:
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())

	johnnysTemporaryVariable = 0
	
	for epoch in range(training_epochs):

		#print "epoch number: " + str(epoch)

		avg_cost = 0.0
		pointsPerBatch = int(len(training_input_data) / numberOfBatches) # pointsPerBatch = how many datapoints are in each batch
		
		#print "pointsPerBatch is: " + str(pointsPerBatch)

		#split the huge training arrays into several (pointsPerBatch) equally sized arrays to make them more managable for the processor
		#each datapoint is an array itself representing one time point
		allInputBatches = np.array_split(training_input_data, pointsPerBatch)
		allOutputBatches = np.array_split(training_output_data, pointsPerBatch)


		for i in range(pointsPerBatch): #i is the current datapoint in this batch that we're processing

			currentPointInput, currentPointOutput = allInputBatches[i], allOutputBatches[i]

			#run(fetches,feed_dict=None)
			#Runs operations and evaluates tensors in fetches.
			#This method runs one "step" of TensorFlow computation,
			# by running the necessary graph fragment to execute every Operation and
			# evaluate every Tensor in fetches,
			#substituting the values in feed_dict for the corresponding input values.
			#the _, is used so x just equals the cost of the current point (sess.run normally returns ['none', the cost] and we want to ignore the 'none')
			_, c = sess.run([optimizer, cost], 
							feed_dict={
								x: currentPointInput, 
								y: currentPointOutput, 
								keep_prob: 0.8
							}) #keep_prob is used to control the dropout rate used when training the neural network. Essentially, it means that each connection between layers (in this case between the last densely connected layer and the readout layer) will only be used with probability 0.8 when training. This reduces overfitting.




			avg_cost += c / pointsPerBatch

			errorArray = np.vstack([errorArray, avg_cost]) #zigzaging graph showing error increasing every batch but overall reducing


			johnnysTemporaryVariable = johnnysTemporaryVariable + 1

		#errorArray = np.vstack([errorArray, avg_cost]) #a smooth graph

		#the %04d is used to ensure we display 4 didgits for the count of the current epoch
		if epoch % display_step == 0:
			print("Epoch:", '%04d' % (epoch+1), "cost=", \
				"{:.9f}".format(avg_cost))


#so far untested
		#save the synapses every 1000 epochs and display the accuracy
		if epoch % 1000 == 0:


			#put a conditional here to only save if the accuracy is better than a certain number (the previous accuracy)


			print("Epoch:", '%04d' % (epoch+1), "cost=", \
				"{:.9f}".format(avg_cost))
			#save the trained session for later predicting use
			saver = tf.train.Saver()
			saver.save(sess, '/Users/Johnny/Monika/Tensor Flow Tests/TrainedSleepPredictionSess')  #filename ends with .ckpt
			print "my temp variable is " + str(johnnysTemporaryVariable)
			print("saved synapses (weights and biases) now")
			correct_prediction = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
			accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
			print("Accuracy:", accuracy.eval({x: testing_input_data, y: testing_output_data, keep_prob: 1.0}))
			print "now continuing to train"



	print "my temp variable is " + str(johnnysTemporaryVariable)
	print("Optimization Finished!")
	correct_prediction = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
	print("Accuracy:", accuracy.eval({x: testing_input_data, y: testing_output_data, keep_prob: 1.0}))


	print "You were sleeping and I thought you were..."
	#["control", "sin_time", "cos_time", "Sun","Mon","Tues","Wed","Thur","Fri","Sat" , "sin_doty", "cos_doty", "normalizedYear"]]
	inputPoint = [[1.000000000000000000e+00,9.858206292667875958e-01,1.678025235568137152e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,6.979441547663435275e-01,-7.161521883143933120e-01,1.000000000000000000e+00]]
	#guess = tf.nn.softmax(tf.matmul(inputPoint,weights) + biases)


#def multilayer_perceptron(x, weights, biases, keep_prob):
	'''tempHiddenLayer = tf.add(  tf.matmul(inputPoint, weights['h1']), biases['b1']  )
	tempHiddenLayer = tf.nn.relu(tempHiddenLayer)
	tempHiddenLayer = tf.nn.dropout(tempHiddenLayer, 1.)
	guess = tf.matmul(tempHiddenLayer, weights['out']) + biases['out']
	'''

	guess = multilayer_perceptron(inputPoint, weights, biases, 1.)

	#print guess.shape # (1, 3)
	#print guess # Tensor("add_1:0", shape=(1, 3), dtype=float32)   # same as print (guess)
	print (sess.run(guess)) # [[6.0709867  -50.731033  8.735189]]

	#print tf.Print(guess, [guess])

	#plt.plot(guess)

	print "weights is a:"
	print(type(weights))
	print "biases is a:"
	print(type(biases))



#try to turn this into a function
	#save the trained session for later predicting use
	saver = tf.train.Saver()
	saver.save(sess, '/Users/Johnny/Monika/Tensor Flow Tests/TrainedSleepPredictionSess')  #filename ends with .ckpt



	'''
	np.savetxt('weights_h1', weights['h1']);
	np.savetxt('weights_out', weights['out']);
	np.savetxt('biases_b1', biases['b1']);
	np.savetxt('biases_out', biases['out']);
	'''





#students_df.course.value_counts().plot(kind="bar", rot=0); #course distribution
#plot_error(errorArray)


#print errorArray.shape
#print errorArray

plt.plot(errorArray)
plt.show();

#print sleep_data.shape



print "fin"




#training_epochs = 1000 numberOfBatches = 32 learning_rate = 0.001 n_hidden_1 = 38 ('Accuracy:', 0.9280303)
#training_epochs = 1000 numberOfBatches = 32 learning_rate = 0.0001 n_hidden_1 = 38 ('Accuracy:', 0.9075758)
#training_epochs = 5000 numberOfBatches = 32 learning_rate = 0.0001 n_hidden_1 = 38 ('Accuracy:', 0.9166667)
#training_epochs = 2000 numberOfBatches = 32 learning_rate = 0.0001 n_hidden_1 = 38 ('Accuracy:', 0.9106061) 6-7 min
#training_epochs = 2000 numberOfBatches = 32 learning_rate = 0.0001 n_hidden_1 = 38 ('Accuracy:', 0.9106061) 6 min
#training_epochs = 2000 numberOfBatches = 16 learning_rate = 0.0001 n_hidden_1 = 38 ('Accuracy:', 0.9159091) 13 min
#training_epochs = 2000 numberOfBatches = 64 learning_rate = 0.0001 n_hidden_1 = 38 ('Accuracy:', 0.91515154) 4 min
#training_epochs = 1000 numberOfBatches = 32 learning_rate = 0.0001 n_hidden_1 = 50 ('Accuracy:', 0.9227273) #all others had been 38
#training_epochs = 2000 numberOfBatches = 32 learning_rate = 0.0001 n_hidden_1 = 50 ('Accuracy:', 0.92651516)
#training_epochs = 3000 numberOfBatches = 64 learning_rate = 0.001 n_hidden_1 = 50 ('Accuracy:', 0.9439394)









