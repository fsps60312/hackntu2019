from picamera import*
from time import*
sleep(10800)
t0=time()+10800
with PiCamera() as camera:
    while(time()<t0):
	camera.start_preview()
	sleep(3)
	whr="/home/pi/Desktop/picture/image"+str(time())+".jpg"
	camera.capture(whr)
	camera.stop_preview()
