import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5
angle = 270
duree = 0.2

pwm=GPIO.PWM(17, 100)
pwm.start(5)

angleChoisi = angle/10 + ajoutAngle
pwm.ChangeDutyCycle(angleChoisi)
time.sleep(duree)

GPIO.cleanup()
