import csv
import PathInitializer



#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path



#return the name of the person if they are in the contacts list
#if not, return -1
#number should be a string
def findName(number):
	f = open(path+'Contacts.csv', 'r')
	contactList = csv.reader(f, delimiter=',')
	for row in contactList:
		print row
		if number == row[1]:
			print "is in file"
			return row[0]
	print "not in file"
	return "-1"

	'''with open('Contacts.csv', 'r') as f:
		contactList = csv.reader(f, delimiter=',')
		for row in contactList:
			#print row
			if number == row[1]:
				#print "is in file"
				return row[0]
		#print "not in file"
		return "-1"
	'''


#adds a new contact to the Contacts.csv file
#both paramaters should be strings
def addContact(name, number):
	with open(path+'Contacts.csv','a') as fd:
		fd.write("\n"+name+","+number)



#addContact("Nia", "12345678910")



#add a function to let people change their name