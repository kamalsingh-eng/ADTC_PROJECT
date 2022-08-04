import socket
import time
#from sense_emu import SenseHat
import sys
from datetime import datetime
from random import uniform
from time import asctime
from time import sleep
#sense=SenseHat()

import os
import paho.mqtt.client as mqtt
import time
import threading
import json
import csv


def client_start():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            
            #client.subscribe("VANAZ_PT")
          
            global Connected                #Use global variable
            Connected = True                #Signal connection 
 
        else:
            print("Connection failed")
 
    def on_message(client, userdata, message):

        
        a=str(message.payload.decode("utf-8"))
        a1 =json.loads(a)

    client = mqtt.Client("vib_monitoring_12223223323")               #create new instance
     #set username and password
    client.on_connect= on_connect                      #attach function to callback
    client.on_message= on_message                      #attach function to callback
 
    client.connect("203.110.86.71", 1883, 60)          #connect to brokerc=a
   
    client.loop_forever()

def ST1_scanning(client,message):
    while(1):
        client.subscribe("001")
        a=str(message.payload.decode("utf-8"))
        a1 =json.loads(a)
        time.sleep(1)


if __name__=="__main__":
  
    t1=threading.Thread(target=ST1_scanning)
    t2=threading.Thread(target=client_start)
  
    
   
    
  
    t1.start()
    t2.start()
   