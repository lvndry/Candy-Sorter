import RPi.GPIO as GPIO
import time

FREQUENCE = 100
SERVO_PIN = 17
ajoutAngle = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setwarnings(False)

print("\n+----------/ ServoMotor controllor /----------+")
print("|                                               |")
print("|   Servo must be plugged on pin 11 / GPIO 17   |")
print("|                                               |")
print("+-----------------------------------------------+\n")

pwm = GPIO.PWM(SERVO_PIN, FREQUENCE)
pwm.start(5)
duty = float(angle2)/10 + ajoutAngle
pwm.ChangeDutyCycle(duty)
time.sleep(0.8)

GPIO.cleanup()
