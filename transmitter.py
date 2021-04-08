import socket
import pyaudio
import sys

CHUNK = 200
audio = pyaudio.PyAudio()

# Listen devices
for i in range(0, audio.get_device_count()):
    print(i, audio.get_device_info_by_index(i)['name'])
device_index = int(input('Device index: '))

# Configure socket
localIP     = input("IP: ")
localPort   = int(input("Port: "))
bufferSize  = 1024

serverAddressPort = (localIP, localPort)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
stream = audio.open(format=pyaudio.paInt16, channels=2,
                rate=44100, input=True, input_device_index=device_index,
                frames_per_buffer=CHUNK)

print("Sending...")
while True:
    data = stream.read(CHUNK)
    UDPClientSocket.sendto(data, serverAddressPort)