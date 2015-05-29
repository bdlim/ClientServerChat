# -*- coding: utf-8 -*-
from network import Listener, Handler, poll
import sys
from threading import Thread
from time import sleep
from view import display, printEasterEgg




########## MODEL ##########

running = True
myname = None
mytxt = None
active = False
chat = "####### CHAT LOG ######\n"



########## CONTROLLER ##########

class Client(Handler):

	def on_open(self):
		pass

	def on_close(self):
		global running
		global chat
		running = False
		display("Goodbye! Press Enter to end program.")

	def on_msg(self, msg):
<<<<<<< HEAD
		print('agent: ' + msg);
		chat();
		
		
host, port = 'localhost', 8888
=======
		global active
		global chat

		if msg == 'Connecting Now!':
			active = True
		display(msg)
		chat += (msg + "\n")


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

host, port = '192.168.2.106', 8888
>>>>>>> 47c7f104042109c52576cf6674f98303c043388e
client = Client(host, port);
client.do_send(chatSettings())

def periodic_poll():
	while 1:
		poll()
		sleep(0.05)  # seconds
<<<<<<< HEAD
							
#thread = Thread(target=periodic_poll)
#thread.daemon = True  # die when the main thread dies 
#thread.start()

######## VIEW ########

def saveCopyOfChat():
	print('Saved a copy of the chat');

def printEasterEgg():
	print('');
	print('Easter egg!');
	print('How we felt while making this project');
	print('');
	print('(╯°□°）╯︵ ┻━┻');
	print('');
	print('How we felt finishing this project');
	print('');
	print('┏━┓ ︵ /(^.^/)');
	print('');

######## CONTROLLER ########

name = None;
option = None;
topic = None;

def chat():
	message = raw_input(name + ': ');
	client.do_send(message);
	print('waiting for agent response');
	periodic_poll();

print('Welcome to chat!');
message = raw_input('Please enter your name: ');

while (message != ':q'):
	message = message.rstrip();
	if (message == ':s'):
		saveCopyOfChat();
		if (name is None):
			message = raw_input('Please enter your name: ');
		elif (option is None):
			print('1 - Complaint');
			print('2 - Question');
			print('3 - Other');
			message = raw_input('Please select an option: ');
		elif (topic is None):
			message = raw_input('Please enter the topic: ');
		else:
			message = raw_input(name + ': ');
	elif (message == ':e'):
		printEasterEgg();
		if (name is None):
			message = raw_input('Please enter your name: ');
		elif (option is None):
			print('1 - Complaint');
			print('2 - Question');
			print('3 - Other');
			message = raw_input('Please select an option: ');
		elif (topic is None):
			message = raw_input('Please enter the topic: ');
		else:
			message = raw_input(name + ': ');
	else:
		if (name is None):
			name = message;
			client.do_send(name + ' has joined the chat');
			print('Hello ' + name + '!');
			print('1 - Complaint');
			print('2 - Question');
			print('3 - Other');
			message = raw_input('Please select an option: ');
		elif (option is None):
			if ((message == '1') or (message == '2') or (message == '3')):
				option = message;
				client.do_send(name + ' has selected option: ' + option);
				print('You have selected option: ' + option);
				message = raw_input('Please enter the topic: ');
			else:
				print('You have selected an invalid option: ' + message);
				message = raw_input('Please try again: ');
		elif (topic is None):
			topic = message;
			client.do_send(name + ' says the topic of the conversation is: ' + topic);
			print('You have stated that the topic is: ' + topic);
			print('You may start your conversation!');
#			message = raw_input(name + ': ');
			chat();
		else:
#			client.do_send(name + ': ' + message);
#			message = raw_input(name + ': ');
			chat();

client.do_send(name + ' has left the chat');
sys.exit("Quitted chat");
=======

thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies
thread.start()



while running:

	mytxt = raw_input('')
	if (not active):
		client.do_send({'name': myname, 'txt': mytxt})
	else:
		if (mytxt == ":q"):
			client.do_send({'name': myname, 'special': 'q'})
			client.do_close()
		elif (mytxt == ":s"):
			client.do_send({'name': myname, 'special': 's'})
			f = open('log.txt', 'w')
			f.write(chat)
			display("Chat Logged Successfully")
		elif (mytxt == ":e"):
			printEasterEgg()
		else:
			client.do_send({'name': myname, 'txt': mytxt})
			chat += (myname + ": " + mytxt + "\n")
>>>>>>> 47c7f104042109c52576cf6674f98303c043388e
