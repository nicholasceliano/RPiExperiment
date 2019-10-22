import RPi.GPIO as GPIO

pin = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

while True:
    cmd = raw_input("-->")

    if cmd == "on":
        GPIO.output(pin, GPIO.HIGH)
    elif cmd == "off":
        GPIO.output(pin, GPIO.LOW)