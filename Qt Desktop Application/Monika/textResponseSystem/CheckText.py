'''
Checks the oldest email in monikatextalerts@gmail.com
ensures email is a text from the text to email app I have
returns an array with the sender info and message
'''



import imapclient
import imaplib
import pyzmail
import re
#import getpass
import PathInitializer


#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path

def getTexts():

	#print "CheckText.getTexts() is running"

	imaplib._MAXLINE = 10000000 #increases the byte limit of how much python can remember

	#create an IMAPClient object (ssl allows encryption which some email providers require)
	imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True) #client is the object that connects to the server
	imapObj.login('monikatextalerts@gmail.com', 'mwzifhbskvmyngae' ) #getpass.getpass('Email Password:') asks for the user to input a password

	#print imapObj.list_folders() #all the folders my gmail has
	imapObj.select_folder('INBOX', readonly=False) #turn this off to allow Monika to mark emails as read and delete them

	UIDs = imapObj.search(['ALL']) #returns the ID's of all emails
	#print UIDs

	rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
	#print rawMessages


	if UIDs: #if there is at least 1 message in my inbox
		#print "messages!"

		messageID = 0

		#check to see if message contains the string "Received the SMS at: " which should be unique to the text message emails. maybe also check that it's from monikatextalerts@gmail.com
		for i in UIDs:
			message = pyzmail.PyzMessage.factory(rawMessages[i]['BODY[]']) #create a PyzMessage object of the email
			

			#decode the plaintext and html parts of the email
			if message.html_part != None: #if the email has html
				body = message.html_part.get_payload().decode(message.html_part.charset)
			if message.text_part != None: #if the email has plaintext
				# (if there's both an html and text part, use the text part)
				body = message.text_part.get_payload().decode(message.text_part.charset)


			if (body.find('Received the SMS at: ') > 1):
				#print "found text at: " + str(i)
				messageID = i
				#print "about to break"
				break
			#else:
				#print body.find('Received the SMS at: ')

			#endSender = message.find('Google')
			#print "your text is in another email"

		#print "got out"

		message = pyzmail.PyzMessage.factory(rawMessages[messageID]['BODY[]']) #create a PyzMessage object of the email

		#decode the plaintext and html parts of the email
		if message.html_part != None:
			cleanMessage = message.html_part.get_payload().decode(message.html_part.charset)
		if message.text_part != None:
			# (if there's both an html and text part, use the text part)
			cleanMessage = message.text_part.get_payload().decode(message.text_part.charset)

		#print cleanMessage

		#get sender's name
		endSender = cleanMessage.find('(') - 1 #find where the sender name ends (assuming I don't have a left parenthesis in my contact names)
		sender = cleanMessage[8:endSender]
			
		cleanMessage = cleanMessage[endSender+2:]#cut down message string

		#get sender's phone number
		endNumber = cleanMessage.find(')')
		number = cleanMessage[:endNumber]
		if len(number)>=10 and len(number)<=15: #the legal length of a phone number (could just be a string though)
				
			cleanMessage = cleanMessage[endNumber+12:] #12 is how many characters till the text begins
		else:
			#print "no number available"
			number = '0'

		endBody = cleanMessage.find('<br/><br/>')
		body = cleanMessage[:endBody]
		body = remove_emoji(body)

		


		cleanMessage = cleanMessage[endBody:]

		endWhenReceived = len(cleanMessage)-130
		whenReceived = cleanMessage[31:endWhenReceived]

		#print number
		#print body
		#print whenReceived


		#add one "line" to a text file representing a single text message with splitters between the number, body, and recieved time; and between each different text
		#splitter = "!#^&@#$%(&^%$&*)(*&$#$%^"
		#newMessageSplitter = "#@$@$YTRFU^G*VT(&DUGUF^RCUY "
		splitter = "&HJ BY&TGU(I&^"
		newMessageSplitter = "DUGUF^RCUY "
                file = open(path+"texts.txt","a")
		

		file.write(number+splitter+body+splitter+whenReceived+newMessageSplitter)
		file.close


		imapObj.delete_messages(messageID)
		

	#else:
		#print "no messages"


	imapObj.logout()

	
def deleteAlreadyRead():
	imaplib._MAXLINE = 10000000 #increases the byte limit of how much python can remember
	#create an IMAPClient object (ssl allows encryption which some email providers require)
	imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True) #client is the object that connects to the server
	imapObj.login('monikatextalerts@gmail.com', 'mwzifhbskvmyngae' ) #getpass.getpass('Email Password:') asks for the user to input a password



	imapObj.select_folder('INBOX', readonly=False) #turn this off to allow Monika to delete emails

	UIDs = imapObj.search(['SEEN']) #returns the ID's of all already read emails

	imapObj.delete_messages(UIDs)

	imapObj.logout()


#removes emojis from strings (in the future maybe just find a way to let Monika display the emojis)
def remove_emoji(data):

    if not data:
        return data
    if not isinstance(data, basestring):
        return data
    try:
    # UCS-4
        patt = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
    # UCS-2
        patt = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return patt.sub('', data)


#print "test"
#getTexts()

#deleteAlreadyRead()




