from vidshare import StreamingServer
import threading

server = StreamingServer("localhost", 5000) #set your ip and port on server

thread = threading.Thread(target = server.start_server) #thread to start server
thread.start() #start the thread

while True:
    input_ = input('Enter Quit To Exit : ')
    if input_ == 'quit' or input_ == 'exit':
        server.stop_server() #to stop the server
        break