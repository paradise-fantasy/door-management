import gpiozero
from time import sleep


led = gpiozero.LED(4)
	

led.on()
print("DOOR CLOSED")

def unlock():
	led.off()
	print("DOOR OPEN")
	sleep(6)
	led.on()
	print("DOOR CLOSED")

