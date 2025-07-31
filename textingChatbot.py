# Take in variables like newConversation, how much Monika likes that person, and weather or not I'm sleeping/busy
# 
# 

import aiml
import sys
import time


def thinkUpResponse():
	if(len(sys.argv)==2): #ensure it got an input message

		inputMessage = sys.argv[1]

		# Create the kernel and learn AIML files
		kernel = aiml.Kernel()
		kernel.learn("init.xml")
		kernel.respond("load aiml b")

		#print inputMessage

		response = kernel.respond(inputMessage)
		time.sleep(5)


		print response

			# Press CTRL-C to break this loop
		'''while True:
			print kernel.respond(raw_input("Enter your message >>"))
		'''

	else:
		print "Please send a valid text."



thinkUpResponse()