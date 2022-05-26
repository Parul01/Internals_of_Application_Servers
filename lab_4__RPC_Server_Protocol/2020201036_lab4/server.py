from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import json


def multiply(self, a, b):
    responseData = {"prod": int(a) * int(b)}


class CustomHandler(FTPHandler):

    def on_connect(self):
        pass
        # print "%s:%s connected" % (self.remote_ip, self.remote_port)


    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):

        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        print(file)
        # self.retrbinary('RETR ' + file, self.write)
        # res = self.retrbinary('RETR %s' % file)
        # print(res)

        inFile = open(file, "r")
        # res = inFile.read(1032)
        res = json.load(inFile)
        print(str(res.function_name))
        # if res['function name'] == 'multiply':
        #     outf = multiply(res['argument_1'[0],res['argument_2'[0]])
        #
        # if res['function name'] == 'sum':
        #     if res['no of arguments'] == 2:
        #     outf = self.multiply(res['argument_1'[0], res['argument_2'[0]])
        #         # call sum_v1
        #     if res['no of arguments'] == 3:
        #         # call sum_v3
        #     if res['no of arguments'] == 4:
        #         #call sum_v4





        # pass
    def multiply(self,a,b):
        responseData = {"prod": int(a)*int(b)}

    def sum_v1(self,a,b):
        responseData = {"sum":int(a)+int(b)}

    def sum_v2(self,a,b,c):
        responseData = {"sum":int(a)+int(b)+int(c)}
    def sum_v3(self,a,b,c,d):
        responseData = {"sum": int(a) + int(b) + int(c) + int(d)}

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        print
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/parul", perm="elradfmw")
authorizer.add_anonymous("/home/parul", perm="elradfmw")

handler = CustomHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1022), handler)
server.serve_forever()
