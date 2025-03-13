import ipaddress
import socket 

#creates a socket
myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connects the socket to a specific port on the computer
myTCPSocket.bind(('localhost', 1024))

#waits for a connection to be initiated 
myTCPSocket.listen(5)

#when it gets a connection it accepts it 
incomingSocket, incomingAddress = myTCPSocket.accept()

#continuously waiting for a message
while True:

    #gets the message, have to use decode to get rid of the 'b'
    myData = str(incomingSocket.recv(20).decode())
    print("UNCHANGED: ", myData)

    #changes the message to all capital letters
    myData = myData.upper()
    print("ALTERED: ", myData)

    #sends the message to the connected socket
    incomingSocket.send(bytearray(str(myData), encoding='utf-8'))


