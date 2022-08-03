import zmq, time, pickle, sys, socket

'''primary socket API functions and methods:
socket()
.bind()
.listen()
.accept()
.connect()
.connect_ex()
.send()
.recv()
.close()
'''
# the nodes are our network and must act as both the client and server
# sockets are used for sending msgs across a network
# we want our 4 nodes to be able to send files back and forth
# how do we keep track of this? >> here we could use the hashtable
# docker network makes a simulated tcp brdige


#1 find the nodes >> look for the ip addresses and local host >> each ip address will scan and match a number of ports >> if it has an open port
#  and a valid ip address then we can proceed cuz its a node >> what is youre the first node on a network
#randomly assign a ip address and a socket and then bind it
#2 then set up the sockets so they can communicate >> and send files back and forth
#3 keep track using hash table >> deal w dif contents and timestamps
#4

''' * How will your nodes discover other clients on the network? Remember, just because it's Docker doesn't mean we don't have to implement the
 LAN networking too.
  * How will your client deal with files of the same name but different contents? Different timestamps?
  * How will your client determine the order of syncing with regards to the files of other clients? (Docker might help here).'''

# create a socket object
s = socket.socket()        
print ("Socket creation successful. ")
 
port = 12345               
 
#bind to the port and the empty ip field slot allows the server to listen to reqs from other computers on the network
s.bind(('', port))        
print ("Socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(2)    # num signifies how many connections will be waiting while the server is busy
print ("Socket is listening")           
 

# a forever loop until we interrupt it or
# an error occurs
while True:
# Establish connection with client.
  c, addr = s.accept()    
  print ('Recieved connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type.
  c.send('Thank you for connecting'.encode())
  # Close the connection with the client >> this would be after were done exchanging the files
  c.close()
   
  # Breaking once connection closed
  break

'''localHost = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 1234  # Port to listen on (non-privileged ports are > 1023)
creating socket object and then setting up a listening socket for the SERVER side'''

'''
socket.socket() 
socket.client()
specifying socket type Note: this protocol default is TCP'''
socket.SOCK_STREAM
socket.AF_INET()
'''associates socket w a specific network interface and port num'''
    socket.bind((localHost, port))
    '''listening for connections from CLIENTS'''
    socket.listen()
    ''' here it accepts the connection'''
    conn, addr = socket.accept()

 with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


#to search for unknown nodes >> one way would be to loop thoruhg eah addresses to find active machines







