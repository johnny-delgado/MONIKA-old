import datetime
import CheckText
import PullText
import TextFileHandler
import ThinkOfTextResponse
import SendText
import PathInitializer


#check and delete the email of one text
#respond if necessisary


#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path


print "Running SingleTextResponder.py"

def respond():
	print "responding"

	CheckText.getTexts()

	print "done sleeping"


	newTextInfo = PullText.pull() #ex. ['7706801238', 'Emoji', 'Tue Aug 28 22:28:33 EDT 2018']

	print "newTextInfo is:"
	print newTextInfo

	if len(newTextInfo) == 3: #if I got a text   //(probably make the minimum length longer) //maybe add   && newText.left(firstSplit) != 9413437452
		print "new text received"
		phoneNumber = newTextInfo[0] #phone number
		body = newTextInfo[1] #body
		timeStamp = newTextInfo[2] #timestamp of when the text was sent


		currentTimeStamp = datetime.datetime.now()


		#setting the time that the text was received to compare it to the current time
		timeStampList = timeStamp.split(' ')
		year = int(timeStampList[5])

		monthWord = timeStampList[1]
		month = 0 #maybe set it to currentTimeStamp.month
		monthList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		for i in xrange(len(monthList)): #i goes from 0 to 1 1
			if monthWord == monthList[i]:
				month = i+1
		if month == 0:
			month = currentTimeStamp.month
			print "ERROR: The month didn't poperly get read from the text time stamp!"

		day = int(timeStampList[2])

		timeList = timeStampList[3].split(':') #a list of [hour, minutes, seconds]
		hour = int(timeList[0])
		minute = int(timeList[1])
		second = int(timeList[2])


		#add seconds (with a range of 4 minutes every second impacts the system)


		#the time the text was received
		textTimeStamp = datetime.datetime(year, month, day, hour, minute, second) #(year, month, day[, hour[, minute[, second]]])




		if (textTimeStamp + datetime.timedelta(minutes=4)) >= currentTimeStamp: #if the received text isn't more than ~4 minutes old
			if phoneNumber != "9413437452": #not a text from Johnny
				if phoneNumber != "9412200945": #not a text from twilio
					johnnyStatus = TextFileHandler.checkValue(path + "JohnnyStatus.txt", "availability")
					if johnnyStatus == "-1": #If Johnny's status is unknown
						

						#check time new text was received compared to time of last text sent to ensure Monika never sends 2 texts in a row before the other person texts her
						#also check to see if the conversation hasn't progressed in over 20-30 minutes and if that's the case, say hello again
						#also eventually check to see if johnny texted them in between messages, johnny texting someone should reset their conversation status



						print "checking NN and setting JohnnyStatus.txt accordingly would go here"
					




					if johnnyStatus != "0" and johnnyStatus != "-1": #if Johnny is unavailable
						print "Johnny is unavailable, let's think of a response"

						response = ""
						response = ThinkOfTextResponse.makeResponse(phoneNumber, body, textTimeStamp.isoformat()) #maybe append textTimeStamp with .isoformat()
						if response != "":
							print "Sending text: " + response
							SendText.sendText(phoneNumber, response) #send important alert to my phone
						else:
							print "No text will be sent."


			else: #if the text was from Johnny
				print "text from johnny"


	else:
		print "No new text received."


#respond()

print "SingleTextResponder.py is done"

