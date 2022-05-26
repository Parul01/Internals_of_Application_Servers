import socket
import os
import mimetypes
import threading

def getHeaders(responseStatus,fileName):

    header = ''
    if responseStatus == 200:
        header += 'HTTP/1.1 200 OK\n'
    elif responseStatus == 404:
        header += 'HTTP/1.1 404 Not Found\n'

    fileType = mimetypes.guess_type(fileName) 

    header += 'mimetype: application/force-download\n'
    header += 'Content-Disposition: attachment; filename='+fileName+'\n'
    # header += 'Content-Type: application/pdf;\n'
    # header += 'Content-Type: video/mp4;\n'
    header += 'Content-Type: '+fileType[0]+';\n'
    header += 'Access-Control-Allow-Credentials:GET\n'

    header += 'Connection: Keep-Alive\n'
    header += 'Server: Local-Host-Server\n\n'
    # header += 'Connection: close\n\n'
    return header

def process(conn,addr):
	try:

		with conn:
			print('Connected by',addr)
			data = conn.recv(10000)
			if not data:
				print('Nothing recieved')
				return
			
			data = data.decode()
	
			data = data.split('\n')

			data = ((data[0]).split(' '))[1]
			# print(data)

			data = data[1:]
		
			filename = data.split('/')[1]
			filetype = filename.split('.')[1]
			# print(filename + " ---- " + filetype)


			with open(data,'rb') as recvFile:
				res = recvFile.read()


			response = getHeaders(200,filename)
			response = bytearray(response,encoding="utf8")+ res

			# response += res
			# # conn.sendall(bytes(str(buffer[0]), encoding='utf8'))
			conn.sendall(response)
		
			conn.close()
	finally:
		conn.close()




HOST = '127.0.0.1'
PORT = 8081

msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msock.bind((HOST,PORT))
msock.listen()

try:

	while True:
		conn,addr = msock.accept()
		threading.Thread(target=process,args=(conn,addr,)).start()

		
		# msock.close()
finally:
	msock.close()