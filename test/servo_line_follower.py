import RPi.GPIO as GPIO
import time

print("\n+----------/ Servomotor controller /------------+\n\n")

print("\n+----------/ Servomotor controller /------------+")
print("|                Candy - Sorter                 |")
print("|   Servo must be plugged on pin 11 / GPIO 17   |")
print("\n+----------/ Line finder controller /-----------+")
print("|   Captor must be plugged on pin 4             |")
print("|                                               |")
print("+-----------------------------------------------+\n")


LINE_FINDER = 4
SERVO_PIN = 17
FREQUENCY = 22
DUTY_CYCLE = 5
ANGLE =180

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LINE_FINDER,GPIO.IN)
	GPIO.setup(SERVO_PIN, GPIO.OUT)
	GPIO.output(SERVO_PIN, True)


def suiveur_ligne():
	# Return HIGH when black line is detected, and LOW when white line is detected
    if GPIO.input(LINE_FINDER) == 1:
        print ("black line detected")
        return True
    else:
        print ("white line detected")
        return False

def loop():
        while True:
                pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
                pwm.start(DUTY_CYCLE)
                GPIO.setwarnings(False)
                tourner = True
                angle = (float(ANGLE)/10 + 5)
                pwm.ChangeDutyCycle(angle)
                debut = time.time()
                while tourner:
                        tourner = suiveur_ligne()
                        chrono = time.time()-debut
                        if(chrono < 0.25 and tourner==False):
                                tourner = True
                                debut = time.time()
                pwm.stop()
                input("Appuyer sur entrée pour continuer")
                time.sleep(1)

def endprogram():
	GPIO.cleanup()
	pwm.stop()

if __name__=='__main__':

	setup()

	try :
		loop()

	except KeyboardInterrupt:
		endprogram()

