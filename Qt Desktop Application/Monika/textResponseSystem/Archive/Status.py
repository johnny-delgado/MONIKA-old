#OBSOLETE!!!
#this stuff has been transgered to the general TextFileHandler.py


#working/finished as of 31 August 2018 0137
#this script queries and modifies the JohnnyStatus.txt file

#one function for modifying availability and another for reading it
#another script should call the NN if avilibility == -1

#.txt file is in format:
'''
availability	-1
hotness	1000
cuteness	99999999
'''



#returns a list with elements like this:
#[['availability', '-1'], ['hotness', '1000'], ['cuteness', '99999999']]
def makeStatusArray():
	file = open("JohnnyStatus.txt","r")
	JohnnyStatus = file.read()
	file.close()
	statusArray = JohnnyStatus.split("\n")

	#now split up each line into list elements
	numberOfTags = len(statusArray)
	for i in xrange(numberOfTags):
		statusArray[i] = statusArray[i].split("\t")
	return statusArray



#returns the row that tag is found in (only checking column 0)
#if the tag doesn't exist in column 0, return -1
def findElementLocation(array, tag):
	tagList = [i[0] for i in array] #[i[0] for i in array] is a list of every first element in the main list (a list of all the tags)
	numberOfTags = len(tagList)
	for i in xrange(numberOfTags):
		if tagList[i] == tag:
			return i
	return -1



#returns the value of the given tag (the value immediately to the right of the tag in the text file)
#returns "" if the tag doesn't exist
#checkStatus("availability")
def checkStatus(tag):
	JohnnyStatus = makeStatusArray()
	tagLocation = findElementLocation(JohnnyStatus, tag)
	if(tagLocation != -1):
		value = JohnnyStatus[tagLocation][1]
		#print value
		return value
	else:
		#print "Tag not found."
		return ""
	file.close()



#ensure both inputs are strings
#setStatus("availability", "1")
def setStatus(tag, newValue):
	JohnnyStatus = makeStatusArray() #make the list of values from the .txt file


	tagLocation = findElementLocation(JohnnyStatus, tag)
	if(tagLocation != -1):
		JohnnyStatus[tagLocation][1] = newValue

		statusString = ""
		for row in xrange(len(JohnnyStatus)):
			for col in xrange(len(JohnnyStatus[row])):
				statusString += JohnnyStatus[row][col]
				if col+1 < len(JohnnyStatus[row]):
					statusString += "\t"
			if row+1 < len(JohnnyStatus):
				statusString += "\n"
		file = open("JohnnyStatus.txt","w")
		file.write(statusString)
		file.close()
	else: #if the tag doesn't exist, make a new tag with the given value
		print "tag not found, creating new tag"
		file = open("JohnnyStatus.txt","a")
		file.write("\n" + tag + "\t" + newValue)
		file.close()





#availability: -1 unknown, 0 available, 1 busy, 2 sleeping, 3 napping