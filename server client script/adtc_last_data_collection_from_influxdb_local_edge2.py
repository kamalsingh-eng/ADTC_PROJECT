import os
from influxdb import InfluxDBClient
import time
import pandas as pd
import json
#df = pd.DataFrame.from_records(influx_points_list)


client = InfluxDBClient('192.168.0.147', 8086, '', '', 'EM_DATA')
#client.create_database('example')
a = client.query("select last(N5) as a1,last(N6) as a2,last(N7) as a3,last(N8) as a4 from em_live1 where ID = 'ADTC/LS1' and time > now() - 10m;")
a1 = list(a.get_points())
#print(a1)
a2 = a1[0]['a1']
a3 = a1[0]['a2']
a4 = a1[0]['a3']
a5 = a1[0]['a4']

b = client.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3,last(N4) as a4,last(N9) as a5 from em_live1 where ID = 'ADTC/GSM1' and time >now() - 10m;")
b1 = list(b.get_points())
#print(a1)
b2 = b1[0]['a1']
b3 = b1[0]['a2']
b4 = b1[0]['a3']
b5 = b1[0]['a4']
b6 = b1[0]['a5']

c = client.query("select last(N1) as a1,last(N2) as a2,last(N3) as a3 from em_live1 where ID = 'ADTC/GS1' and time > now() - 10m;")
c1 = list(c.get_points())
#print(a1)
c2 = c1[0]['a1']
c3 = c1[0]['a2']
c4 = c1[0]['a3']


data = {
"front-left alarm":a2,
"front-right alarm":a3,
"Back-left alarm":a4,
"Back-right alarm":a5,
"long":b2,
"lat":b3,
"Reverse count":b4,
"forward count":b5,
"stop count":b6,
"Zebra Crossing":c2,
"Gradient Sensor Parking":c3, 
"Parking Sensor Alarm":c4

}

data1 = json.dumps(data)
print(data1)
