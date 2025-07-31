#returns a list with elements like this:
#[['availability', '-1'], ['hotness', '1000'], ['cuteness', '99999999']]
def makeValueList(path):
	file = open(path,"r")
	textFile = file.read()
	file.close()
	valueList = textFile.split("\n")

	#now split up each line into list elements
	numberOfTags = len(valueList)
	for i in xrange(numberOfTags):
		valueList[i] = valueList[i].split("\t")
	return valueList





#returns the row that tag is found in (only checking column 0)
#if the tag doesn't exist in column 0, return -1
def findElementLocation(list, tag):
	tagList = [i[0] for i in list] #[i[0] for i in list] is a list of every first element in the main list (a list of all the tags)
	numberOfTags = len(tagList)
	for i in xrange(numberOfTags):
		if tagList[i] == tag:
			return i
	return -1



#returns the value of the given tag (the value immediately to the right of the tag in the text file)
#returns "" if the tag doesn't exist
#checkValue("Text Logs/9418073003.txt", "Introduction")
#the index is which column value you want to pull (0 is the location of the tag)
def checkValue(path, tag, index = 1):
	valueList = makeValueList(path)
	tagLocation = findElementLocation(valueList, tag)
	if(tagLocation != -1):
		value = valueList[tagLocation][index]
		#print value
		return value
	else:
		#print "Tag not found."
		return ""
	file.close()





#ensure both inputs are strings
#setStatus("Text Logs/9418073003.txt", "Introduction", "20")
def setStatus(path, tag, newValue):
	valueList = makeValueList(path) #make the list of values from the .txt file


	tagLocation = findElementLocation(valueList, tag)
	if(tagLocation != -1):
		valueList[tagLocation][1] = newValue

		statusString = ""
		for row in xrange(len(valueList)):
			for col in xrange(len(valueList[row])):
				statusString += valueList[row][col]
				if col+1 < len(valueList[row]):
					statusString += "\t"
			if row+1 < len(valueList):
				statusString += "\n"
		file = open(path,"w")
		file.write(statusString)
		file.close()
	else: #if the tag doesn't exist, make a new tag with the given value
		print "tag not found, creating new tag"
		file = open(path,"a")
		file.write("\n" + tag + "\t" + newValue)
		file.close()


