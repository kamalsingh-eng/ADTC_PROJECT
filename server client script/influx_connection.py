from influxdb import InfluxDBClient



client = InfluxDBClient('localhost', 8086, '', '', 'EM_DATA')
#client.create_database('example')


result = client.query('select * from em_live1 limit 10')

print("Result: {0}".format(result))