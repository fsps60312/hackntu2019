from time import*
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
i=0
while(i<20):
    GPIO.setup(i,GPIO.OUT,initial=GPIO.HIGH)
    #GPIO.output(i,GPIO.HIGH)
    #sleep(2)
    #GPIO.output(i,GPIO.LOW)
    #sleep(2)
    i+=1
sleep(40)
GPIO.cleanup()
