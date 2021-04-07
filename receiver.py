import socket

localIP = socket.gethostbyname(socket.gethostname())
bufferSize  = 1024


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, 0))
print("Connect to {}".format(UDPServerSocket.getsockname()))
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    (message, address) = UDPServerSocket.recvfrom(bufferSize)

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)