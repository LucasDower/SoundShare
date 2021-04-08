import socket
import pyaudio
import constants
import sys

local_ip = socket.gethostbyname(socket.gethostname())

# Create a datagram socket
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and generate free port
try:
    udp_socket.bind((local_ip, 0))
except Exception as e:
    sys.exit("Could not bind to a socket\n")

print("Connect to {}".format(udp_socket.getsockname()))
print("UDP server up and listening")

audio = pyaudio.PyAudio()
stream = audio.open(rate=constants.SAMPLE_RATE, channels=constants.NUM_CHANNELS, format=pyaudio.paInt16, output=True)

# Listen for incoming datagrams
while True:
    (frames, address) = udp_socket.recvfrom(constants.BUFFER_SIZE)
    stream.write(frames)