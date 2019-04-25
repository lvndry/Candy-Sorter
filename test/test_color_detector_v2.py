import RPi.GPIO as GPIO
import time

print("\n+----------/ Servomotor controller /------------+")
print("|                Candy - Sorter                 |")
print("|   Servo must be plugged on pin 11 / GPIO 17   |")
print("\n+----------/ Line finder controller /-----------+")
print("|   Captor must be plugged on pin 4             |")
print("|                                               |")
print("+-----------------------------------------------+\n")

s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 1000
NUM_CYCLES2 = 10
LINE_FINDER = 4
SERVO_PIN = 17
FREQUENCY = 22
DUTY_CYCLE = 5
ANGLE = 180

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LINE_FINDER,GPIO.IN)
	GPIO.setup(SERVO_PIN, GPIO.OUT)
	GPIO.output(SERVO_PIN, True)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(s2, GPIO.OUT)
	GPIO.setup(s3, GPIO.OUT)


def couleur_prise_mesure(nom):
	nomFic = nom + ".csv"
	fichier = open(nomFic, "w")
	fichier.write("red;blue;green\n")
	temps = 0
	while (temps<10):
                GPIO.output(s2, GPIO.LOW)
                GPIO.output(s3, GPIO.LOW)
                time.sleep(0.3)
                start = time.time()
                for impulse_count in range(NUM_CYCLES2):
                    GPIO.wait_for_edge(signal, GPIO.RISING)
                duration = time.time() - start  # seconds to run for loop
                red = NUM_CYCLES / duration  # in Hz
                # print("red value - ",red)

                GPIO.output(s2, GPIO.LOW)
                GPIO.output(s3, GPIO.HIGH)
                time.sleep(0.3)
                start = time.time()
                for impulse_count in range(NUM_CYCLES2):
                    GPIO.wait_for_edge(signal, GPIO.RISING)
                duration = time.time() - start
                blue = NUM_CYCLES / duration
                # print("blue value - ",blue)

                GPIO.output(s2, GPIO.HIGH)
                GPIO.output(s3, GPIO.HIGH)
                time.sleep(0.3)
                start = time.time()
                for impulse_count in range(NUM_CYCLES2):
                    GPIO.wait_for_edge(signal, GPIO.RISING)
                duration = time.time() - start
                green = NUM_CYCLES / duration
                # print("green value - ",green)
                # time.sleep(2)
                # print("\n\n")

                fichier.write("%.2f;%.2f;%.2f\n" % (red, blue, green))


                temps += 1

                print("Nombre de mesure : ",temps)
	fichier.close()

def savoir_couleur():
        GPIO.output(s2, GPIO.LOW)
        GPIO.output(s3, GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
                GPIO.wait_for_edge(signal, GPIO.RISING)
        duration = time.time() - start  # seconds to run for loop
        red = NUM_CYCLES / duration  # in Hz


        GPIO.output(s2, GPIO.LOW)
        GPIO.output(s3, GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
                GPIO.wait_for_edge(signal, GPIO.RISING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration


        GPIO.output(s2, GPIO.HIGH)
        GPIO.output(s3, GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
                GPIO.wait_for_edge(signal, GPIO.RISING)
        duration = time.time() - start
        green = NUM_CYCLES / duration


        if( (20000 <= red <= 20100) and (20000 <= blue <= 20100) and (14000 <= green <= 17000)):
                return "orange"
        if( (13500 <= red <= 16500) and (19000 <= blue <= 19200) and (14000 <= green <= 14500)):
                return "rouge"
        if( (19300 <= red <= 19600) and (21100 <= blue <= 21500) and (18300 <= green <= 18600)):
                return "jaune"
        if( (16300 <= red <= 16700) and (20200 <= blue <= 20600) and (17200 <= green <= 17600)):
                return "vert"
        if( (14400 <= red <= 15600) and (19700 <= blue <= 20000) and (14300 <= green <= 15000)):
                return "violet"
        return "inconnu"

def suiveur_ligne():
	# Return HIGH when black line is detected, and LOW when white line is detected
    if GPIO.input(LINE_FINDER) == 1:
        #print ("black line detected")
        return True
    else:
        #print ("white line detected")
        return False

def loop(nom):
	couleur_prise_mesure(nom)
	compteur = 0

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
	print("Nouvelle Mesure -->")

def endprogram():
	GPIO.cleanup()

if __name__=='__main__':

	setup()

	try :
		i = 0
		titreFic = ['TEST','VIOLET','VERT','ORANGE','ROUGE','JAUNE']

		while i < len(titreFic):
			loop(titreFic[i])
			i += 1;
		endprogram()

	except KeyboardInterrupt:
		endprogram()
