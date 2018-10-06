import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
print("Please enter the file you want to send") 
picture = input() #designates the file you want to send
outfile = open(picture,'rb')
print('Uploading file...')
upload = outfile.read(100) #sends the file 100 bytes at a time
while (upload):
    print('Uploading file...') #Lets the user know that the process is...processing
    s.send(upload)
    upload = outfile.read(100)
outfile.close()
print("Upload complete!")
s.close          
