import numpy as np

minYear = 2018 #this will be reset once we setTeachingArray

"""set maxYear to current year even if I don't have data for this year b/c running test cases will be using the current year"""
maxYear = 2018 #current year


# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output


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


#convert the hours past midnight into seconds past midnight
def hourToSec(hour):
	return hour*60.*60
#convert the inputs of days past jan 1, and current year into numbers between -1 and 1
#def normalizeDayOfTheYear(day):
#	return day/183.-1
def normalizeYear(year): #min is the oldest year in our data set, max is the current year regardless of if we have data on it
	global minYear
	global maxYear
	if(minYear == maxYear):
		return 1
	return (2*(year-minYear))/(1.0*maxYear-minYear)-1


#load the synapses from text files produced by TrainIsJohnnySleeping.py
synapse_0 = open('synapse_0', 'r')
synapse_1 = open('synapse_1', 'r')
synapse_0 = np.loadtxt(synapse_0)
synapse_1 = np.loadtxt(synapse_1)
#print(synapse_1)




#time = hours after midnight
#dotw = day of the week (sunday is 1)
#doty = Jan 1 is 0, December 31 is 365 or 366 depending on leap year
#year = current year ex. 2018
def isJohnnySleepingAt(hour, dotw, doty):

	#print "at " + str(hour) + " hours you are..."

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

	sec = hourToSec(hour) #we give seconds past midnight to sin_time() and cos_time
	#day = normalizeDayOfTheYear(doty)
	#normalizedYear = normalizeYear(year)

	layer_0 = [1, sin_time(sec), cos_time(sec), Sun, Mon, Tues, Wed, Thur, Fri, Sat]
	layer_1 = sigmoid(np.dot(layer_0,synapse_0))
	layer_2 = sigmoid(np.dot(layer_1,synapse_1))
	return layer_2

print isJohnnySleepingAt(12.15, 5, 164) #isJohnnySleepingAt(time, dotw (1=sun), doty, year)





#a for loop
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step




#return the time Monika thinks with a given confidence amount that I'm at a given state
	#dotw (1=sun)
	#doty, year
	#desired state you want to know about: wake nap or sleep
	#probability threshold you count as Monika being sure
	#minHour & maxHour = the range of times to check for the desired state change
def predictStateTime(dotw, doty, state, prob, minHour, maxHour): 
	#I'm almost always asleep at 7am and I won't wake up after 8pm

	hourRange = maxHour - minHour #makes the max hour in the for loop maxHour if the range doesn't cross midnight
	if(minHour>maxHour):
		hourRange = 24 - minHour + maxHour


	for h in my_range(minHour, minHour + hourRange, 0.05):
		#print "hour is: " + str(h)
		hour = h
		if(h > 24): #account for 
			hour = h-24
			dotw += 1
			doty += 1
		chanceInState = isJohnnySleepingAt(hour, dotw, doty)[state]
		if (chanceInState >= prob):
			return hour



#account for weeks that cross years
def predictNextWeek(startDotw , startDoty, state, prob, minHour, maxHour): # dotw (of start day), doty (of start day)
	for day in range(0, 7): #[0,7) | 0 = start of week we're asking about
		print predictStateTime(startDotw+day, startDoty+day, state, prob, minHour, maxHour)


'''print predictStateTime(5, 164, 2018, 0, .5, 0, 24)
print predictStateTime(6, 165, 2018, 0, .5, 0, 24)
print predictStateTime(7, 166, 2018, 0, .5, 0, 24)
print predictStateTime(8, 167, 2018, 0, .5, 0, 24)
print predictStateTime(9, 168, 2018, 0, .5, 0, 24)
print predictStateTime(10, 169, 2018, 0, .5, 0, 24)
print predictStateTime(11, 170, 2018, 0, .5, 0, 24)
'''

print "wake times:"
predictNextWeek(1, 167, 0, .5, 7, 20)

print "bed times:"
predictNextWeek(1, 167, 2, .5, 20, 6)







