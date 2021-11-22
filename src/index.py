from time import *
import time
import datetime
import main2
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
            main2.insert(str(1))
            pass # do something
        elif  request.form.get('action2') == 'Sensor Off':
            print("Sensor Off")
            index.active0='Sensor Off'
            main2.insert(str(0))
            pass # do something else
        elif  request.form.get('action3') == 'Status':
            print("Status")
            main2.status(index.active0)
            pass # do something else
        elif  request.form.get('action4') == 'Log Check':
            print("Log Check")
            main2.logcheck()
            pass # do something else
        elif  request.form.get('action5') == 'Log download':
            print("Log Download")
            pass # do something else
        elif  request.form.get('action6') == 'Exit':
            print("Exited")
            index.active0='Exit'
            main2.insert(str(2))
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')

def fun1():
    main2.create()
    while 1:
        time.sleep(10)
        if (main2.status_check()==str(0)):
            continue
        if (main2.status_check()==str(1)):
            tim = time0.strftime("%H:%M:%S")
            main2.send()
        if (main2.status_check()==2):
            break
            
        
        
if __name__ == '__main__':
    main2.insert(str(1))
    print(main2.status_check())
    x=threading.Thread(target=fun1)
    x.start()
    app.run(host='0.0.0.0', port=80)
    