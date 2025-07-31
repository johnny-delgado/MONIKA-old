# A new approach to the IsJohnnySleeping neural network.
# This system takes a specific day as input and outputs the time it thinks I wake up and go to sleep.
# An initial problem I already anticipate is that this method can't deal with segmented sleep, naps, or any non one long sleep per day sleep style
# This method may, however, work better with a limited data set and then once I have enough data points I can use the original method of outputting the chance it thinks I'm sleeping at any given time
#18 June 2018 1220

import numpy as np

layer1_size = 20 #the size of the first hidden layer

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)


seconds_in_day = 24*60*60
#convert the number of seconds after midnight to a sin function (the output is between -1 and 1)
def sin_time(sec):
	return np.sin(2*np.pi*sec/seconds_in_day)
#same as sin_time but cos (used to help NN ignore how most times another time that returns the same value due to the fxn looking like a U)
def cos_time(sec):
	return np.cos(2*np.pi*sec/seconds_in_day)
#for x in xrange(86400):
#	if x % 1000 == 0:
#		print sin_time(x)


def sin_doty(doty):
	return np.sin(2*np.pi*doty/366)
#same as sin_time but cos (used to help NN ignore how most times another time that returns the same value due to the fxn looking like a U)
def cos_doty(doty):
	return np.cos(2*np.pi*doty/366)

#convert the hours past midnight into seconds past midnight
def hourToSec(hour):
	return hour*60.*60
#convert the inputs of days past jan 1, and current year into numbers between -1 and 1
'''def normalizeTimeSinceLightsTurnedOff(maxDelay, delay): #max is the longest delay b/t lights turning off and sleeping in training data
	if(min == max):
		return 1
	return (2*(year-min))/(max-min)-1
'''





#Input Neuron Definitions
#time is split into the sin and cos of how many seconds after midnight it is
#there is a different node for each day of the week. if it is that day, 1, if not, -1
"""
0 = Bias (always 1) - the b if this was y=mx+b and x was an input and m was a weight
1 = sin(time) - time of day (normalized between -1 and 1)
2 = cos(time) - time of day (normalized between -1 and 1)
3 = Sun (1 if yes, -1 if no)
4 = Mon
5 = Tues
6 = Wed
7 = Thurs
8 = Fri
9 = Sat
11 = day of the year (normalized between -1 and 1)
12 = year (normalized with oldest year as -1 and newest year as 1)
to add in the future maybe: time since lights turned off
"""

#Output Neuron Definitions
#each of these is given as a percentage of how sure Monika is that it's the answer
#the highest percentage is her decision
"""
0 awake
1 napping
2 sleeping
"""

#give random numbers same seed so we get the same sequence of generated numbers every time (good for debugging)
np.random.seed(1)

#the input array (either for training or testing)
X = np.empty([0, 10]) #initialize an empty array of this size [0 rows, # of col for the input vars we give it]
Y = np.empty([0, 2]) #the output array (either for training or testing)
minYear = 2018 #this will be reset once we setTeachingArray

"""set maxYear to current year even if I don't have data for this year b/c running test cases will be using the current year"""
maxYear = 2018 #current year

def setTeachingArray(numOfDataPoints):
	global X
	global Y
	global minYear
	

	#dotw (sunday is 1)
	#doty
	#year
	#time asleep
	#time awake	(napping = 1 sleeping = 2)
	#format: [5,81,2018,9000,9000,30300,2]
	Rules = np.vstack([[5,80,2018,9000,30300,2],
					[6,81,2018,14580,44400,2],
					[7,82,2018,16020,36900,2],
					[1,83,2018,19080,45900,2],
					[2,84,2018,10200,30600,2],
					[3,85,2018,12600,30300,2],
					[4,86,2018,9300,30900,2],
					[5,87,2018,9120,30300,2],
					[6,88,2018,8100,29100,2],
					[7,89,2018,13500,45000,2],
					[1,90,2018,14100,84180,2],
					[2,91,2018,16500,34080,2],
					[3,92,2018,8820,30900,2],
					[4,93,2018,12600,34800,2],
					[5,94,2018,13500,30300,2],
					[6,95,2018,14700,49500,2],
					[7,96,2018,17820,43200,2],
					[1,97,2018,18300,43800,2],
					[2,98,2018,4320,31020,2],
					[3,99,2018,6960,30900,2],
					[4,100,2018,4320,29700,2],
					[5,101,2018,11220,30900,2],
					[6,102,2018,12360,38100,2],
					[7,103,2018,19260,44280,2],
					[1,104,2018,13500,44100,2],
					[2,105,2018,7380,30300,2],
					[3,106,2018,10680,39600,2],
					[4,107,2018,5820,30900,2],
					[5,108,2018,8100,30900,2],
					[6,109,2018,19560,43200,2],
					[7,110,2018,7200,29100,2],
					[1,111,2018,7500,41940,2],
					[2,112,2018,6720,30960,2],
					[3,113,2018,5940,31260,2],
					[4,114,2018,9000,30960,2],
					[5,115,2018,9780,26880,2],
					[6,116,2018,17400,47700,2],
					[7,117,2018,17280,47160,2],
					[1,118,2018,12660,43200,2],
					[2,119,2018,11700,30600,2],
					[3,120,2018,16500,44940,2],
					[4,121,2018,10560,40260,2],
					[5,122,2018,6000,37680,2],
					[6,123,2018,17400,43800,2],
					[7,124,2018,15600,38700,2],
					[1,125,2018,22440,49200,2],
					[2,126,2018,23220,46800,2],
					[4,128,2018,1860,30600,2],
					[5,129,2018,90900,113700,2],
					[6,130,2018,3300,33300,2],
					[7,131,2018,12120,36420,2],
					[1,132,2018,8580,552600,2],
					[2,133,2018,13200,42060,2],
					[3,134,2018,19500,42900,2],
					[4,135,2018,16680,45300,2],
					[5,136,2018,19080,45900,2],
					[6,137,2018,16200,40200,2],
					[7,138,2018,19200,45540,2],
					[1,139,2018,21300,47940,2],
					[2,140,2018,15360,42360,2],
					[3,141,2018,14640,39900,2],
					[4,142,2018,14700,33480,2],
					[4,163,2018,12060,31500,2],
					[5,164,2018,11220,30300,2],
					[6,165,2018,8280,30600,2]])

	#make an array of the days the rules cover
	#then delete the excess days (days that have multiple rules: a nap, sleeping before midnight, segmented sleep, etc.)
	Days = Rules[0:len(Rules), 0:3] #copies the first 3 columns of Rules into Days
	Days = np.unique(Days, axis=0) #removes duplicate rows
	for row in xrange(len(Days)):

		#progress bar
		'''if ( (row+1) % (len(Days)/20)) == 0:
			print "Creating data for day #" + str(row+1)
			print str( (row+1.)/len(Days) ) + " complete"
		'''
		#print "data point #" + str(row)



		dotw = Days[row,0]

		doty = Days[row,1]
		#normalizedDoty = normalizeDayOfTheYear(doty)

		Years = Rules[0:len(Rules), 2] #copies the first 3 columns of Rules into Days
		Years = np.unique(Years, axis=0) #removes duplicate rows
		minYear = np.amin(Years, axis=0) #the oldest year that the data encompases
		
		year = Days[row,2]

		#print Days



		Sun=Mon=Tues=Wed=Thur=Fri=Sat= -1
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


		output = 0
		
		for a in xrange(len(Rules)): #go through all the rules
			if Rules[a,2]==year and Rules[a,1]==doty: #and figure out which ones are for this day
				timeAsleep = Rules[row,4]
				timeAwake = Rules[row,3]
				
				


		trainingOutput = [timeAwake,timeAsleep]


		trainingEx = [1, Sun,Mon,Tues,Wed,Thur,Fri,Sat , sin_doty(doty), cos_doty(doty)]
		X = np.vstack([X, trainingEx])
		Y = np.vstack([Y, trainingOutput])


		#print out the test data time and status
		#print "when it is " + str(time/(60*60)) + " hours, Johnny is [" + str(awake) + ", " + str(napping) + ", " + str(sleeping) + "]" 




	
	#print len(X.T) #.T transposes the array and in this case causes the return to be the number of rows
		

	

# randomly initialize our weights with mean 0
# synapse_n = 2*np.random.random((number of inputs from layer n, number of outputs to layer n+1)) - 1
synapse_0 = 2*np.random.random((len(X.T),layer1_size)) - 1
synapse_1 = 2*np.random.random((layer1_size,len(Y.T))) - 1


#to be turned into a fxn in its own file that will be used to train all neural networks eventually
#train a neural network that has 1 hidden layer with the given paramaters and return the modified synapses
#make several versions of this function for varrying levels of hidden layers
#make a version of this that doesn't take the synapses as an input but instead an int for number of hidden layers. it will randomly generate synapse values inside this function
#X = input teaching array
#Y = output teaching array
#synapse_0 = connects the input nodes to hidden layer 1
#synapse_1 = connects hidden layer 1 to the output nodes
#iterations = how many times you want the neural network to train with the data set (ex. 100000)
#alpha = a multiplier to the amount that the synapses (weights) will change each iteration (ex. 0.01, 0.1, 1, 10) increase if the error doesn't go down fast enough and decrease it if the error stops going down at a certain point or doesn't go down fast enough
def teachMonika(X, Y, s0, s1, iterations, alpha):
	synapse_0 = s0
	synapse_1 = s1
    
	for j in xrange(iterations):

		# Feed forward through layers 0, 1, and 2
		layer_0 = X
		layer_1 = sigmoid(np.dot(layer_0,synapse_0))
		layer_2 = sigmoid(np.dot(layer_1,synapse_1))

		# how much did we miss the target value?
		layer_2_error = layer_2 - Y

		if ( (j+1) % (iterations/100)) == 0:
			print "Error after "+str(j+1)+" iterations:" + str(np.mean(np.abs(layer_2_error)))

		# in what direction is the target value?
		# were we really sure? if so, don't change too much.
		layer_2_delta = layer_2_error*sigmoid_output_to_derivative(layer_2)

		# how much did each l1 value contribute to the l2 error (according to the weights)?
		layer_1_error = layer_2_delta.dot(synapse_1.T)

		# in what direction is the target l1?
		# were we really sure? if so, don't change too much.
		layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)

		synapse_1 -= alpha * (layer_1.T.dot(layer_2_delta))
		synapse_0 -= alpha * (layer_0.T.dot(layer_1_delta))
		#print j+1

	return synapse_0, synapse_1





#the synapses are what have to be saved to let Monika continue learning from where she left off
#alternately: just save the training data I used and add to the set and retrain her each time I modify the NN, although that might require me to revamp the training data each time



setTeachingArray(100) #how many data points per day in teaching array
synapse_0, synapse_1 = teachMonika(X, Y, synapse_0, synapse_1, 10000000, .00001) #number of iterations through training array, alpha value (change per iteration) #https://stackoverflow.com/questions/11690333/is-it-possible-to-return-two-lists-from-a-function-in-python

#export synapse_0 and synapse_1 to text files


np.savetxt('synapse_0', synapse_0);
np.savetxt('synapse_1', synapse_1);







