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
d13=0;

d21 =0
d22 =0
time.sleep(5)

def data_collection():
    
    while True:
    
        d1 = randint(49,51)
        d2 = randint(220,240)
        d3 = randint(220,240)
        d4 = randint(220,240)
        d5 = randint(415,440)
        d6 = randint(415,440)
        d7 = randint(415,440)
        d8 = randint(10,15)
        d9 = randint(10, 15)
        d10 = randint(10, 15)
        d11 = randint(10,15)
        d12 = 1.732*d5*d11/1000.0
        d13 = 0.0 
       
        d14 = randint(85,100)/100.0
        d15 = randint(250,500)/100.0
        d16 =  randint(250,500)/100.0
        d17 =randint(250,500)/100.0
        d18 =randint(250,500)/100.0
        d19 =d13
        d20 = 0.0;
        

        
        
        
        data3 = json.dumps({ "ID":"SUZUKI/123", "NCH1":d1,"NCH2":d2,"NCH3":d3,"NCH4":d4,"NCH5":d5,"NCH6":d6,"NCH7":d7,"NCH8":d8,"NCH9":d9,"NCH10":d10,"NCH11":d11,"NCH12":d12,"NCH13":d13,"NCH14":d14,"NCH15":d15,"NCH16":d16,"NCH17":d17,"NCH18":d18,"NCH19":d19,"NCH20":d20})
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
    
   
        

