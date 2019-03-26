import RPi.GPIO as GPIO
import time

print("\n+----------/ Servomotor controller /----------+")
print("|                Candy - Sorter                 |")
print("|   Servo must be plugged on pin 11 / GPIO 17   |")
print("|                                               |")
print("+-----------------------------------------------+\n")

SERVO_PIN = 17
GOBELET = 1
ANGLE = 60 * GOBELET
FREQUENCY = 50
START_FC = 50
DUTY_CYCLE = 5
ROTATION_TIME = 1.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(17, True)

pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
pwm.start(START_FC)
angle = (float(ANGLE)/180 + 1) * 5
pwm.ChangeDutyCycle(angle)
time.sleep(ROTATION_TIME) # 60 degree

pwm.ChangeDutyCycle(0)
time.sleep(2)

origin = (((360 - ANGLE) / 180) + 1) * 5
pwm.ChangeDutyCycle(origin)
time.sleep(ROTATION_TIME)

pwm.stop()
GPIO.output(17, False)
GPIO.cleanup()
