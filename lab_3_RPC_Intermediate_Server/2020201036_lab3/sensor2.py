import threading
import string
import random
import socket

sen_serv_ip = '127.2.2.2'
sen_serv_port = 8086

sensor_data1 = ""
current_length = 0
last_length = 0
N = 11
class Generate(threading.Thread):
    def __init__(self,callback,event,intr):

        self.callback = callback
        self.event = event
        self.interval = intr
        super(Generate,self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()



event = threading.Event()

def append_data():

    global N, sensor_data1
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    sensor_data1 += res
    # print(res)
    #append to global variable here
    msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    msock.connect((sen_serv_ip, sen_serv_port))
    data_to_send = "S2 " + res
    msock.sendall(data_to_send.encode("utf-8"))
    last_length = len(sensor_data1)

random_thread = Generate(append_data,event,4)
random_thread.start()

# while sensor_data1:
#     if last_length != len(sensor_data1):
#         msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         msock.connect((sen_serv_ip, sen_serv_port))
#         data_to_send = "S1 " + sensor_data1[last_length:]
#         msock.sendall(data_to_send.encode("utf-8"))
#         last_length = len(sensor_data1)
#         # send data to sensor_server
#
