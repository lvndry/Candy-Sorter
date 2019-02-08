import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

print("\n+----------/ ServoMoteur  Controlleur /----------+")
print("|                                                |")
print("| Le Servo doit etre branche au pin 11 / GPIO 17 |")
print("|                                                |")
print("+------------------------------------------------+\n")


pwm=GPIO.PWM(17,100)
pwm.start(5)

angle1 = 0
duty1 = float(angle1)/10 + ajoutAngle

angle2=360
duty2= float(angle2)/10 + ajoutAngle

pwm.ChangeDutyCycle(duty1)
time.sleep(0.8)
pwm.ChangeDutyCycle(duty2)
time.sleep(0.8)
GPIO.cleanup()

angle = 60

pwm=GPIO.PWM(17,100)
pwm.start(5)

angleChoisi = angle/10 + ajoutAngle
pwm.ChangeDutyCycle(angleChoisi)
time.sleep(1.5)
GPIO.cleanup()
