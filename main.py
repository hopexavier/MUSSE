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

GPIO_TRIGGER = 8
GPIO_EchoList = [7,11,12,13,15,16,18,22]

print("Ultrasonic Measurement")

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
for i in GPIO_EchoList:
	GPIO.output(GPIO_TRIGGER, False)
	GPIO.setup(i,GPIO.IN)
	GPIO_ECHO = i
	distance = measure()
	if distance > 500.0:
		print("Invalid Reading(too far)")
	elif distance < 2.0:
		print("Invalid Reading(too short)")
	else:
		print("Pin#%d  Distance : %.1f cm" % (i, distance))
	time.sleep(0.01)
GPIO.cleanup()
