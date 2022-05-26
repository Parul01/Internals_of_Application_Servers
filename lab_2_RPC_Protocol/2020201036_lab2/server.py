import socket
import threading
import sys
import inspect

HOST = '127.0.0.1'
PORT = 8080


textFile = "proc.txt"

class Compute(object):
	# __init__ works like a constructor
	# def __init__(self):

	def display(self,name):
		return ("the name received is "+name)

	def sum(self,a,b):
		return (int(a) + int(b))

	def multiply(self,n1,n2,n3):
		mul = int(n1)*int(n2)*int(n3)
		# print(mul)
		return mul
		

writeToText = ""
procList = [method for method in dir(Compute) if method.startswith('_') is False]

ob = Compute()

for x in procList:
	writeToText += x
	name = "ob."+x
	l = inspect.getfullargspec(eval(name)).args
	for i in l:
		if i != 'self':
			writeToText += " "+i
	writeToText +="\n"


w = open(textFile,"w+")
w.write(writeToText)
w.close()




def process(conn,addr):

	with conn:
		print('Processing: ',addr)
		while True:
			obj = Compute()
			outputMsg = ""

			data = conn.recv(4096).decode()

			if(len(data) < 1):
				continue


			tokens = data.split(" ")
			try:
				m = getattr(obj,tokens[0])
			except:
				conn.sendall(b"No such function defined at server side")
				sys.exit()
		

			outputMsg = m(*tokens[1:])

			if(type(outputMsg) == int):
				outputMsg = str(outputMsg)


			# if not data:
			# 	print('Nothing received')
			# 	return

			# elif "display" in data:
			# 	tokens = data.split()
			# 	outputMsg = obj.display(tokens[1])


			# elif "sum" in data:
			# 	tokens = data.split()
			# 	outputMsg = obj.sum(int(tokens[1]),int(tokens[2]))
			# 	outputMsg = str(outputMsg)



			

			conn.sendall(outputMsg.encode())
		# conn.close()


msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msock.bind((HOST,PORT))
msock.listen()

while True:
	conn,addr = msock.accept()
	tm = threading.Thread(target=process,args=(conn,addr,))
	tm.start()