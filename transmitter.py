import socket
import pyaudio
import sys
import constants
import re

audio = pyaudio.PyAudio()

# Listen devices
for i in range(0, audio.get_device_count()):
    print(i, audio.get_device_info_by_index(i)['name'])
device_index = int(input('Device index: '))

# Configure socket
local_ip = input("IP: ")
if not constants.IP_REGEX.match(local_ip):
    sys.exit("Invalid IP")

try:
    local_port = int(input("Port: "))
    assert(1025 <= local_port <= 65535)
except:
    sys.exit("Invalid port number")

address = (local_ip, local_port)
udp_socket = socket.socket(family=address.AF_INET, type=address.SOCK_DGRAM)

# Send to server using created UDP socket
stream = audio.open(format=pyaudio.paInt16, channels=constants.NUM_CHANNELS,
                rate=constants.SAMPLE_RATE, input=True, input_device_index=device_index,
                frames_per_buffer=constants.CHUNK_SIZE)

print("Sending...")
while True:
    data = stream.read(CHUNK, False)
    udp_socket.sendto(data, address)
