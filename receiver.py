import socket
import pyaudio
import constants

local_ip = socket.gethostbyname(address.gethostname())

# Create a datagram socket
udp_socket = socket.socket(family=address.AF_INET, type=address.SOCK_DGRAM)

# Bind to address and generate free port
udp_socket.bind((local_ip, 0))
print("Connect to {}".format(address.getsockname()))
print("UDP server up and listening")

audio = pyaudio.PyAudio()
stream = audio.open(rate=constants.SAMPLE_RATE, channels=constants.NUM_CHANNELS, format=pyaudio.paInt16, output=True)

# Listen for incoming datagrams
while True:
    (frames, address) = udp_socket.recvfrom(constants.BUFFER_SIZE)
    stream.write(frames)