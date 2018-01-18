import numpy as np 
import csv, os

city_data = []
with open('/Users/tianyu/Desktop/Astar/data/CityData.csv') as f:
	reader = csv.reader(f)
	next(reader, None) # skip header
	for row in reader:
		items = [np.int(i) for i in row]
		city_data.append(items)
city_data = np.array(city_data)
print(city_data)

insitu_data = []
with open('/Users/tianyu/Desktop/Astar/data/In_situMeasurementforTraining_201712.csv') as f:
	reader = csv.reader(f)
	next(reader, None) # skip header
	for row in reader:
		items = [np.float(i) for i in row]
		insitu_data.append(items)
insitu_data = np.array(insitu_data)
print(city_data)