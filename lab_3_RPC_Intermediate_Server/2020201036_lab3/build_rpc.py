import socket

PORT = 8080
HOST = "127.0.0.1"

#  build rpc stub program


textFile = "proc.txt"

w = open("stub.py","w")
w.write("import socket\n")
w.write("import sys\n\n")



with open(textFile,"r") as txt:
	fileData = txt.readlines()
	for x in fileData:

		x = x.split(" ")
		print(x)

		
		fn = "def "+x[0]+"(*args):\n"
		w.write(fn)
		w.write("\tmsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\n")
		w.write("\ttry:\n")
		w.write("\t\tmsock.connect(('127.0.0.1',8082))\n")
		w.write("\texcept:\n")
		w.write("\t\tprint('could not connect')\n")
		w.write("\t\tsys.exit()\n\n")
		fn ="\tres = ''\n"
		fn +="\tfor x in args:\n"
		fn +="\t\tres +=' '+str(x)\n"
		fn += "\tmsg = res\n"
		fn += "\tmsg = '"+x[0]+"' + msg\n"
		fn += "\tmsg = msg.encode()\n"
		# w.write("def "+l[0]+"(*args):\n")
		w.write(fn)
		w.write("\tmsock.send(msg)\n")
		w.write("\trecvData = msock.recv(2046).decode()\n")
		w.write("\tmsock.close()\n")
		w.write("\treturn recvData")
		w.write("\n\n")
		


w.close()
