import socket
import pyaudio

localIP = socket.gethostbyname(socket.gethostname())
bufferSize  = 1024


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, 0))
print("Connect to {}".format(UDPServerSocket.getsockname()))
print("UDP server up and listening")

audio = pyaudio.PyAudio()
stream = audio.open(rate=44100, channels=2, format=pyaudio.paInt16, output=True)

# Listen for incoming datagrams
while(True):
    (frames, address) = UDPServerSocket.recvfrom(bufferSize)

    stream.write(frames)

    #clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    #print(clientMsg)
    print(clientIP)