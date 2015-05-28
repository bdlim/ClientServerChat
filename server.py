from network import Listener, Handler, poll
import Queue

# Current Customer and Agent
customerName = None
customerHandler = None
agentName = None
agentHandler = None

queue = Queue.Queue() # Queue of remaining Customers

class MyHandler(Handler):

    def on_open(self):
        pass

    def on_close(self):
        pass

    def on_msg(self, msg):
        global customerName
        global customerHandler
        global agentName
        global agentHandler

        if 'join' in msg:
            if msg['personnel'] == 'agent':
                agentName = msg['join']
                agentHandler = self
                print 'Agent ' + agentName + ' has connected successfully!'
                agentHandler.do_send('Connection Successful')
            elif msg['personnel'] == 'customer':
                if (customerName is None) and (customerHandler is None):
                    customerName = msg['join']
                    customerHandler = self
                    print 'Customer ' + customerName + ' has connected successfully!'
                    customerHandler.do_send('Welcome to the chat!')
                else:
                    queue.put({msg['join']: self})
                    print 'Customer ' + msg['join'] + ' is waiting in the queue.'
                    self.do_send('All available agents are busy. Please wait')
            else:
                print 'Error'
        elif 'txt' in msg:
            if msg['name'] == agentName:
                customerHandler.do_send(msg['txt'])
            elif msg['name'] == customerName:
                agentHandler.do_send(msg['txt'])
            else:
                self.do_send('All available agents are busy. Please wait')

port = 8888
server = Listener(port, MyHandler)
while 1:
    poll(timeout=0.05) # in seconds
