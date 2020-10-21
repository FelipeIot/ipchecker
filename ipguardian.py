#!/usr/bin/python3
import socket
import fcntl
import struct
import os
from time import sleep

def get_ipfpga():
  f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
  ipdir=f.read()
  f.close()
  return ipdir


def get_ipservicio():
  f = os.popen("grep -w 'address' '/etc/network/interfaces'| cut -d ' ' -f2")
  ip=f.read()
  f.close()
  print("ip de la carpeta interfaces: ",ip)
  return ip


  
def get_ipconfig():
  try:
    with open("/home/ubuntu/vms/config/IPBASE.csv", "r") as f:
      path=f.read()
      texto=path.split('\n')
  except:
    print("Error lectura "+self.dirDivisas)
  return texto[1]

while True:
  dirbase=get_ipconfig()
  dirinterfaces=get_ipservicio()
  diriplocal=get_ipfpga()

  response = os.system("ping -c 1 " + dirbase)


  if response == 0:
    print('PING BASE OK')
    if diriplocal==dirinterfaces:
      print("IP CORRECTA")
    else:
      print("IP INCORRECTA")
      sleep(60)
      os.system("sudo reboot now")  
  else:
    print( 'PING BASE WRONG')
  sleep(1)


