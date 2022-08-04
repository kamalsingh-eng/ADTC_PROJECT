
import os
import datetime
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

#hostname = socket.gethostname()
#HOST = socket.gethostbyname(hostname)
HOST1 = "10.107.27.112"
HOST = "10.107.54.200"
#HOST = "10.107.27.112"

PORT = 1201
PORT1 = 1202
PORT2 = 1203
PORT3 = 1204
PORT4 = 1205
PORT5 = 1206
PORT6 = 1207

print(HOST)




def ST1_scanning():
    while(1):
       
              
       
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print("kamalalaaal")
        device_id =  "A6FE193660754"
        PRROOT = "1201"
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
        
def ST2_scanning():
    while(1):
       
              
       
        time.sleep(60)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT1))
        print("kamalalaaal")
        device_id = "A6FE193660754"
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
        device_id = "A6FE193660754"
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
        device_id = "A6FE193660754"
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
        device_id = "A6FE193660754"
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
        device_id = "A6FE193660754"
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
        device_id = "A6FE193660754"
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
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    
   




