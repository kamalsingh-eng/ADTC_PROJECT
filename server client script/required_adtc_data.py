import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import os
import json
from datetime import datetime
from random import randint
import time
import csv
import threading
broker = "203.110.86.71"
port = 1883

time.sleep(5)

def punch_data():
    
    while True:
        a = input("punch at track-1");
        d1 = "QWE1234321"
        d2 = "001"


    
       
        

        
        
        
        data3 = json.dumps({ "ID":"AC/1_ADTC", "NCH1":d1,"NCH2":d2})
        print(data3)
        client.publish("SUZUKI/123",data3)
        time.sleep(1)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
                        
        print("Connected to broker")
        client.subscribe("EnergyMeter1")

        global Connected                #Use global variable
        Connected = True                #Signal connection 

    else:
        print("Bad connection Returned code=",rc)

def on_message(client)
                        
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client = mqtt.Client("espdfdfdd123445")
#create new instance
     #set username and password
#client.username_pw_set(username="kamal", password="23021991")
#client.tls_set('e:/ca.crt','e:/test2.crt','e:/test2.key')
client.on_connect= on_connect                      #attach function to callback
mqtt.Client.connected_flag=False#create flag in class

client.on_publish = on_publish  

print("Connecting to broker ",broker)
client.connect(broker,port, 60)        #connect to broker

#                    while not client.connected_flag: #wait in loop
#                        print("In wait loop")
#                        time.sleep(1)
print("in Main Loop")
               
 
 
 
if __name__=="__main__":
    t1=threading.Thread(target=data_collection)
    #t2=threading.Thread(target=client1_start)
   
    
    t1.start() 
 
 
 

       
    
client.loop_forever()
   
   
    #publish.single(MQTT_PATH, MSG, hostname=MQTT_SERVER,port=1883,client_id="espclient",qos=0, auth={'username':"kamal", 'password':"23021991"} ,will=None, tls=None,
    #transport="tcp")
    
   
        

