from time import *
import time
import datetime
import main
import threading
import sys
global time0s
time0=datetime.datetime.now()
global time2
time2= time0.strftime("%H:%M:%S")
global active0
active0='Sensor On'

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Sensor On':
            print("Sensor On")
            index.active0='Sensor On'
            pass # do something
        elif  request.form.get('action2') == 'Sensor Off':
            print("Sensor Off")
            index.active0='Sensor Off'
            pass # do something else
        elif  request.form.get('action3') == 'Status':
            print("Status")
            main.status(index.active0)
            pass # do something else
        elif  request.form.get('action4') == 'Log Check':
            print("Log Check")
            main.logcheck()
            pass # do something else
        elif  request.form.get('action5') == 'Log download':
            print("Log Download")
            pass # do something else
        elif  request.form.get('action6') == 'Exit':
            print("Exited")
            index.active0='Exit'
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')

def fun1():
    main.create()
    while 1:
        time.sleep(10)
        if (active0=='Sensor Off'):
            main.recieving(0)
            continue
        if (active0=='Sensor Off'):
            tim = time0.strftime("%H:%M:%S")
            main.recieving(1)
        if (active0=='Sensor Off'):
            break
            
        
        
if __name__ == '__main__':
    print(active0)
    x=threading.Thread(target=fun1)
    x.start()
    app.run(host='0.0.0.0', port=80)
    