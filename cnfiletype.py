# convert example1.json to csv file
import json
import csv  
with open('example1.json', 'r') as f:
    data = json.load(f)
with open('example2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])

