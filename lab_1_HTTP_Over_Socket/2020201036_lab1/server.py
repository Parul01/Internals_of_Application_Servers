import socket
import os
import threading

HOST = '127.0.0.1'
PORT = 8080

def process(conn,addr):

	with conn:
		print('Connection: ',addr)
		data = conn.recv(4096).decode('utf-8')

		if not data:
			print('Nothing received')
			return
		
		# data = data.decode().split(' ')
		data = data.split(' ')
		if(data[0] != 'GET'):

			conn.sendall(b'HTTP/1.1 404 Not Found')
			return

		
		with open(data[1],'rb') as recvFile:
			res = recvFile.read()
			# print(res)

		conn.sendall(res)
	# conn.close()


msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msock.bind((HOST,PORT))
msock.listen()

while True:
	conn,addr = msock.accept()
	threading.Thread(target=process,args=(conn,addr,)).start()