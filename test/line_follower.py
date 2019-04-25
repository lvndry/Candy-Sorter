import RPi.GPIO as GPIO
import time

# Connect the Grove Line Finder to digital port D7
# SIG,NC,VCC,GND
line_finder = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(line_finder,GPIO.IN)

while True:
    try:
        # Return HIGH when black line is detected, and LOW when white line is detected
        if GPIO.input(line_finder) == 1:
            print ("black line detected")
        else:
            print ("white line detected")

        time.sleep(.5)

    except IOError:
        print ("Error")
