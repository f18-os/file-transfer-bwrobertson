#! /usr/bin/env python3

# Echo server program

import socket, sys, re
sys.path.append("../lib")       # for params
import params

thisDelimiter = '<(*.*<)'
switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

conn, addr = s.accept()  # wait until incoming connection request (and accept it)
print('Connected by', addr)
data = ""
message = ""
myFile = ""
writeFile = ""
while 1:
    while(thisDelimiter not in data):
        data += conn.recv(100).decode()
    if len(data) == 0:
        print("Zero length read, nothing to send, terminating")
        break
    message = data.replace(thisDelimiter, "")
    sendMsg = "Echoing %s" % data
    print("Received '%s', sending '%s'" % (message, sendMsg))
    print("A file has been received. What would you like to save it as?")
    myFile = input()
    writeFile = open(myFile, 'w+')
    writeFile.write(message + '\n')
    writeFile.close()
    while len(sendMsg):
        bytesSent = conn.send(sendMsg.encode())
        sendMsg = sendMsg[bytesSent:0]
    data = ""
conn.shutdown(socket.SHUT_WR)
conn.close()

