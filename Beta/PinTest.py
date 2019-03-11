import RPi.GPIO as GPIO  
from time import sleep     
GPIO.setmode(GPIO.BCM) 
GPIO.setup(25, GPIO.IN)     
GPIO.setup(24, GPIO.OUT)  
GPIO.output(24,1)  
try:  
    while True:        
        if GPIO.input(25):
            print "Accident Trigger" 
        else:  
            print "All Clear"  
         sleep(0.1)    
finally:                    
    GPIO.cleanup() 




