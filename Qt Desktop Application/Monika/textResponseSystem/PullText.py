#checks the texts.txt file and prints the oldest text and deletes it from the file

import PathInitializer



#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path


def pull():

	#print "PullText.py"


	splitter = "&HJ BY&TGU(I&^"
	newMessageSplitter = "DUGUF^RCUY "


	#I'm an idiot!!!!! I didn't use the full path to get to texts.txt
	file = open(path+"texts.txt","r")


	texts = file.read()

	output = ""

	if(newMessageSplitter in texts):

		x = texts.find(newMessageSplitter) + len(newMessageSplitter) #the location the first message ends


		singleText = texts[:x-len(newMessageSplitter)] #the -2 removes the \n at the end of it from the textfile

		file.close()
		file = open(path+"texts.txt","w")
		file.write(texts[x:])
		file.close()


		output = singleText.split(splitter)

	#maybe account for another splitter existing in the string like if len>3
		'''
		print output[0]
		print output[1]
		print output[2]
		'''

	else:
		file.close()
		output = ""
		#print "*No Text Received*"

	return output