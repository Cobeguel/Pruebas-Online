from _thread import *
import socket,time,json


class TCPexchange

	def __init__(dest_IP, dest_port)
		self.dest_IP=dest_IP
		self.dest.port=dest_port
		self.exchange={}
		self.sender_socket=(socket.AF_INET, socket.SOCK_STREAM)
		self.receiver_socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def startConection(self):
		self.sender_socket.connect((self.dest_IP, self.dest_port))

	def checkConnection(self):
		return self.sender_socket


	def startListening(self):
		# self.listening_endpoint = ("0.0.0.0", self.my_port)
		# self.receiving_sock.bind(self.listening_endpoint)
		self.receiver_socket.connect(("0.0.0.0",self.dest_port)) #FIXME PORT

	def sendInfo(socket, to_send):
		checker=""
		#while(checker != "Ok"):
			socket.send(to_send)
			sleep(20)
			data,server=socket.recv(1024)
			print("Recibido tras enviar: ",data)
			


def receiveInfo(socket,to_receive):
	to_receive={}
	#while(to_receive)
	data,server=socket.recv(1024)
	print()

#Data

channels=2
samplerate=44100
blocksize=256

source_IP = "192.168.1.51"
destiny_IP = "192.168.1.51"

source_port = 7676
destiny_port = 7676

to_send	=	{	"channels" : channels,
						"samplerate" : samplerate,
						"blocksize" : blocksize}
to_receive="";

to_send = json.dumps(to_send)

TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_socket.connect((destiny_IP, destiny_port))



