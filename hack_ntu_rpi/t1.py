#author: dreamjade
import time, RPi.GPIO as GPIO

LED_PIN=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

p1=GPIO.PWM(4,1000)
p1.start(0)
try:
    while True:
	for dc in range(1,101,1):
            print(dc)
            p1.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    print "Excxption: KeyboardInterrupt"
finally:
    GPIO.cleanup()
