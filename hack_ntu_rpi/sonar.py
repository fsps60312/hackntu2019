import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ECHO, GPIO.IN)

def wait(channel, state):
    t = time.time()
    timeout = t + 0.002
    while GPIO.input(channel) != state:
        if t > timeout:
            return -1
        t = time.time()
    
    return t

def _get_distance():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(3e-5)
    GPIO.output(TRIG, GPIO.LOW)

    pulse_start = wait(ECHO, GPIO.HIGH)
    pulse_end = wait(ECHO, GPIO.LOW)
    if pulse_start < 0 or pulse_end < 0:
        return None

    pulse = pulse_end - pulse_start

    dis = 343 * pulse * 50
    return dis

def get_distance():
    N = 100
    cnt = 0
    arr = []
    for i in range(N):
        d = _get_distance()
        if d is None:
            cnt += 1
            if cnt == 3:
                return None
        else:
            arr.append(d)
    return sum(arr) / len(arr)


def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    init()
    while True:
         try:
             print(get_distance())
         except KeyboardInterrupt:
             break
    cleanup()

