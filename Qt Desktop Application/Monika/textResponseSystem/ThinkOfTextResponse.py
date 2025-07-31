import os.path
import datetime
import ContactList
import TextFileHandler
import SendText
import TimestampHandler
import PathInitializer


#take the person's number, text message, and the time the message was received
#the formulate an appropriate response


#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/"
path = PathInitializer.path


#first, check if there's already a text log for this person
#check timestamp of last text you sent and they sent
#if not, check contacts list to get name and introduce self
	#if no name available, ask for name
def makeResponse(number, body, timestampTextSent):

	johnnyStatusString = TextFileHandler.checkValue(path + "JohnnyStatus.txt", "availability", 2)


	filePath = path + "Text Logs/" + number + ".txt"

	if os.path.isfile(filePath): #if txt file exists (if Monika knows this person)
		print "file exists"


		#check timestamp to see if a new introduction needs to be done and ensure Monika doesn't send 2 texts at once
		#still need to add this code
		
		print timestampTextSent
		sentTimeStamp = TimestampHandler.stringToTimestamp(timestampTextSent) #turns something in the format "2018-10-12T01:49:00" into a datetime object
		print sentTimeStamp

		#currentTimeStamp = datetime.datetime.now()

		lastTextTimestamp = TextFileHandler.checkValue(path+"Text Logs/"+number+".txt", "Timestamp")
		lastTextTimestamp = TimestampHandler.stringToTimestamp(lastTextTimestamp)

		if sentTimeStamp > (lastTextTimestamp + datetime.timedelta(minutes=30)): #if the received text is more than 30 minutes old, reset the conversation
			print "It's been so long! I'm gonna re introduce myself."
			TextFileHandler.setStatus(filePath, "Introduction", "0")
			TextFileHandler.setStatus(filePath, "FaqListOpen", "0")
			TextFileHandler.setStatus(filePath, "UnableToUnderstand", "0")
			TextFileHandler.setStatus(filePath, "ImportantAlertRequested", "0")

		else:
			print "sentTimeStamp:"
			print sentTimeStamp
			print ""
			print "sentTimeStamp + datetime.timedelta(minutes=5)):"
			print sentTimeStamp + datetime.timedelta(minutes=5)
			print ""
			print "lastTextTimestamp"
			print lastTextTimestamp






		


		#update the timestamp of last text received from a person
		#make sure this works
		TextFileHandler.setStatus(path+"Text Logs/"+number+".txt", "Timestamp", timestampTextSent)



		if TextFileHandler.checkValue(filePath, "Introduction") == "0": #if monika hasn't introduced herself this conversation
			#First message in conversation
			name = TextFileHandler.checkValue(filePath, "Name")
			response = "Hello again"
			if name == number: #if monika needs to ask for the name
				response+= "!"
			else: #monika already has their name
				response+= " " + name + "!"
			response+= " Johnny's "+johnnyStatusString+" right now, but just like before, text me \"IMPORTANT\" if you want me to try and get his attention.\n-Monika"
			TextFileHandler.setStatus(filePath, "Introduction", "1")
			return response
		else: #if monika is currently in a conversation with that person
			
			simplifiedBody = body.lower()
			#convert below block to a loop
			simplifiedBody = simplifiedBody.replace(" ", "")
			simplifiedBody = simplifiedBody.replace("!", "")
			simplifiedBody = simplifiedBody.replace(".", "")
			simplifiedBody = simplifiedBody.replace(",", "")
			simplifiedBody = simplifiedBody.replace("\'", "")
			simplifiedBody = simplifiedBody.replace("\"", "")
			if "important" in simplifiedBody: #if Monika was texted "Important"
				if TextFileHandler.checkValue(filePath, "ImportantAlertRequested") == "0": #if this is the first Important request of the conversation
					SendText.sendText("9413437452", "IMPORTANT TEXT RECEIVED!") #send important alert to my phone
					TextFileHandler.setStatus(filePath, "ImportantAlertRequested", "1")
					return "Thanks! I'm getting his attention now.\n-Monika"
				else:
					return "Sorry, I already tried getting Johnny's attention. His phone might be off or on silent.\n-Monika"



			FAQList = TextFileHandler.makeValueList(path+"FAQ List.txt")




			#send the FAQ list
			if "?" in body and TextFileHandler.checkValue(filePath, "FaqListOpen") == "0":
				TextFileHandler.setStatus(filePath, "FaqListOpen", "1")
				response = "To ask me one of these questions, just text me that question's number:"
				
				questionList = [i[0] for i in FAQList] #[i[0] for i in list] is a list of every first element in the main list (a list of all the tags)
				for i in xrange(len(FAQList)):
					response += "\n" + str(i+1) + ". " +questionList[i]

				return response
			

			#if the FAQ list has already been presented, see if the text is a number
			if TextFileHandler.checkValue(filePath, "FaqListOpen") == "1": 
				answerList = [i[1] for i in FAQList] #[i[0] for i in list] is a list of every first element in the main list (a list of all the tags)
				for i in xrange(len(FAQList)):
					if str(i+1) in body:
						return answerList[i] + "\n-Monika"



			#at this point, Monika has no idea what the message means

			if TextFileHandler.checkValue(filePath, "UnableToUnderstand") == "0": #if Monika hasn't said she couldn't understand before
				TextFileHandler.setStatus(filePath, "UnableToUnderstand", "1")
				response = "Sorry, I'm not sure what that means."
				if TextFileHandler.checkValue(filePath, "FaqListOpen") == "0": #if Monika hasn't presented the FAQ list before
					response += " If you want to ask me something, just send me a question mark \"?\" back."
				return response + "\n-Monika"
			#else: #if monika has already said she didn't understand what something means



		return ""





	else: #txt file doesn't exist, find name, make txt file, and introduce self
		print "file doesn't exist"

		#try to get name
		name = ContactList.findName(number)
		if (name == "-1"): #if there is no name in the contact list
			name = number

		newTxtFile = open(filePath,'w+') #make txt file
		newTxtFile.write("Name\t"+name+"\n"
						"Opinion\t20\n"
						"Timestamp\t"+timestampTextSent+"\n"
						"\n"
						"Introduction\t1\n"
						"FaqListOpen\t0\n"
						"UnableToUnderstand\t0\n"
						"ImportantAlertRequested\t0\n")

		response = "Hi"

		if name == number: #if monika needs to ask for the name
			response+= "!"
		else: #monika already has their name
			response+= " " + name + "!"


		response += " I'm Monika, a digital secretary Johnny made. Unfortunately he's "+johnnyStatusString+" right now, but if you message me \"IMPORTANT\" I'll let him know you texted right away.\n-Monika"

		return response




	#364






#print makeResponse("+16786410271", "hi", "08 09 2018 0244")


