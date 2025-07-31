import DeleteAllTextEmails
import SingleTextResponder
import time
import TextFileHandler
import PathInitializer
#import os

#print os.getcwd()

#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path

TextFileHandler.setStatus(path+"KeepLoopRunning.txt", "Toggle", "1")

DeleteAllTextEmails.deleteAll()


while TextFileHandler.checkValue(path+"KeepLoopRunning.txt", "Toggle")=="1":
	SingleTextResponder.respond()
	time.sleep(5)
	print "looping"
