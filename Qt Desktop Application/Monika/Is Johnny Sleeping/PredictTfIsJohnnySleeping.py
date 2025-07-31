# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import pandas as pd
import sys

#min is the oldest year in our data set, max is the current year regardless of if we have data on it
minYear = 2018
maxYear = 2018



print "beginning program"



#this first couple dozen lines of code prep the weights and biasses to be the right size to then load the pre saved (trained) values

#load data
sleep_data = pd.read_csv("SleepTrainingData.csv", sep=";")
#print sleep_data.shape #(number of datapoints, number of values in each datapoint)

print "line 2"


input_data = sleep_data[["control", "sin_time", "cos_time", "Sun","Mon","Tues","Wed","Thur","Fri","Sat" , "sin_doty", "cos_doty", "normalizedYear"]]
output_data = sleep_data[["awake", "napping","sleeping"]]

n_hidden_1 = 50 #number of neurons in the hidden layer
n_input = input_data.shape[1] # 13
n_output = output_data.shape[1] # 3

weights = {
	'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
	'out': tf.Variable(tf.random_normal([n_hidden_1, n_output]))
} 

biases = {
	'b1': tf.Variable(tf.random_normal([n_hidden_1])),
	'out': tf.Variable(tf.random_normal([n_output]))
}



#load weights and biasses from save files
saver = tf.train.Saver()



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


def predict_state(inputPoint):

	print "arrived at predict_state"

	with tf.Session() as sess:
		# Restore variables from disk.
		saver.restore(sess, "/Users/Johnny/Monika/Qt Desktop Application/Monika/Is Johnny Sleeping/TrainedSleepPredictionSess")
		#print("Model restored.")
		# Check the values of the variables
		#print("v1 : %s" % weights.eval())
		#print("v2 : %s" % biases.eval())




		#print "You were sleeping and I thought you were..."


		guess = multilayer_perceptron(inputPoint, weights, biases, 1.)

		#print guess.shape # (1, 3)
		#print guess # Tensor("add_1:0", shape=(1, 3), dtype=float32)   # same as print (guess)
		#print (sess.run(guess)) # [[6.0709867  -50.731033  8.735189]] #prints out the values of her guesses of each state

		sleepGuess = sess.run(guess[[0,0]])
		napGuess = sess.run(guess[[0,1]])
		awakeGuess = sess.run(guess[[0,2]])

		#Monika's final guess on my state
		# 0 if awake
		# 1 if napping
		# 2 if sleeping
		finalPrediction = 2
		if(sleepGuess > napGuess and sleepGuess > awakeGuess):
			finalPrediction = 0
		if(napGuess > sleepGuess and napGuess > awakeGuess):
			finalPrediction = 1
		if(awakeGuess > sleepGuess and awakeGuess > napGuess):
			finalPrediction = 2

		"I think you're at state:"
		print finalPrediction



seconds_in_day = 24*60*60
#convert the number of seconds after midnight to a sin function (the output is between -1 and 1)
def sin_time(sec):
	return np.sin(2*np.pi*sec/seconds_in_day)
#same as sin_time but cos (used to help NN ignore how most times another time that returns the same value due to the fxn looking like a U)
def cos_time(sec):
	return np.cos(2*np.pi*sec/seconds_in_day)
def sin_doty(doty):
	return np.sin(2*np.pi*doty/366)
def cos_doty(doty):
	return np.cos(2*np.pi*doty/366)
#min is the oldest year in our data set, max is the current year regardless of if we have data on it
def normalizeYear(year):
	global minYear
	global maxYear
	if(minYear == maxYear):
		return 1
	return (2*(year-minYear))/(1.0*maxYear-minYear)-1


#convert from normal timestamp to an array of numbers between -1 and 1 I think [1, sin_time(time), cos_time(time), Sun,Mon,Tues,Wed,Thur,Fri,Sat , sin_doty(doty), cos_doty(doty), normalizedYear]
def convertTimestamp(currentHour, dotw, doty, year):
	#trainingEx = [1, sin_time(time), cos_time(time), Sun,Mon,Tues,Wed,Thur,Fri,Sat , sin_doty(doty), cos_doty(doty), normalizedYear]
	
	time = currentHour*60*60 #the time in sec after midnight

	Sun=Mon=Tues=Wed=Thur=Fri=Sat= 0
	if dotw == 1:
		Sun = 1
	elif dotw == 2:
		Mon = 1
	elif dotw == 3:
		Tues = 1
	elif dotw == 4:
		Wed = 1
	elif dotw == 5:
		Thur = 1
	elif dotw == 6:
		Fri = 1
	elif dotw == 7:
		Sat = 1

	return [1, sin_time(time), cos_time(time), Sun,Mon,Tues,Wed,Thur,Fri,Sat , sin_doty(doty), cos_doty(doty), normalizeYear(year)]



# expected sleeping points are called sleep_n
'''
sleepyBoi_1 = [[1.000000000000000000e+00,9.858206292667875958e-01,1.678025235568137152e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,6.979441547663435275e-01,-7.161521883143933120e-01,1.000000000000000000e+00]]
sleepyBoi_2 = [[1.000000000000000000e+00,5.315418351017969778e-01,-8.470320404427533756e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,8.483511978123039476e-01,-5.294338912181851819e-01,1.000000000000000000e+00]]
sleepyBoi_3 = [[1.000000000000000000e+00,9.605302828123596370e-01,-2.781754406852058326e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,9.805753940631429799e-01,-1.961425414281968704e-01,1.000000000000000000e+00]]
sleepyBoi_4 = [[1.000000000000000000e+00,7.883919336750275786e-01,-6.151732755217433901e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,9.990791668951153337e-01,4.290475819955437420e-02,1.000000000000000000e+00]]
sleepyBoi_5 = [[1.000000000000000000e+00,4.104894335987944731e-01,-9.118653545912032143e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,9.867305793119813817e-01,1.623661413307639911e-01,1.000000000000000000e+00]]

awakeBoi_1 = [[1.000000000000000000e+00,-9.943109243671389708e-01,-1.065165981627540087e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,9.499899229945010237e-01,-3.122805568857948133e-01,1.000000000000000000e+00]]
awakeBoi_2 = [[1.000000000000000000e+00,-7.216798576690799383e-01,6.922269736399589979e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,9.970175264485267030e-01,-7.717546212664619376e-02,1.000000000000000000e+00]]
awakeBoi_3 = [[1.000000000000000000e+00,3.590459640354806692e-01,9.333198785570959721e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,9.867305793119813817e-01,1.623661413307639911e-01,1.000000000000000000e+00]]
awakeBoi_4 = [[1.000000000000000000e+00,-8.026429878081167146e-01,5.964597506307188768e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,0.000000000000000000e+00,7.101350157125357887e-01,-7.040655221348057768e-01,1.000000000000000000e+00]]
awakeBoi_5 = [[1.000000000000000000e+00,-9.601856347205081077e-01,-2.793627514118068311e-01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00,6.979441547663435275e-01,-7.161521883143933120e-01,1.000000000000000000e+00]]

predict_state(sleepyBoi_1)
predict_state(sleepyBoi_2)
predict_state(sleepyBoi_3)
predict_state(sleepyBoi_4)
predict_state(sleepyBoi_5)

predict_state(awakeBoi_1)
predict_state(awakeBoi_2)
predict_state(awakeBoi_3)
predict_state(awakeBoi_4)
predict_state(awakeBoi_5)
'''

#print "testing timestamp converter"
#time1 = [convertTimestamp(7, 4, 177, 2018)] #7am
#predict_state(time1)
'''
predict_state( [convertTimestamp(7, 4, 177, 2018)] ) #7am
predict_state( [convertTimestamp(8, 4, 177, 2018)] ) #8am
predict_state( [convertTimestamp(8.5, 4, 177, 2018)] ) #8:30am
predict_state( [convertTimestamp(9, 4, 177, 2018)] ) #9am
predict_state( [convertTimestamp(3.25, 4, 178, 2018)] ) #3:15am
predict_state( [convertTimestamp(3.5, 4, 178, 2018)] ) #3:30am
predict_state( [convertTimestamp(4, 4, 178, 2018)] ) #4am
'''

#argument 1 is always the name of the .py file
#argument 2 current time in hours (as a decimal number between 0 and 24)
#argument 3 day of the week (1 = sunday)
#argument 4 day of the year
#argument 5 year
#ex. python PredictTfIsJohnnySleeping.py 1.75 1 237 2018
if len(sys.argv)==5:
	inputTime = float(sys.argv[1])
	inputDotw = int(sys.argv[2])
	inputDoty = int(sys.argv[3])
	inputYear = int(sys.argv[4])
	predict_state( [convertTimestamp(inputTime, inputDotw, inputDoty, inputYear)] )
	#print "worked"
else:
	print "Wrong number of arguments given to PredictTfIsJohnnySleeping.py"

#Monika's final guess on my state
# 0 if awake
# 1 if napping
# 2 if sleeping








