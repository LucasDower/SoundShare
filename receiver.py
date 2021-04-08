import socket
import pyaudio

localIP = socket.gethostbyname(socket.gethostname())
bufferSize  = 1024

# Create a datagram socket
socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and generate free port
socket.bind((localIP, 0))
print("Connect to {}".format(socket.getsockname()))
print("UDP server up and listening")

audio = pyaudio.PyAudio()
stream = audio.open(rate=44100, channels=2, format=pyaudio.paInt16, output=True)

# Listen for incoming datagrams
while True:
    (frames, address) = socket.recvfrom(bufferSize)
    stream.write(frames)