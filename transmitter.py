import socket
import pyaudio
import sys
import constants

audio = pyaudio.PyAudio()

# Listen devices
for i in range(0, audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    print(i, device_info['name'], device_info['maxInputChannels'], device_info['maxOutputChannels'])
device_index = int(input('Device index: '))

# Configure socket
local_ip = input("IP: ")
local_port = int(input("Port: "))

address = (local_ip, local_port)
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

selected_device_info = audio.get_device_info_by_index(device_index)
num_channels = selected_device_info['maxOutputChannels']
print("Number of channels", num_channels)

# Send to server using created UDP socket
stream = audio.open(format=pyaudio.paInt16, channels=num_channels,
                rate=constants.SAMPLE_RATE, input=True, input_device_index=device_index,
                frames_per_buffer=constants.CHUNK_SIZE)

print("Sending...")
while True:
    try:
        data = stream.read(constants.CHUNK_SIZE)
        udp_socket.sendto(data, address)
    except:
        pass