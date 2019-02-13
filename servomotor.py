import RPi.GPIO as GPIO
import time

SERVO_PIN = 17
FREQUENCE = 100
DUTY_CYCLE = 7.5
ajoutAngle = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setwarnings(False)

print("\n+----------/ ServoMotor controllor /----------+")
print("|                Candy - Sorter                 |")
print("|   Servo must be plugged on pin 11 / GPIO 17   |")
print("|                                               |")
print("+-----------------------------------------------+\n")

pwm = GPIO.PWM(SERVO_PIN, FREQUENCE)
pwm.start(DUTY_CYCLE)
duty = float(angle2)/10 + ajoutAngle
GPIO.output(17, True)
pwm.ChangeDutyCycle(DUTY_CYCLE)
time.sleep(1) # 60 degree
GPIO.output(17, False)
pwm.ChangeDutyCycle(0)

GPIO.cleanup()
