import sys
import TextFileHandler
import PathInitializer


#ex) python QtTextFileModifyer.py JohnnyStatus.txt availability 1 busy
#argument 1 [0] is always QtTextFileModifyer.py
#argument 2 [1] the text file name
#argument 3 [2] the tag to modify
#argument 4 [3] the new value
#argument 5 [4] an optional third value for things like explanations for being busy


#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path

#ensure both inputs are strings
#setStatus("Text Logs/9418073003.txt", "Introduction", "20")
def setStatusAndFlavorText(path, tag, newValue, flavorText):
	valueList = TextFileHandler.makeValueList(path) #make the list of values from the .txt file


	tagLocation = TextFileHandler.findElementLocation(valueList, tag)
	if(tagLocation != -1):
		valueList[tagLocation][1] = newValue
		valueList[tagLocation][2] = flavorText

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



if(len(sys.argv)==4):
	TextFileHandler.setStatus(path + sys.argv[1], sys.argv[2], sys.argv[3])

if(len(sys.argv)==5):
	setStatusAndFlavorText(path + sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


