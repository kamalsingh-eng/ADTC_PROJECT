#import socket
import time
import json
#from sense_emu import SenseHat
import sys
from datetime import datetime
from random import uniform
from time import asctime
from time import sleep
#sense=SenseHat()
import threading
import os
import paho.mqtt.client as mqtt
import time


client = mqtt.Client("espclient100")
    #client.username_pw_set(username="kamal", password="23021991")
    #create new instance
         #set username and password
                       #attach function to callback

client.connect("192.168.43.217", 1883, 60)          #connect to brokerc=a

client.loop_forever()

while True:
    client.subscribe("001")
    time.sleep(1)