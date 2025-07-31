# this script sends a text to my cell number via twilio
# the form is: recipientPhoneNumber*messageBody
#
# tasker then takes any text received from the twilio number
# and sends the messageBody as a text to the recipientPhoneNumber
#
# 9 Sep 2018
# 
# based on the 'Sending Text Messages with Twilio' section from Al Sweigart's book 'Automate the Boring Stuff With Python'
# monitor how many texts I send and how much it costs on twilio.com/console/usage


from twilio.rest import Client
#ex) sendText(9413437452, 'Hello World!')
def sendText(number, text):
	accountSID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	authToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	twilioCli = Client(accountSID, authToken)
	myTwilioNumber = '+XXXXXXXXXXX'
	myCellPhone = '+XXXXXXXXXXX'


	recipientPhoneNumber = number


	#text = 'Hello World!\n-Love Monika'


	split = '*<@/?[,>(!' #used by Tasker to split up the message (It's justmonika but with the default special characters for those letters in my phone)

	message = twilioCli.messages.create(
							body=split+recipientPhoneNumber+split+text,
							from_=myTwilioNumber,
							to=myCellPhone) #begin with the split symbol to compensate for twilio's trial account message preface


	#updatedMessage = twilioCli.messages.get(message.sid)
	#updatedMessage.status # should return queued', 'sending', 'sent', 'delivered', 'undelivered', or 'failed'











