import gpiozero
from time import sleep


led = gpiozero.LED(4)
	

def unlock():
	led.off()
	print("DOOR OPEN")
	sleep(6)
	led.on()
	print("DOOR CLOSED")

led.on()
print("DOOR CLOSED")

while True:
	opendoor = raw_input("Press enter to open door: ")
	unlock()
