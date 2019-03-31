#author: dreamjade
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

in1=11
in2=12
en1=13
in3=15
in4=16
en3=18

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
p1=GPIO.PWM(en1,250)
p1.start(0)
p3=GPIO.PWM(en3,250)
p3.start(0)

print "Clockwise"

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.HIGH)
for dc in range(90,101,1):
    print(dc)
    p1.ChangeDutyCycle(dc)
    p3.ChangeDutyCycle(dc)
    sleep(1)


print "Counterclockwise"

GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)
for dc in range(90,101,1):
    print(dc)
    p1.ChangeDutyCycle(dc)
    p3.ChangeDutyCycle(dc)
    sleep(1)

print "STOP"

GPIO.output(en1,GPIO.LOW)
GPIO.output(en3,GPIO.LOW)
GPIO.cleanup()
