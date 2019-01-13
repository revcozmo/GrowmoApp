from flask import Flask, render_template, url_for
import serial
import re

app = Flask(__name__)

ser = serial.Serial('COM5', 9600)

sensor = []

t = 0
while t < 4:
    if (ser.in_waiting > 0):
        line = ser.readline().strip()
        values = line.decode('ascii').split(',')
        sensor.append(values)
        t += 1

temp = sensor[0]
ph = sensor[1]
ec = sensor[2]
do = sensor[3]

temp = re.findall('\d*\.?\d+', temp[0])
temp = temp[0]

ph = re.findall('\d*\.?\d+', ph[0])
ph = ph[0]


ec_main = re.findall('\d*\.?\d+', ec[2])

ec = ec[2]
ec1 = re.findall('\d*\.?\d+', ec[0])
ec2 = re.findall('\d*\.?\d+', ec[1])
ec3 = re.findall('\d*\.?\d+', ec[2])
ec4 = re.findall('\d*\.?\d+', ec[3])

do = re.findall('\d*\.?\d+', do[0])
do = do[0]





@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', temp=temp, ph=ph, ec1=ec1, ec2=ec2, ec3=ec3, ec4=ec4, do=do)


if __name__ == '__main__':
    app.run()
