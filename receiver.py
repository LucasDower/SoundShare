import socket

localIP = socket.gethostbyname(socket.gethostname())
localPort   = 20001
bufferSize  = 1024
print("Connect to {}:{}".format(localIP, localPort))

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    (message, address) = UDPServerSocket.recvfrom(bufferSize)

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)