from websocket import create_connection
from time import sleep
import RPi.GPIO as GPIO
from sklearn import tree
import numpy as np
import smbus                    #import SMBus module of I2C
from time import sleep          #import
import math

PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def MPU_Init():
        #write to sample rate register
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

        #Write to power management register
        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

        #Write to Configuration register
        bus.write_byte_data(Device_Address, CONFIG, 0)

        #Write to Gyro configuration register
        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

        #Write to interrupt enable register
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
        #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24,1)
static="Mr Sample,9754754185,TN12KF3636,lat:25.5941,lng:85.1376"
i=1
s="hello"
ws=create_connection("ws://192.168.43.14:5001")
bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address
MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

data = np.loadtxt('data1.csv', delimiter=',')
features = data[:, 0:2]
labels = data[:, 2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

while True:
    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)

    #Read Gyroscope raw value
    #gyro_x = read_raw_data(GYRO_XOUT_H)
    #gyro_y = read_raw_data(GYRO_YOUT_H)
    Ax = (acc_x*9.8)/16384.0
    Ay = (9.8*acc_y)/16384.0
    Az = (9.8*acc_z)/16384.0
    acc = math.sqrt((Ax*Ax)+(Ay*Ay)+(Az*Az))
    acci = int(acc)
    print("Ax=%.2f" %Ax, "    Ay=%.2f" %Ay, "    Az=%.2f" %Az, "    Accel=%.2f" %acci)
    res=int(clf.predict([[acci,0]]))
    print(res)
    if res: # if port 25 == 1
        print ("Accident Occured")
        ws.send(static)
    else:
        print("All Clear" )
        sleep(0.1)

    sleep(0.1)
ws.close()
