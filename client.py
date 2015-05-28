# -*- coding: utf-8 -*-
from network import Handler, poll
import sys
from threading import Thread
from time import sleep
from view import display, printEasterEgg




########## MODEL ##########

running = True
myname = None
active = False




########## CONTROLLER ##########

class Client(Handler):

	def on_open(self):
		pass

	def on_close(self):
		global running
		running = False
		display("Goodbye! Press Enter to end program.")

	def on_msg(self, msg):
		global active
		if msg == 'Connecting Now!':
			active = True
		display(msg)


def chatSettings():
	global myname

	personnel = raw_input('Are you agent or customer? ')
	while (personnel != "agent") and (personnel != "customer"):
		personnel = raw_input('Invalid. Please select agent or customer: ')
	myname = raw_input('What is your name? ')
	while (myname == ""):
		myname = raw_input('Invalid. Please put a valid name: ')
	if (personnel == "customer"):
		display('1 - Complaint');
		display('2 - Question');
		display('3 - Other');
		myoption = raw_input('Please select an option: ');
		while (myoption != "1") and (myoption != "2") and (myoption != "3"):
			myoption = raw_input('Invalid. Please select an option: ')
		mytopic = raw_input('What is your topic? ')
		while (mytopic == ""):
			mytopic = raw_input('Invalid. Please put a valid topic: ')
		return {'join': myname, 'personnel': personnel, 'option': myoption, 'topic': mytopic}
	else:
		return {'join': myname, 'personnel': personnel}

host, port = 'localhost', 8888
client = Client(host, port);
client.do_send(chatSettings())

def periodic_poll():
	while 1:
		poll()
		sleep(0.05)  # seconds

thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies
thread.start()



while running:
	global mytxt

	mytxt = raw_input('')
	if (not active):
		client.do_send({'name': myname, 'txt': mytxt})
	else:
		if (mytxt == ":q"):
			client.do_send({'name': myname, 'special': 'q'})
			client.do_close()
		elif (mytxt == ":s"):
			client.do_send({'name': myname, 'special': 's'})
		elif (mytxt == ":e"):
			printEasterEgg()
		else:
			client.do_send({'name': myname, 'txt': mytxt})
