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

GPIO_TRIGGER = 7
GPIO_EchoList    = [11,13,15]

print("Ultrasonic Measurement")

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
for i in GPIO_EchoList:
	GPIO.output(GPIO_TRIGGER, False)
	GPIO.setup(i,GPIO.IN)
	GPIO_ECHO = i
	distance = measure()
	print("Pin#%d  Distance : %.1f cm" % (i, distance))
	time.sleep(1)

GPIO.cleanup()

#Credits: Script based on Matt Hawkins' work. Thanks.
