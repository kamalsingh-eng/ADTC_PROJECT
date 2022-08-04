import os
from influxdb import InfluxDBClient
import time
import pandas as pd   
#df = pd.DataFrame.from_records(influx_points_list)


client = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')
#client.create_database('example')
a = client.query("select * from em_live1 limit 100")
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
        'measurement': 'vibration',
        'time': metric[1],
        "fields" : {
             'host': metric[2],
             'lat':metric[3],
             'long':metric[4]
        }
    }]
    client.write_points(influx_metric)

print("done")
print("please check")
#print(result)

