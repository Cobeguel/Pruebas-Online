# Minimal Intercom

import argparse
import logging
import socket


try:
    import sounddevice as sd
except ModuleNotFoundError:
    import os
    os.system("pip3 install sounddevice --user")
    import sounddevice as sd

try:
    import numpy as np
except ModuleNotFoundError:
    print("Installing numpy with pip")
    import os
    os.system("pip3 install numpy --user")
    import numpy as np

try:
    import psutil
except ModuleNotFoundError:
    import os
    os.system("pip3 install psutil --user")
    import psutil




class MinimalIntercom

	CHANNELS = 1
	
	SAMPLE_RATE = 44100
	
	CHUNK_SIZE = 512 
	
	SOURCE_PORT = 7676
	
	DESTINATION_PORT = 7676
	
	DESTINATION_IP = "127.0.0.1"

	# Expected TCP connection for synchronize variables, however
	# at this moment, variables would be passed in constructor
	
			
	
	def __init__(self, args)
		#self.channels = argument["key"]  if "channels" in arguments else self.channels = CHANNELS
		self.channels = args.number_of_channels
    self.samplerate = args.frames_per_second
    self.chunk_size = args.frames_per_chunk
    self.source_port = args.source_port
    self.destination_IP = args.destination_IP 
    self.destination_port = args.destination_port
		
		#Socket deffinition
		
		self.sender_socket = socket

parser = argparse.ArgumentParser(description="Minimal intercom")

#parser.add_argument('-i', '--input-device', type=int_or_str,
#                    help='input device ID or substring')
#parser.add_argument('-o', '--output-device', type=int_or_str,
#                    help='output device ID or substring')
parser.add_argument('-c', '--channels', type=int, default=2,
                    help='number of channels')
#parser.add_argument('-t', '--dtype', help='audio data type')
parser.add_argument('-s', '--samplerate', type=int, default=44100, help='sampling rate')
parser.add_argument('-b', '--blocksize', type=int, default=256, help='block size')
#parser.add_argument('-l', '--latency', type=float, help='latency in seconds')
args = parser.parse_args()
    
#Global variable declaration


# Minimal sounddevice. Just take the general parameters needed to implement
# communication. 

class MinimalSounddevice:

	def __init__(self, channels=2, samplerate=44100, blocksize=256)
		self.channels=channels
		self.samplerate=samplerate
		self.blocksize=blocksize

class SounddeviceFactory(object)
		
	
class CallBackSounddevice(MinimalSounddevice):
	def __init__(self, channels=2, samplerate=44100, blocksize=256):
		super().__self__(channels, samplerate, blocksize)
		
	
	


    
class MinimalIntercom:

	def __init__(self, dest_IP, dest_Port):
	#Definimos un socket de familia direccion puerto (AF_INET)
	# y de tipo UDP (SCK_DGRAM)
		self.UDPsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		self.stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
		self.stream.start()
		
	# Ligamos el socket 
		self.UDPsocket.bind((dest_IP, dest_Port))
	
	
	
	def send(self):
		chunk, overflowed = self.stream.read(1024)
		self.UDPsocket.sendto(chunk, ("127.0.0.1", 7777))
		
	def receive(self):
		chunk,server=self.UDPsocket.recvfrom(7777);
		self.stream.write(chunk)
		
		
intercom = MinimalIntercom("127.0.0.1",7777);

while True:
	intercom.send()
	intercom.receive()

#intercom.send(b"Wepale");
#intercom.receive()

    
