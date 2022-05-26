import stub
import sys

a = input()
b = input()
c = input()


try:
	print(stub.multiply(a,b,c))
	print(stub.sum(b,c))
	print(stub.display("Parul"))
except:
	print("Incorrect function call")
	sys.exit()