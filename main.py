import time, RPi.GPIO as GPIO
def measure():
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()
  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  pulse_interval = stop-start
  distance = (pulse_interval * 34300)/2

  return distance

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = [1,2,3,4,5,6,7,8]
GPIO_ECHO    = 24

print "Ultrasonic Measurement"

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)  
GPIO.output(GPIO_TRIGGER, False)

try:
  while True:
    distance = measure()
    print "Distance : %.1f cm" % distance
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
