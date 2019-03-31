#author: dreamjade
import time, RPi.GPIO as GPIO

LED_PIN=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
try:
    while True:
	print("LED is on")
    	GPIO.output(LED_PIN,GPIO.HIGH)
        time.sleep(1)
        print("LED is off")
        GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print "Excxption: KeyboardInterrupt"
finally:
    GPIO.cleanup()
