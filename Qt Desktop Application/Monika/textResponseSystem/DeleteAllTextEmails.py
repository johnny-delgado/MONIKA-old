import imapclient
import imaplib
#import pyzmail
#import re

def deleteAll():
	print "Deleting..."




	imaplib._MAXLINE = 10000000 #increases the byte limit of how much python can remember
	#create an IMAPClient object (ssl allows encryption which some email providers require)
	imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True) #client is the object that connects to the server
	imapObj.login('monikatextalerts@gmail.com', 'mwzifhbskvmyngae' ) #getpass.getpass('Email Password:') asks for the user to input a password



	imapObj.select_folder('INBOX', readonly=False) #turn this off to allow Monika to delete emails

	UIDs = imapObj.search(['ALL']) #returns the ID's of all already read emails

	imapObj.delete_messages(UIDs)

	imapObj.logout()




	print "Deleted."
