#UDPClient.py

from socket import *
import time
# '127.0.0.1' is the loopback IP address, which always refers to the current machine.
# serverName = '127.0.0.1' # Local host
serverName = 'localhost' # Local host
serverPort = 12000

# AF_INET tells the socket to use IPv4.
# SOCK_DGRAM tells the socket to use the UDP protocol (as opposed to SOCK_STREAMfor TCP).
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  #Tells client to wait 1 second for reply, or assume packet was lost

# (1) Loop to send 10 ping messages to server
for i in range(1,11):
    start = time.time()
    message = 'Ping #' + str(i) + " " + time.ctime(start)
    try:
            clientSocket.sendto(message.encode(), (serverName, serverPort))     #send message to server
            print("Sent " + message)

            msg, serverAddress = clientSocket.recvfrom(2048)        #received from client
            print("Received " + msg.decode())                       # (2) print server response message
            end = time.time();

            RTT = end - start                                   # (3) Calculate Round-trip time (RTT)
            print("RTT: " + str(RTT) + " seconds\n")
    except timeout:
            print("Request timed out\n")                        # (4) Timed out 



clientSocket.close()
