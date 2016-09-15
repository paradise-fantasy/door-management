import RPi.GPIO as GPIO
from time import sleep
def unlock():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)

	GPIO.output(25,1)
	sleep(0.5)
	GPIO.output(25,0)
	print ("done")
	GPIO.cleanup()

