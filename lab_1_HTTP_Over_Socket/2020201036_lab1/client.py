import socket
import os

request = input()

# GET site1/file1.txt

msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    msock.connect(("127.0.0.1",8080))
except socket.error as e:
    print(str(e))

# msock.connect(("127.0.0.1",8080))


while True:
	msock.sendall(bytes(request, encoding='utf8'))
	data = msock.recv(1024)
	if(len(data) < 1):
		break
	response = data
	while True:
		data = msock.recv(1024)
		if(len(data)<1):
			break
		response = response + data

	# print(response)
	response = response
	fnew = open((request.split(' '))[1].split('/')[1], "wb")
	# fnew = open(sample.txt,"w")
	fnew.write(response)
	fnew.close()

# msock.close()