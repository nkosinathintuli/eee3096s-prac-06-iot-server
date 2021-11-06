from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Sensor On':
            print("Sensor On")
            pass # do something
        elif  request.form.get('action2') == 'Sensor Off':
            print("Sensor Off")
            pass # do something else
        elif  request.form.get('action3') == 'Status':
            print("Status")
            pass # do something else
        elif  request.form.get('action4') == 'Log Check':
            print("Log Check")
            pass # do something else
        elif  request.form.get('action5') == 'Log download':
            print("Log Download")
            pass # do something else
        elif  request.form.get('action6') == 'Exit':
            print("Exit")
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)