import os
from influxdb import InfluxDBClient
import time
import pandas as pd   
#df = pd.DataFrame.from_records(influx_points_list)


client = InfluxDBClient('192.168.0.147', 8086, '', '', 'EM_DATA')

client1 = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')
#client.create_database('example')
a = client.query("select * from em_live1 limit 100")
#df = pd.DataFrame.from_records(influx_points_list)
df = pd.DataFrame(a.get_points())
df.to_csv("C:\\Users\\u18m90\\Pictures\\VIBRATION2.csv")
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
#print(result)

