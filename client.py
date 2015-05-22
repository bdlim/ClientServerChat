# -*- coding: utf-8 -*-
from network import Listener, Handler, poll
import sys
from threading import Thread
from time import sleep

######## MODEL ########

class Client(Handler):
	
	def on_close(self):
		pass
	
	def on_msg(self, msg):
		print('agent: ' + msg);
		chat();
		
		
host, port = 'localhost', 8888
client = Client(host, port);

def periodic_poll():
	while 1:
		poll()
		sleep(0.05)  # seconds
							
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