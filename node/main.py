
import sys, os, traceback, time
from threading import Thread
from socket import *
from tracemalloc import stop
from ping3 import ping


print ("starting...")
print(gethostbyname(gethostname()))

files = os.listdir("/files")
requestFiles = []
listIP = []
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
#listIP.append(gethostbyname(gethostname()))

def broadcastRequest():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(b"", ("255.255.255.255", 1234))
    s.close()

def broadcastListen():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("", 1234))
    while True:
        msg, senderIP = s.recvfrom(1234)
        newIP = str(senderIP[0])

        if newIP not in listIP and newIP != gethostbyname(gethostname()):
            listIP.append(newIP)

        #if stop():
        #    break

        msg = msg.decode("utf-8")
    s.close()
'''
        if msg == "List all files.":
            print("Sending list of files")
            for file in files:
                s.sendto(file.encode("utf-8"), (newIP, 1234))
        else:
            if msg not in files:
                requestFiles.append(msg)
'''

def sendFile():
    for node in listIP:
        s = socket(AF_INET, SOCK_STREAM)
        print("Connecting to " + node)
        s.connect((node, 1234))
        for file in files:
            print("Sending " + file)
            filesize = os.path.getsize("/files/" + file)
            s.send(f"{file}{SEPARATOR}{filesize}".encode("utf-8"))
            with open("/files/" + file, "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in 
                    # busy networks
                    s.sendall(bytes_read)
                    #time.sleep(1)
    s.close()

def recieveFile():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("", 1234))
    s.listen()
    clientSocket, clientIP = s.accept()
    received = clientSocket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filesize = int(filesize)
    if filename not in files:
        with open("/files/" + filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = clientSocket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)
        #requestFiles.remove(filename)
    time.sleep(1)
    s.close()

        

#stop = False

time.sleep(1)
Thread(target = broadcastListen).start()
time.sleep(1)
Thread(target = broadcastRequest).start()
#time.sleep(1)
#Thread(target = broadcastListen, args = (lambda: stop,)).start()
#stop = True
time.sleep(1)
Thread(target = recieveFile).start()
Thread(target = sendFile).start()



'''
if os.path.isfile("serverlist.txt"):
    os.remove("serverlist.txt")

ad = ''.join(str(address));
ad1 = ad.split()
ad2= ad1[0]
ad3=ad2[2:15]
print ad3
f = open('serverlist.txt', 'a')
f.write(ad3+'\n')
f.close()
'''