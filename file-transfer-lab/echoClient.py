#! /usr/bin/env python3

# Echo client program
import socket, sys, re
sys.path.append("../lib")       # for params
import params
thisDelimiter = '<(*.*<)'
switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

print("Please enter the name of the file you want to read from.")
thisFile = input()
myFile = open(thisFile, "r")
outMessage = myFile.read()

origMessage = outMessage
outMessage += thisDelimiter
while len(outMessage):
    #print("sending '%s'" % origMessage)
    print("File sent!")
    bytesSent = s.send(outMessage.encode())
    outMessage = outMessage[bytesSent:]

data = ""
while(thisDelimiter not in data):
    data += s.recv(100).decode()
data = data.replace(thisDelimiter, "")
#print("Received '%s'" % data)
print("File received successfully!")


"""
outMessage = "Hello client!"
origMessage = outMessage
outMessage += thisDelimiter
while len(outMessage):
    print("sending '%s'" % origMessage)
    bytesSent = s.send(outMessage.encode())
    outMessage = outMessage[bytesSent:]

s.shutdown(socket.SHUT_WR)      # no more output

data = ""
while 1:
    while(thisDelimiter not in data):
        data += s.recv(1024).decode()
    data = data.replace(thisDelimiter, "")
    print("Received '%s'" % data)
    break
"""
print("Zero length read.  Closing")
s.close()

