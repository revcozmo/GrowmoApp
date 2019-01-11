from flask import Flask, render_template, url_for
import serial


app = Flask(__name__)


ser = serial.Serial('COM5', 9600)

sensor = []

t = 0
while t < 4:
    if(ser.in_waiting > 0):
        line = ser.readline().strip()
        values = line.decode('ascii').split(',')
        sensor.append(values)
        t += 1


temp = sensor[0]
ph = sensor[1]
ec = sensor[2]
do = sensor[3]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', temp=temp, ph=ph, ec=ec, do=do)


if __name__ == '__main__':
    app.run(debug=True)
