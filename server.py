import ipaddress
import socket 

myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myTCPSocket.bind(('localhost', 1024))
myTCPSocket.listen(5)
incomingSocket, incomingAddress = myTCPSocket.accept()

while True:
    myData = str(incomingSocket.recv(20))
    print("UNCHANGED: ", myData)
    myData = myData.upper()
    print("ALTERED: ", myData)
    incomingSocket.send(bytearray(str(myData), encoding='utf-8'))


