#author: dreamjade
import RPi.GPIO as GPIO
from time import sleep
import threading
import sys, tty, termios

def getch():
    fd=sys.stdin.fileno()
    old=termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

class KeyEventThread(threading.Thread):
    def run(self):
        print("thread");
        Fun()
        #your while-loop here

def Fun():
    print("Fun")
    while True:
        key=getch()
        if key=='q':
            funExit()
            exit()
            return
        elif key=='1':
            print('speed 1')
            funSpeed(100,100)
        elif key=='2':
            print('speed 2')
            funSpeed(90,90)
        elif key=='3':
            print('speed 3')
            funSpeed(85,85)
        elif key=='w':
            print('forward')
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            funSpeed(95,95)
        elif key=='x':
            print('backward')
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            funSpeed(95,95)
        elif key=='a':
            print('left')
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            funSpeed(95,95)
        elif key=='d':
            print('right')
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            funSpeed(95,95)
        elif key=='s':
            print('stop')
            funSpeed(0,0)
        else:
            print("key"+key)
    return

def funSpeed(i1,i2):
    dc1=i1
    dc2=i2
    p1.ChangeDutyCycle(dc1)
    p2.ChangeDutyCycle(dc2)

def funInit():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en1,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en2,GPIO.OUT)

def funExit():
    print "Stopping motor"
    GPIO.output(en1,GPIO.LOW)
    GPIO.output(en2,GPIO.LOW)
    GPIO.cleanup()
    
in2=11
in1=12
en1=13
in4=15
in3=16
en2=18

print("Press 'q' to exit")
print("'w'=forward, 'x'=backward, 'a'=left, 'd'=right, 's'=stop")
print("'1','2','3' motor speed")
funInit()
p1=GPIO.PWM(en1,250)
p1.start(0)
p2=GPIO.PWM(en2,250)
p2.start(0)

kethread = KeyEventThread()
kethread.start()
