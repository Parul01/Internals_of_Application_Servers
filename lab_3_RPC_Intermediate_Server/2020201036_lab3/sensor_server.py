import socket
import os

import random
import sys

import threading

serv_ip = '127.0.0.1'
serv_port = 8082

data_sensor1 = ""
data_sensor2 = ""

list_ip = '127.2.2.2'
list_port = 8086

def polling_thread():
    global data_sensor1, data_sensor2
    while True:
        try:

            msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            msock.connect((serv_ip, serv_port))
            msock.sendall(b'SENSOR')
            data = msock.recv(1024).decode('utf-8')

            # print(data)

            data = data.split(" ")
            if (data[0] == 'SUCCESS'):
                # proc_data = process_data(data)
                if data[1] == "S1":
                    proc_data = data_sensor1
                    data_sensor1 = ""

                else:
                    proc_data = data_sensor2
                    data_sensor2 = ""

                # print(proc_data)
                msock.sendall(proc_data.encode('utf-8'))

            msock.close()

        except:
            sys.exit("Unable to connect")

threading.Thread(target=polling_thread).start()


def process_data(conn,addr):
    global data_sensor1,data_sensor2
    # print("connection ")
    global data_sensor1,data_sensor2
    with conn:
        dd = conn.recv(2046).decode("utf-8")
        dd = dd.split(" ")
        if(dd[0] == "S1"):
            data_sensor1 += dd[1]
        else:
            data_sensor2 += dd[1]



#     logic to connect to sensor
    return "random text"

def list_process():
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((list_ip, int(list_port)))
    lsock.listen()

    while True:
        conn, addr = lsock.accept()
        tm = threading.Thread(target=process_data, args=(conn, addr,))
        tm.start()


threading.Thread(target=list_process).start()






