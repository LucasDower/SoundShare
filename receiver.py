import socket
import pyaudio
import constants
import sys

host_info = socket.gethostbyname_ex(socket.gethostname())
local_ip = host_info[2][1]
#local_ip = socket.gethostbyname(socket.gethostname())

# Create a datagram socket
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# Bind to address and generate free port
try:
    udp_socket.bind((local_ip, 0))
except Exception as e:
    sys.exit("Could not bind to a socket\n")

address = str(udp_socket.getsockname()[0]) + ':' + str(udp_socket.getsockname()[1])

print("UDP server up and listening...")
print("Connect to", address)

num_channels = int(input("Number of channels: "))

audio = pyaudio.PyAudio()
stream = audio.open(rate=constants.SAMPLE_RATE, channels=num_channels, format=pyaudio.paInt16, output=True)

# Listen for incoming datagrams
while True:
    (frames, address) = udp_socket.recvfrom(constants.BUFFER_SIZE)
    print(len(frames), "bytes received")
    stream.write(frames)