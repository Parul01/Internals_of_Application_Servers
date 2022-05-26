from ftplib import FTP
import json

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
# ftp.cwd('/home/parul/Desktop/IIITH/sem2/ias') #replace with your directory
ftp.retrlines('LIST')
ftp.cwd('Test')

fname = input()
parameters = input().split(" ")
requestData = {"function_name": fname,
               "no_of_arguments": len(parameters),
               "arguments": parameters}

case = 0
if(fname == "multiply"):

 requestData = {"function_name": fname,
                "no_of_arguments": len(parameters),
                "argument_1": [parameters[0],int],
                "argument_2": [parameters[1],int]}

if(fname ==  "sum" and len(parameters) == 2 ):
 requestData = {"function_name": fname,
                "no_of_arguments": len(parameters),
                "argument_1": [parameters[0],int],
                "argument_2": [parameters[1],int]
                }

if(fname == "sum" and len(parameters) == 3):
 requestData = {"function_name": fname,
                "no_of_arguments": len(parameters),
                "argument_1": [parameters[0],int],
                "argument_2": [parameters[1],int],
                "argument_3": [parameters[1],int]
                }

if(fname == "sum" and len(parameters) == 4):
 requestData = {"function name": fname,
                "no_of_arguments": len(parameters),
                "argument_1": [parameters[0],int],
                "argument_2": [parameters[1],int],
                "argument_3": [parameters[0], int],
                "argument_4": [parameters[1], int]
                }

with open('demo.txt', 'w') as sf:
 json.dump(str(requestData), sf)
# ------------------------ function calling
# send data to server in form of json file
def requestData():
 filename = 'demo.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def retreiveData():
 filename = 'demo.txt' #replace with your file in the directory ('directory_name')
 wfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, wfile.write, 1024)
 ftp.quit()
 wfile.close()

requestData()
# retreiveData()