import socket
import json
import sys

ip = str(socket.gethostbyname(socket.gethostname()))
print(ip)
myFile = open("./ComputerIpv4.json","r+")
jsonData = myFile.read()
data = json.loads(jsonData)
data.append(ip)
newJsonData = json.dumps(data)
myFile.write(newJsonData)
myFile.close()
print("Finished")