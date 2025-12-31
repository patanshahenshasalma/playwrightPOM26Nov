import csv
import os

def insert_data_to_csv(filePath, headers, data):
    with open(filePath, mode="a", newline="") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        if(headers!=None):
            writer.writeheader()            
        writer.writerow(data)

def read_dataFromCSV(path):
    data = []
    with open(path) as csvFile:
         datainCSV = csv.DictReader(csvFile)
         for row in datainCSV:
              data.append(row)
    return data