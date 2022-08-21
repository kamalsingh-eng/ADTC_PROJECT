
import os
import datetime
#from sunau import AUDIO_FILE_ENCODING_LINEAR_16
from time import sleep
import time
from datetime import datetime
import socket
import sys
import json
import random
import shutil
import os
import threading
import random
import math
import paho.mqtt.client as mqtt
import pandas as pd
from influxdb import InfluxDBClient
#hostname = socket.gethostname()
#HOST = socket.gethostbyname(hostname)
#HOST1 = "10.107.27.112"
#HOST = "10.107.54.200"
HOST = "192.168.87.130"

PORT = 1201
PORT1 = 1202
PORT2 = 1203
PORT3 = 1204
PORT4 = 1205
PORT5 = 1206
PORT6 = 1207

global a11
global a16
global a17
global a18
a11 = "";
a16 = "";
a17 = "";
a18 = "";
print(HOST)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        
        #client.subscribe("VANAZ_PT")
        
        global Connected                #Use global variable
        Connected = True                #Signal connection 

    else:
        print("Connection failed")

def on_message(mosq, obj, msg):
    print(msg.topic+" Data is coming")
def track1_punch(mosq, obj, msg):
    a=str(msg.payload.decode("utf-8"))
    global a11
    a11 =json.loads(a)
    print(a11)
def track2_punch(mosq, obj, msg):
    a2=str(msg.payload.decode("utf-8"))
    global a12
    a12 =json.loads(a2)
def track3_punch(mosq, obj, msg):
    a3=str(msg.payload.decode("utf-8"))
    global a13
    a13 =json.loads(a3)
def track4_punch(mosq, obj, msg):
    a4=str(msg.payload.decode("utf-8"))
    global a14
    a14 =json.loads(a4)
def track5_punch(mosq, obj, msg):
    a5=str(msg.payload.decode("utf-8"))
    global a15
    a15 =json.loads(a5)
def IotBox1_Alarm(mosq, obj, msg):
    a6=str(msg.payload.decode("utf-8"))
    global a16
    a16 =json.loads(a6)
def IotBox2_Alarm(mosq, obj, msg):
    a7=str(msg.payload.decode("utf-8"))
    global a17
    a17 =json.loads(a7)
def IotBox3_Alarm(mosq, obj, msg):
    a8=str(msg.payload.decode("utf-8"))
    global a18
    a18 =json.loads(a8)
    
    

client = mqtt.Client("vib_monitoring_12223223323")  #create new instance set username and password

client.message_callback_add('AC/1_ADTC', track1_punch)
client.message_callback_add('AC/2_ADTC', track2_punch)
client.message_callback_add('AC/3_ADTC', track3_punch)
client.message_callback_add('AC/4_ADTC', track4_punch)
client.message_callback_add('AC/5_ADTC', track5_punch)
client.message_callback_add('STFB/1AL', IotBox1_Alarm)
client.message_callback_add('STFB/2AL', IotBox2_Alarm)
client.message_callback_add('STFB/3AL', IotBox3_Alarm)



client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect("203.110.86.71", 1883, 60)          #connect to brokerc=a
client.subscribe("AC/#")
client.subscribe("STFB/#")



   




def ST1_scanning():
    al_fd =0
    while(1):
        global a11
        global a16 
        global a17  
        global a18  
        
        global a18  
        if not a11 =="":
            a1_1 = a11['TrackID']
            a1_2 = a11['IotBox']
            print(len(a1_2))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print("kamalalaaal")
            device_id = a1_1
            PRROOT = "1201"
            data4 = "%s|%s" % (device_id, PRROOT)
            sock.sendall(bytes(data4, encoding="utf-8"))
            print("Sent:     {}".format(data4))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            # need to Publish the feedback 
            sock.close()
            if received1:
                time1 = time.time()
                data1 = received2.split("|")
                data3 = data1[0]
                data4 = data1[1]
                data5 = data1[2]
                #print(type(data5));
                #print(data5)
                data5 = data5[0:3]



                print(data5 == 'HMV')
            if data5 == 'HMV':
                LW = 2.34;
                HW = 10.33;
                LA = 2.0;
                HA = 11.00;
            if data5 == "LMV":
                LW = 2.34;
                HW = 10.33;
                LA = 2.0;
                HA = 11.00;
            data = {
                "Track":1,
                "LW":LW,
                "HW":HW,
                "LA":LA,
                "HA":HA,

                }
            data = json.dumps(data)
            client3 = mqtt.Client("vib_monitoring_1222322DEDE")
            client3.connect("203.110.86.71", 1883, 60)
            if a1_2 == "001":
                client3.publish("ST/1AL",data)
            if a1_2 == "002":
                client3.publish("ST/2AL",data)
            if a1_2 == "003":
                client3.publish("ST/3AL",data)
            
            a11 = "";
        if not a16 == "":
            if a16['feedback'] == 1 and a1_2 == "001":
                al_fd = 1 ;
        if not a17 == "":
            if a17['feedback'] == 1 and a1_2 == "002":
                al_fd = 2 ;
        if not a18 == "":
            if a18['feedback'] == 1 and a1_2 == "003":
                al_fd = 3 ;
            

        if al_fd == 1:
            client = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')

            client1 = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')
            #client.create_database('example')
            a = client.query("select * from local_edge1 limit 100")
            #df = pd.DataFrame.from_records(influx_points_list)
            df = pd.DataFrame(a.get_points())
            df.to_csv("C:\\Users\\u18m90\\Pictures\\VIBRATION1.csv")
            time.sleep(1)
                        
            #cpu_points = list(result.get_points(measurement='em_live1'))
            #client.write_points(result,database='example')
            def read_data():
                with open("C:\\Users\\u18m90\\Pictures\\VIBRATION1.csv") as f:
                    return [x.split(',') for x in f.readlines()[1:]]

            a = read_data()

            for metric in a:
                influx_metric = [{
                    'measurement': 'local_edge2',
                    'time': metric[1],
                    "fields" : {
                        'ID': metric[2],
                        'N1':metric[3],
                        'N2':metric[6],
                        'N3':metric[7],
                        'N4':metric[8],
                        'N5': metric[9],
                        'N6':metric[10],
                        'N7':metric[11],
                        'N8':metric[12],
                        'N9':metric[13],
                        'N10': metric[4],
                        'N11':metric[5],
                        
                    }
                }]
                client1.write_points(influx_metric)

            print("done")
            print("please check")
            a = client1.query("select last(N5) as a1,last(N6) as a2,last(N7) as a3,last(N8) as a4 from local_edge2 where ID = 'ADTC/LS1';")
            a1 = list(a.get_points())
            print(a1)
            a2 = a1[0]['a1']
            a3 = a1[0]['a2']
            a4 = a1[0]['a3']
            a5 = a1[0]['a4']

            b = client1.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3,last(N4) as a4,last(N9) as a5 from local_edge2 where ID = 'ADTC/GSM1';")
            b1 = list(b.get_points())
            #print(a1)
            b2 = b1[0]['a1']
            b3 = b1[0]['a2']
            b4 = b1[0]['a3']
            b5 = b1[0]['a4']
            b6 = b1[0]['a5']

            c = client1.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3 from local_edge2 where ID = 'ADTC/GS1';")
            c1 = list(c.get_points())
            #print(a1)
            c2 = c1[0]['a1']
            c3 = c1[0]['a2']
            c4 = c1[0]['a3']
            test_attempt = 1
            tsv_violation = c2
            std_direction =  c3
            reverse_dir_stop = b3
            Avg_speed = b5
            kerb_hit = a2
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            #tt = random.randint(30,40)
            #time.sleep(tt)
        
            time2 = time.time()
            time_difference = time2-time1
            #DDD =input("just response")
            
            data2 = "%s|%d|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
        
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(4)
            al_fd = 0
            a16 =""
            a11 = ""


        if al_fd == 2:
            client = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')

            client1 = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')
            #client.create_database('example')
            a = client.query("select * from local_edge1 limit 100")
            #df = pd.DataFrame.from_records(influx_points_list)
            df = pd.DataFrame(a.get_points())
            df.to_csv("C:\\Users\\u18m90\\Pictures\\VIBRATION3.csv")
            time.sleep(1)
                        
            #cpu_points = list(result.get_points(measurement='em_live1'))
            #client.write_points(result,database='example')
            def read_data():
                with open("C:\\Users\\u18m90\\Pictures\\VIBRATION3.csv") as f:
                    return [x.split(',') for x in f.readlines()[1:]]

            a = read_data()

            for metric in a:
                influx_metric = [{
                    'measurement': 'local_edge3',
                    'time': metric[1],
                    "fields" : {
                        'ID': metric[2],
                        'N1':metric[3],
                        'N2':metric[6],
                        'N3':metric[7],
                        'N4':metric[8],
                        'N5': metric[9],
                        'N6':metric[10],
                        'N7':metric[11],
                        'N8':metric[12],
                        'N9':metric[13],
                        'N10': metric[4],
                        'N11':metric[5],
                        
                    }
                }]
                client1.write_points(influx_metric)

            print("done")
            print("please check")
            a = client1.query("select last(N5) as a1,last(N6) as a2,last(N7) as a3,last(N8) as a4 from local_edge3 where ID = 'ADTC/LS1';")
            a1 = list(a.get_points())
            print(a1)
            a2 = a1[0]['a1']
            a3 = a1[0]['a2']
            a4 = a1[0]['a3']
            a5 = a1[0]['a4']

            b = client1.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3,last(N4) as a4,last(N9) as a5 from local_edge3 where ID = 'ADTC/GSM1';")
            b1 = list(b.get_points())
            #print(a1)
            b2 = b1[0]['a1']
            b3 = b1[0]['a2']
            b4 = b1[0]['a3']
            b5 = b1[0]['a4']
            b6 = b1[0]['a5']

            c = client1.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3 from local_edge3 where ID = 'ADTC/GS1';")
            c1 = list(c.get_points())
            #print(a1)
            c2 = c1[0]['a1']
            c3 = c1[0]['a2']
            c4 = c1[0]['a3']
            test_attempt = 1
            tsv_violation = c2
            std_direction = c3
            reverse_dir_stop = b3
            Avg_speed = b5
            kerb_hit = a2
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            #tt = random.randint(30,40)
            #time.sleep(tt)
            print(a2,a3,a4,a5,b2,b3,b4,b5,c2,c3,c4)
            time2 = time.time()
            time_difference = time2-time1
            #DDD =input("just response")

            data2 = "%s|%d|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
        
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(4)
            al_fd = 0
            a17 = ""
            a11 = ""
            
        if al_fd == 3:
            client = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')

            client1 = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')
            #client.create_database('example')
            a = client.query("select * from local_edge1 limit 100")
            #df = pd.DataFrame.from_records(influx_points_list)
            df = pd.DataFrame(a.get_points())
            df.to_csv("C:\\Users\\u18m90\\Pictures\\VIBRATION4.csv")
            time.sleep(1)
                        
            #cpu_points = list(result.get_points(measurement='em_live1'))
            #client.write_points(result,database='example')
            def read_data():
                with open("C:\\Users\\u18m90\\Pictures\\VIBRATION4.csv") as f:
                    return [x.split(',') for x in f.readlines()[1:]]

            a = read_data()

            for metric in a:
                influx_metric = [{
                    'measurement': 'local_edge4',
                    'time': metric[1],
                    "fields" : {
                        'ID': metric[2],
                        'N1':metric[3],
                        'N2':metric[6],
                        'N3':metric[7],
                        'N4':metric[8],
                        'N5': metric[9],
                        'N6':metric[10],
                        'N7':metric[11],
                        'N8':metric[12],
                        'N9':metric[13],
                        'N10': metric[4],
                        'N11':metric[5],
                        
                    }
                }]
                client1.write_points(influx_metric)

            print("done")
            print("please check")
            a = client1.query("select last(N5) as a1,last(N6) as a2,last(N7) as a3,last(N8) as a4 from local_edge4 where ID = 'ADTC/LS1';")
            a1 = list(a.get_points())
            #print(a1)
            a2 = a1[0]['a1']
            a3 = a1[0]['a2']
            a4 = a1[0]['a3']
            a5 = a1[0]['a4']

            b = client1.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3,last(N4) as a4,last(N9) as a5 from local_edge4 where ID = 'ADTC/GSM1';")
            b1 = list(b.get_points())
            #print(a1)
            b2 = b1[0]['a1']
            b3 = b1[0]['a2']
            b4 = b1[0]['a3']
            b5 = b1[0]['a4']
            b6 = b1[0]['a5']

            c = client1.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3 from local_edge4 where ID = 'ADTC/GS1';")
            c1 = list(c.get_points())
            #print(a1)
            c2 = c1[0]['a1']
            c3 = c1[0]['a2']
            c4 = c1[0]['a3']
            test_attempt = 1
            tsv_violation = c2
            std_direction =  c3
            reverse_dir_stop = b3
            Avg_speed = b5
            kerb_hit = a2
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            #tt = random.randint(30,40)
            #time.sleep(tt)
        
            time2 = time.time()
            time_difference = time2-time1
            #DDD =input("just response")
            
            data2 = "%s|%d|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
        
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(4)
            al_fd = 0
            a18 = ""
            a11 = ""

            
            


                               

                            
            


        
       
        
       
              
       
        
        
        
            
       
"""
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,15)*10)/100)
        print(test_attempt)
        if test_attempt:
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  math.floor((random.randint(10,22)*6)/100)
            reverse_dir_stop = random.randint(1,7)
            Avg_speed = random.randint(5,10)
            kerb_hit = random.randint(1,7)
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            tt = random.randint(30,40)
            time.sleep(tt)
           
            time2 = time.time()
            time_difference = time2-time1
            #DDD =input("just response")
            
            data2 = "%s|%d|%d|%d|%d|%d|%d|%d|%s|%s|%s|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
           
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(400)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4
            

           
            #time.sleep(5)
            DDD =input("just response")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%s|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(5)
"""       
def ST2_scanning():
    while(1):
       
              
       
        time.sleep(60)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT1))
        print("kamalalaaal")
        device_id = "A6FE193660752"
        PRROOT = "1202"
        data4 = "%s|%s" % (device_id, PRROOT)
        sock.sendall(bytes(data4, encoding="utf-8"))
        print("Sent:     {}".format(data4))
        received1 = sock.recv(1024)
        received2 = received1.decode("utf-8")
        sock.close()
        if received1:
            time1 = time.time()
            data1 = received2.split("|")
            data3 = data1[0]
            data4 = data1[1]
            data5 = data1[2]
            
        print(time1)
        print(data3)

        print(data4)
        
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,16)*10)/100)
        print(test_attempt)
        if test_attempt:
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  math.floor((random.randint(10,22)*6)/100)
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = random.randint(1,7)
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            tt = random.randint(20,30)
            time.sleep(tt)
           
            time2 = time.time()
            time_difference = time2-time1
            
            #DDD =input("just response")
            data2 = "%s|%d|%d|%d|%s|%d|%s|%d|%s|%s|%s|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT1))
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(800)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT1))
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4
            

           
            #time.sleep(5)
            DDD =input("just response")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%s|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(340)
        
def ST3_scanning():
    while(1):
        time.sleep(120)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT2))
        print("kamalalaaal")
        device_id = "A6FE193660752"
        PRROOT = "1203"
        data4 = "%s|%s" % (device_id, PRROOT)
        sock.sendall(bytes(data4, encoding="utf-8"))
        print("Sent:     {}".format(data4))
        received1 = sock.recv(1024)
        received2 = received1.decode("utf-8")
        sock.close()
        if received1:
            time1 = time.time()
            data1 = received2.split("|")
            data3 = data1[0]
            data4 = data1[1]
            data5 = data1[2]
            
        print(time1)
        print(data3)

        print(data4)
        
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,16)*10)/100)
        print(test_attempt)      
        
        if test_attempt:
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  math.floor((random.randint(10,22)*6)/100)
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = random.randint(1,10)
            roll_back = math.floor((random.randint(11,16)*10)/100)
            applicant_id = data4

            tt = random.randint(15,26)
            time.sleep(tt)
            #dd3 = input("track3--->")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%d|%d|%d|%s|%d|%s|%s|%s|%s|%d|%d|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT2))
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(280)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT2))
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

           
            #time.sleep(5)
            dd3 = input("track3--->")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%s|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            sock.close()
            time.sleep(10)

def ST4_scanning():
    while(1):
       
              
        time.sleep(180)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT3))
        print("kamalalaaal")
        device_id = "A6FE193660752"
        PRROOT = "1204"
        data4 = "%s|%s" % (device_id, PRROOT)
        sock.sendall(bytes(data4, encoding="utf-8"))
        print("Sent:     {}".format(data4))
        received1 = sock.recv(1024)
        received2 = received1.decode("utf-8")
        sock.close()
        if received1:
            time1 = time.time()
            data1 = received2.split("|")
            data3 = data1[0]
            data4 = data1[1]
            data5 = data1[2]
            
        print(time1)
        print(data3)

        print(data4)
        
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,16)*10)/100)
        print(test_attempt)
        if test_attempt:
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = random.randint(1,7)
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            tt = random.randint(20,30)
            time.sleep(tt)
            #dd3 = input("track4-->")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%d|%d|%s|%s|%d|%s|%d|%s|%s|%s|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT3))
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(220)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT3))
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

           
            time.sleep(5)
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%s|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            sock.close()
            time.sleep(10)

def ST5_scanning():
    while(1):
       
              
        time.sleep(240)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT4))
        print("kamalalaaal")
        device_id = "A6FE193660752"
        PRROOT = "1205"
        data4 = "%s|%s" % (device_id, PRROOT)
        sock.sendall(bytes(data4, encoding="utf-8"))
        print("Sent:     {}".format(data4))
        received1 = sock.recv(1024)
        received2 = received1.decode("utf-8")
        sock.close()
        if received1:
            time1 = time.time()
            data1 = received2.split("|")
            data3 = data1[0]
            data4 = data1[1]
            data5 = data1[2]
            
        print(time1)
        print(data3)

        print(data4)
        
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,15)*10)/100)
        print(test_attempt)
        if test_attempt:
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = math.floor((random.randint(10,22)*6)/100)
            mirror_gazing = math.floor((random.randint(10,22)*6)/100)
            out_of_track = random.randint(1,7)
            roll_back = "xx"
            applicant_id = data4

            tt = random.randint(20,30)
            time.sleep(tt)
            #dd3 = input("track5------")
            time2 = time.time()
            time_difference = "xx"
            data2 = "%s|%d|%d|%s|%s|%s|%s|%s|%s|%s|%d|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT4))
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(160)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT4))
            
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

           
            time.sleep(5)
            time2 = time.time()
            time_difference = "xx"
            data2 = "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            sock.close()
            time.sleep(10)


def ST6_scanning():
    while(1):
       
              
        time.sleep(300)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT5))
        print("kamalalaaal")
        device_id = "A6FE193660752"
        PRROOT = "1206"
        data4 = "%s|%s" % (device_id, PRROOT)
        sock.sendall(bytes(data4, encoding="utf-8"))
        print("Sent:     {}".format(data4))
        received1 = sock.recv(1024)
        received2 = received1.decode("utf-8")
        sock.close()
        if received1:
            time1 = time.time()
            data1 = received2.split("|")
            data3 = data1[0]
            data4 = data1[1]
            data5 = data1[2]
            
        print(time1)
        print(data3)

        print(data4)
        
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,15)*10)/100)
        print(test_attempt)
        if test_attempt:
            
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  math.floor((random.randint(10,22)*6)/100)
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = random.randint(1,7)
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            tt = random.randint(20,30)
            time.sleep(tt)
            #dd3 = input("errrerrr")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%d|%d|%d|%s|%d|%s|%d|%s|%s|%s|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT5))
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(800)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT5))
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

           
            time.sleep(5)
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%s|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            sock.close()
            time.sleep(80)


def ST7_scanning():
    while(1):

       
              
        time.sleep(360)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT6))
        print("kamalalaaal")
        device_id = "A6FE193660752"
        PRROOT = "1207"
        data4 = "%s|%s" % (device_id, PRROOT)
        sock.sendall(bytes(data4, encoding="utf-8"))
        print("Sent:     {}".format(data4))
        received1 = sock.recv(1024)
        received2 = received1.decode("utf-8")
        sock.close()
        if received1:
            time1 = time.time()
            data1 = received2.split("|")
            data3 = data1[0]
            data4 = data1[1]
            data5 = data1[2]
            
        print(time1)
        print(data3)

        print(data4)
        
        print("Received: {}".format(received2))
        print("successfully received")
        test_attempt = math.floor((random.randint(11,15)*10)/100)
        print(test_attempt)
        if test_attempt:
            
            tsv_violation = math.floor((random.randint(10,22)*6)/100)
            std_direction =  math.floor((random.randint(10,22)*6)/100)
            reverse_dir_stop = random.randint(1,7)
            Avg_speed = random.randint(5,10)
            kerb_hit = random.randint(1,7)
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

            tt = random.randint(20,30)
            time.sleep(tt)
            #dd3 = input("test2------>")
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%d|%d|%d|%d|%d|%d|%d|%s|%s|%s|%s|%d|%d|%s|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3,data5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT6))
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            received1 = sock.recv(1024)
            received2 = received1.decode("utf-8")
            print("Received: {}".format(received2))
            print("successfully received")
            sock.close()
            time.sleep(10)

        if not test_attempt:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT6))
            tsv_violation = "xx"
            std_direction =  "xx"
            reverse_dir_stop = "xx"
            Avg_speed = "xx"
            kerb_hit = "xx"
            zcv = "xx" 
            mirror_gazing = "xx"
            out_of_track = "xx"
            roll_back = "xx"
            applicant_id = data4

           
            time.sleep(5)
            time2 = time.time()
            time_difference = time2-time1
            data2 = "%s|%s|%s|%s|%s|%d|%s|%s|%s|%s|%s|%s|%d|%d|%s|%s<EOF>" % (
                                data3, test_attempt, tsv_violation, std_direction,
                                reverse_dir_stop,time_difference,Avg_speed, kerb_hit, zcv, mirror_gazing,
                                out_of_track, roll_back, time1,time2,applicant_id,data3)
            sock.sendall(bytes(data2, encoding="utf-8"))
            print("Sent:     {}".format(data2))
            sock.close()
            time.sleep(10)










if __name__=="__main__":
  
    t1=threading.Thread(target=ST1_scanning)
    t2=threading.Thread(target=ST2_scanning)
    t3=threading.Thread(target=ST3_scanning)
    t4=threading.Thread(target=ST4_scanning)
    t5=threading.Thread(target=ST5_scanning)
    t6=threading.Thread(target=ST6_scanning)
    t7=threading.Thread(target=ST7_scanning)
    
   
    
  
    t1.start()
    #t2.start()
    #t3.start()
    #t4.start()
    #t5.start()
    #t6.start()
    #t7.start()
    
   

client.loop_forever()


