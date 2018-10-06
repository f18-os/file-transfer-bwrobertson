import socket, os               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
picture = ""
while True:
    client, addr = s.accept()     # Establish connection with client.
    cpid = os.fork()                #this is to identify the child's pid, 
    if(cpid==0):                    #this also allows you to receive multiple files on the server without have to reopen it
        print("Enter name for new file")
        picture = input()           #designate what you want to save the incoming file as
        infile = open(picture,'wb')
        print('Got connection from', addr)
        print("Incoming file...")
        download = client.recv(100)
        while (download):
            print("File downloading")
            infile.write(download)
            download = client.recv(100)
        infile.close()
        print("File received successfully!")
        client.close()    
