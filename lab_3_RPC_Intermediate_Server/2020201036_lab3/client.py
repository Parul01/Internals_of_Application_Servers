import stub
import sys

sensor_id = input()


try:
	print(stub.receive_data(sensor_id))

except:
	print("Incorrect function call")
	sys.exit()