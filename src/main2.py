import time
import datetime
import random
from csv import DictReader
# Import writer class from csv module
from csv import writer
import csv
import os
global temp_ADC
temp_ADC = 14000
global LDR_ADC
LDR_ADC = 17000

global counter
counter=time.time()
e=datetime.datetime.now()
global tim
tim = e.strftime("%H:%M:%S")
def create():
    header = ['Date', 'Time', 'Temparature', 'LDR']
    with open('sensorlog.csv', 'w',encoding='UTF8',newline='') as csvfile: 
        writer1 = writer(csvfile) 
        writer1.writerow(header)
        csvfile.close()


def to_temp():
    round(15.2789,3)
    t_a=str(round(21.132+random.randrange(-3,3,1)/random.randrange(1,7,2),2))+"C"
    return t_a

def insert(cmd):
    header = ['Status']
    with open('status.csv', 'w',encoding='UTF8',newline='') as csvfile: 
        writer1 = writer(csvfile)
        writer1.writerow(header)
        writer1.writerow(cmd)
        csvfile.close()

def status_check():
    with open('status.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            return str(row['Status'])

def add(row):
    with open('sensorlog.csv', 'a',encoding='UTF8',newline='') as csvfile: 
        writer1 = writer(csvfile) 
        writer1.writerow(row)
        csvfile.close()

def send():
  e = datetime.datetime.now()
  date = e.strftime("%d/%m/%Y")
  tim = e.strftime("%H:%M:%S")
  strin=date+' '+tim+' '+str(to_temp())+' '+str(LDR_ADC+random.randrange(-900,900,1))
  counter=time.time()
  add(strin.split(" "))
  print("Data Received:",strin)

# for checking the status and print the last time it was sample

def receiving():  
# iterate over each line as a ordered dictionary and print only few column by column name
    with open('sensorlog.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            print("Data Received:",row['Date'], row['Time'],row['Temparature'],row['LDR'])

def status(active1):
    if(active1=="Sensor On"):
        print("The last data was sampled at:",tim)
    elif(active1=='Sensor Off'):
        print("The Pi is not sampling")


def logcheck():
    with open('sensorlog.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        count=1
        print("The last 10 items to be samples are listed")
        for row in csv_dict_reader:
            print(count,row['Date'], row['Time'],row['Temparature'],row['LDR'])
            count=count+1
            if(count>=11):
                break

def download():
	path = "sensorlog.csv"
	return send_file(path, as_attachment=True)

create()
for i in range(0,10):
    send()
logcheck()