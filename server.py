from network import Listener, Handler, poll

 
handlers = {}  # map client handler to user name
 
class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        print msg
 
 
port = 8888
server = Listener(port, MyHandler)
while 1:
    poll(timeout=0.05) # in seconds

# print('Welcome to chat!');
# message = None;

# while (message != ':q'):
# 	message = message.rstrip();
# 	message = raw_input('Admin: ');

# server.stop();
