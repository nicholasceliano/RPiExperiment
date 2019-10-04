import RPi.GPIO as gpio
import time

ledPin = 18

gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

while True:
	gpio.output(ledPin, gpio.HIGH)
	passcode = raw_input("What is pi?: ")
	
	if passcode == "Awesome":
		gpio.output(ledPin, gpio.LOW)
		time.sleep(4)
	else:
		gpio.output(ledPin, gpio.HIGH)
		print("Wrong Password!")	