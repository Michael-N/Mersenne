from threading import Thread
import sys
import socket
import queue as Queue
import time
import argparse
import os

#Handle Each Client Connection
class handleConnection(Thread):
    def __init__(self,connection,address,index_id):
        Thread.__init__(self)
        self.q = Queue.Queue()
        self.c = connection
        self.a = address
        self.index_id = index_id
        self.doClose=False
    def addCommand(self,command):
        self.q.put(command)
    def getIdandIp(self):
        return [self.index_id,self.a]
    def closeConnection(self):
        self.doClose = True
    def run(self):
        try:
            while True:
                command = self.q.get()
                self.c.send(command.encode())
                if(self.doClose):
                    break
            self.c.close()
        finally:
            pass
#Server
class server():
    #init
    def __init__(self,ip_addr=socket.gethostbyname(socket.gethostname()),port=50007):
        #args
        self.ip_addr = ip_addr
        self.port= port
        #init
        self.soc = socket.socket()
        self.soc.bind((ip_addr,port))
        self.soc.listen(8)
        #storage
        self.commands=Queue.Queue()
        self.allConections = []
        self.parser = argparse.ArgumentParser()
        self.parserFunctions = {}

    #core functions
    def start(self):
        #Accept Connections
        self.accepter = Thread(target=self.handleAccepting,args=[])
        self.accepter.start()
        #Main Interface loop
        self.main()
    def handleAccepting(self):
        while True:
            c,a = self.soc.accept()
            print("[%s connected]" % str(a))
            id = len(self.allConections)
            hanCon = handleConnection(c, a, id)
            hanCon.setName(str(id))
            hanCon.start()
            self.allConections.append(hanCon)
    def sendCommands(self,command,indicies):
        for i in range(0, len(indicies)):
            self.allConections[indicies[i]].addCommand(command)
    def closeConections(self,indicies):
        for i in range(0,len(indicies)):
            self.allConections[indicies[i]].closeConnection()

    #utility Functions
    def printConections(self,extra):
        print("-----------")
        print("Connections")
        print("-----------")
        for i in range(0, len(self.allConections)):
            end = ""
            if i % 4 == 0:
                end = "\n"
            print("[ID:%s  @%s] " % (i, self.allConections[i].a), end)
            end = ""
    def openCodeFile(self,filepath):
        mf = open(filepath,"r")
        allLines = mf.read()
        mf.close()
        self.sendCommands(str(allLines),list(range(0, len(self.allConections))))
        print("File Text Sent")
    #Helper and Main
    def runCommandByArg(self,args):
        args = vars(args)
        for key in args:
            if args[str(key)]:
                cmd = self.parserFunctions[str(key)]
                cmd(args[str(key)])
    def main(self):
        print("------------------------------------------------------------")
        print("            Server@%s                " % self.ip_addr)
        print("-------------------------------------------")

        print("ALL commands must be prefixed by $ ex:   $--help ")
        print("and for every other command: $-c True")
        print("-------------------------------------------")
        print("[Initial Connection Wait: 5 more can connect after]")
        print("-------------------------------------------")
        time.sleep(5)
        while True:
            try:
                nc = str(input(">>>"))
                print("%s" % nc)
                if (nc[0] =="$"):
                    strArgs = nc[1:len(nc)]
                    args = self.parser.parse_args(strArgs.split(" "))
                    self.runCommandByArg(args)
                else:
                    self.sendCommands(nc, list(range(0, len(self.allConections))))
            except BaseException as e:
                print("[ERROR: %s]"%str(e))
                pass

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("-i","--ip",default=socket.gethostbyname(socket.gethostname()) ,type=str,help=" Specify the Ipv4 defaults to the computer's ip")
    parser.add_argument("-p", "--port", default=50007, type=int, help=" Specify the Port defaults to: 50007")
    args = parser.parse_args()
    snekServer = server(args.ip,args.port)

    #initalize
    #snekServer = server('192.168.1.4')

    #Console Args
    snekServer.parserFunctions["conections"] = snekServer.printConections
    snekServer.parser.add_argument("-c","--conections",action="store_true", default=False,help="Display server Connections")
    snekServer.parserFunctions["open"] = snekServer.openCodeFile
    snekServer.parser.add_argument("-o", "--open", default=False,help="Specify a Filepath to open: CHWD=[%s]"%str(os.getcwd()))
    #Begin the server
    snekServer.start()