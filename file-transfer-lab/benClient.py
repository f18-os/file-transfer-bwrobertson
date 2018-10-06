import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
print("Please enter the file you want to send")
picture = input()
outfile = open(picture,'rb')
print('Sending...')
upload = outfile.read(100)
while (upload):
    print('Sending...')
    s.send(upload)
    upload = outfile.read(100)
outfile.close()
print("Done Sending")
#print(s.recv(1024))
s.close          