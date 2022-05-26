import socket
import threading
import sys

flag = False
HOST = '127.0.0.1'
PORT = 8082

current_sensor = ""
sensorIdDictionary = {}
sensorDataToClient = {}

textFile = "proc.txt"
#  server can provide sensor id in a sub

w = open(textFile,"w+")
w.write("receive_data sensor_id")
w.close()

def process(conn, addr):
    global flag
    global current_sensor
    with conn:
        # print('Connection: ',addr)

        data = conn.recv(2046).decode()
        data = data.split(" ")
        # print(data)
        if data[0] == "SENSOR":

            # CHECK IF ANY CLIENT IS REQUESTING DATA from sensors (check on behalf of every server

            """
                response = {status: "SUCCESS/FAILURE",
                            sensor_count: 1/2,
                            sensor_ids: "id1 id2",
                            data1: "data"
                            data2: "data"
                            }

            """

            if len(current_sensor) > 0:

                # meaning there is a client requesting data from sensor
                bfr = "SUCCESS "
                bfr += current_sensor
                conn.sendall(bfr.encode('utf-8'))

                data_to_client = ""
                recv_from_sensor = conn.recv(4096).decode("utf-8")
                data_to_client = recv_from_sensor
                while True:
                    recv_from_sensor = conn.recv(4096)
                    if len(recv_from_sensor) < 1:
                        break

                    data_to_client += recv_from_sensor.decode("utf-8")
                # print(" --- ")
                # print(data_to_client)

                if not flag:
                    return
                sensorDataToClient[current_sensor] = data_to_client
                # current_sensor = ""
                flag = False
            else:
                # no request from client yet send failure
                failure_msg = "FAILURE"
                conn.sendall(failure_msg.encode('utf-8'))

        else:

            # expects an identifier for sensor
            if data[0] == "receive_data":

                # print("data")
                # print(data)
                current_sensor = data[1]
                flag = True
                # print("current_sensor")
                # print(current_sensor)
                while current_sensor not in sensorDataToClient:
                    continue
                # out of loop -- means sensor has already uploaded data with intermediate server -- stored in
                # print(" ***** ")
                # print(sensorDataToClient)
                bfr = sensorDataToClient[current_sensor]
                sensorDataToClient.pop(current_sensor)
                conn.sendall(bfr.encode("utf-8"))
                current_sensor = ""

        # conn.close()

# def list_process():
#     # threading.Thread(target=list_process).start()
#
#     msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     msock.bind((HOST, PORT))
#     msock.listen()
#
#     while True:
#         conn, addr = msock.accept()
#         tm = threading.Thread(target=process, args=(conn, addr,))
#         tm.start()
#
#
# threading.Thread(target=list_process).start()
# #

msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msock.bind((HOST, PORT))
msock.listen()

while True:
    conn, addr = msock.accept()
    tm = threading.Thread(target=process, args=(conn, addr,))
    tm.start()