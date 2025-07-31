#complete and working as of [27 June 2018 0025]
#modify it as needed to add more variables, change formats of existing variables, and continue to add new data

import numpy as np
import csv

minYear = 2018
maxYear = 2018

#the input array (either for training or testing)
X = np.empty([0, 13]) #initialize an empty array of this size [0 rows, # of col for the input vars we give it]
Y = np.empty([0, 3]) #the output array (either for training or testing)

trainingData = np.empty([0, 16]) #13 inputs + 3 outputs
#trainingData = np.vstack(["control", "sin_time", "cos_time", "Sun","Mon","Tues","Wed","Thur","Fri","Sat" , "sin_doty", "cos_doty", "normalizedYear", "awake","napping","sleeping"])


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


def setTeachingArray(pointsPerDay):
	global X
	global Y
	global trainingData
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
					[2,84,2018,57600,62100,1],
					[3,85,2018,12600,30300,2],
					[4,86,2018,9300,30900,2],
					[5,87,2018,9120,30300,2],
					[6,88,2018,8100,29100,2],
					[7,89,2018,13500,45000,2],
					[1,90,2018,14100,40800,2],
					[1,90,2018,71940,84180,2],
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
					[7,103,2018,61080,63000,1],
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
					[3,127,2018,10320,27600,2],
					[3,127,2018,87600,286200,2],
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
					[4,163,2018,60420,69900,1],
					[5,164,2018,11220,30300,2],
					[6,165,2018,8280,30600,2]])

	#make an array of the days the rules cover
	#then delete the excess days (days that have multiple rules: a nap, sleeping before midnight, segmented sleep, etc.)
	Days = Rules[0:len(Rules), 0:3] #copies the first 3 columns of Rules into Days
	Days = np.unique(Days, axis=0) #removes duplicate rows
	for row in xrange(len(Days)): #for each day

		#progress bar
		if ( (row+1) % (len(Days)/20)) == 0:
			print "Creating data for day #" + str(row+1)
			print str( (row+1.)/len(Days) ) + " complete"
		#print "data point #" + str(row)



		dotw = Days[row,0]

		doty = Days[row,1]
		#normalizedDoty = normalizeDayOfTheYear(doty)

		Years = Rules[0:len(Rules), 2] #copies the first 3 columns of Rules into Days
		Years = np.unique(Years, axis=0) #removes duplicate rows
		minYear = np.amin(Years, axis=0) #the oldest year that the data encompases
		
		year = Days[row,2]
		normalizedYear = normalizeYear(year)

		#print Days


		for i in xrange(pointsPerDay): #make this many data points per day


			time = 86400*np.random.random()

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


			output = 0
			
			for a in xrange(len(Rules)): #go through all the rules
				if Rules[a,2]==year and Rules[a,1]==doty: #and figure out which ones are for this day
					timeAsleep = Rules[row,3]
					timeAwake = Rules[row,4]
					
					#look at this line to see if I messed something up (account for between midnight times)

					# (time >= timeAsleep and time < timeAwake) for falling asleep and waking up without crossing midnight
					# (time >= timeAsleep and timeAwake < timeAsleep) for the pre midnight part of falling asleep before midnight and waking up after midnight
					# (time <= timeAwake and timeAsleep > timeAwake) for the post midnight part of falling asleep before midnight and waking up after midnight
					if (time >= timeAsleep and time < timeAwake) or (time >= timeAsleep and timeAwake < timeAsleep) or (time <= timeAwake and timeAsleep > timeAwake): #then see if the random time we're interested in is within this rule (I'm sleeping or napping at that time)
						output = Rules[row,5] #if so, set the output to either sleeping or napping

			awake=napping=sleeping=0
			if output == 0:
				awake = 1
			elif output == 1:
				napping = 1
			elif output == 2:
				sleeping = 1

			trainingEx = [1, sin_time(time), cos_time(time), Sun,Mon,Tues,Wed,Thur,Fri,Sat , sin_doty(doty), cos_doty(doty), normalizedYear]
			trainingOutput = [awake,napping,sleeping]
			newDataLine = [1, sin_time(time), cos_time(time), Sun,Mon,Tues,Wed,Thur,Fri,Sat , sin_doty(doty), cos_doty(doty), normalizedYear, awake,napping,sleeping]

						

			X = np.vstack([X, trainingEx])
			Y = np.vstack([Y, trainingOutput])
			trainingData = np.vstack([trainingData, newDataLine])

			#print out the test data time and status
			#print "when it is " + str(time/(60*60)) + " hours, Johnny is [" + str(awake) + ", " + str(napping) + ", " + str(sleeping) + "]" 




	
	#print len(X.T) #.T transposes the array and in this case causes the return to be the number of rows
	

setTeachingArray(200) #number of data points per day
#print X
#print Y
#np.savetxt('input data.csv', X, delimiter=",");
#np.savetxt('output data.csv', Y, delimiter=",");



with open('SleepTrainingData.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["sin_time", "cos_time", "Sun","Mon","Tues","Wed","Thur","Fri","Sat", "awake","napping","sleeping"])

np.savetxt('SleepTrainingData.csv', trainingData, delimiter=";", header="control;sin_time;cos_time;Sun;Mon;Tues;Wed;Thur;Fri;Sat;sin_doty;cos_doty;normalizedYear;awake;napping;sleeping", comments='');


