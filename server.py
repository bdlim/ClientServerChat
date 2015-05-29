from network import Listener, Handler, poll
import Queue
from view import display



########## MODEL ##########

# Current Customer and Agent
customerName = None
customerHandler = None
agentName = None
agentHandler = None

queue = Queue.Queue() # Queue of remaining Customers




########## CONTROLLER ##########

class MyHandler(Handler):

    def on_open(self):
<<<<<<< HEAD
		print('the server has been established')
		         
=======
        pass

>>>>>>> 47c7f104042109c52576cf6674f98303c043388e
    def on_close(self):
        pass

    def on_msg(self, msg):
<<<<<<< HEAD
		print('client: ' + msg);
		message = raw_input('agent: ');
		self.do_send(message);
		print('waiting for client response')
 
 
=======
        global customerName
        global customerHandler
        global agentName
        global agentHandler

        if 'join' in msg:
            if msg['personnel'] == 'agent':
                agentName = msg['join']
                agentHandler = self
                display('Agent ' + agentName + ' has connected successfully!')
                agentHandler.do_send('Welcome to the Chat System. Please wait to be connected')
                agentHandler.do_send('Connecting Now!')
            elif msg['personnel'] == 'customer':
                if (customerName is None) and (customerHandler is None):
                    customerName = msg['join']
                    customerHandler = self
                    display('Customer ' + customerName + ' has connected successfully!')
                    agentHandler.do_send('Customer ' + customerName + ' is being connected')
                    agentHandler.do_send(handleOption(msg['option']))
                    agentHandler.do_send('Topic is: ' + msg['topic'])
                    agentHandler.do_send('You are now connected to Customer ' + customerName)
                    customerHandler.do_send('Welcome to the Chat System. Please wait to be connected')
                    customerHandler.do_send('Connecting Now!')
                    customerHandler.do_send('You are now connected to Agent ' + agentName)
                else:
                    queue.put({'name': msg['join'], 'option': msg['option'], 'topic': msg['topic'], 'handler': self})
                    display('Customer ' + msg['join'] + ' is waiting in the queue.')
                    self.do_send('Welcome to the Chat System. Please wait to be connected')
                    self.do_send('All available agents are busy. Please wait')
            else:
                display('Error')
        elif 'txt' in msg:
            if msg['name'] == agentName:
                customerHandler.do_send(agentName + ": " + msg['txt'])
            elif msg['name'] == customerName:
                agentHandler.do_send(customerName + ": " + msg['txt'])
            else:
                self.do_send('All available agents are busy. Please wait')
        elif 'special' in msg:
            if msg['special'] == "q":
                display('Customer ' + customerName + ' has quit the chat')
                agentHandler.do_send('Customer ' + customerName + ' has quit the chat\n\n\n')
                if (not queue.empty()):
                    nextCustomer = queue.get()
                    customerName = nextCustomer['name']
                    customerHandler = nextCustomer['handler']
                    display('Customer ' + customerName + ' has connected successfully')
                    agentHandler.do_send('Customer ' + customerName + ' is being connected')
                    agentHandler.do_send(handleOption(nextCustomer['option']))
                    agentHandler.do_send('Topic is: ' + nextCustomer['topic'])
                    agentHandler.do_send('You are now connected to Customer ' + customerName)
                    customerHandler.do_send('Connecting Now!')
                    customerHandler.do_send('You are now connected to Agent ' + agentName)
                else:
                    customerName = None
                    customerHandler = None
                self.do_close()
            else:
                # SAVE CHAT
                pass

def handleOption(option):
    if (option == "1"):
        return "Option Selected: Complaint"
    elif (option == "2"):
        return "Option Selected: Question"
    else:
        return "Option Selected: Other"

>>>>>>> 47c7f104042109c52576cf6674f98303c043388e
port = 8888
server = Listener(port, MyHandler)
while 1:
    poll(timeout=0.05) # in seconds
