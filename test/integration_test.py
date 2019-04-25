from string import Template
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

LINE_FINDER_PIN = 4
COLOR_DETECTOR_PIN_1 = 23
COLOR_DETECTOR_2 = 24
SIGNAL_DETECTOR_PIN = 25
NUM_CYCLES = 1000
NUM_CYCLES2 = 10
SERVO_PIN = 17
FREQUENCY = 22
DUTY_CYCLE = 5
ANGLE = 180

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LINE_FINDER_PIN,GPIO.IN)
	GPIO.setup(SERVO_PIN, GPIO.OUT)
	GPIO.output(SERVO_PIN, True)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SIGNAL_DETECTOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(COLOR_DETECTOR_PIN_1, GPIO.OUT)
	GPIO.setup(COLOR_DETECTOR_2, GPIO.OUT)


def couleur_prise_mesure(filename):
	path = Template('$filename.cvs')
	path.substitute(filename=filename)
	logFile = open(path, "w")
	logFile.write("red;blue;green\n")
	temps = 0
	while (temps < 20):
		GPIO.output(COLOR_DETECTOR_PIN_1, GPIO.LOW)
        GPIO.output(COLOR_DETECTOR_2, GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(SIGNAL_DETECTOR_PIN, GPIO.RISING)
        duration = time.time() - start  # seconds to run for loop
        red = NUM_CYCLES / duration  # in Hz
        # print("red value - ", red)

        GPIO.output(COLOR_DETECTOR_PIN_1, GPIO.LOW)
        GPIO.output(COLOR_DETECTOR_2, GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(SIGNAL_DETECTOR_PIN, GPIO.RISING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration
        # print("blue value - ", blue)

        GPIO.output(COLOR_DETECTOR_PIN_1, GPIO.HIGH)
        GPIO.output(COLOR_DETECTOR_2, GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(SIGNAL_DETECTOR_PIN, GPIO.RISING)
        duration = time.time() - start
        green = NUM_CYCLES / duration
        # print("green value - ", green)
        # time.sleep(2)
        # print("\n\n")

        logFile.write("%.2f;%.2f;%.2f\n" % (red, blue, green))
        temps += 1

        print("Nombre de mesure : ",temps)
	logFile.close()

def savoir_couleur():
	GPIO.output(COLOR_DETECTOR_PIN_1, GPIO.LOW)
    GPIO.output(COLOR_DETECTOR_2, GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
		GPIO.wait_for_edge(SIGNAL_DETECTOR_PIN, GPIO.RISING)
    duration = time.time() - start  # seconds to run for loop
    red = NUM_CYCLES / duration  # in Hz

    GPIO.output(COLOR_DETECTOR_PIN_1, GPIO.LOW)
    GPIO.output(COLOR_DETECTOR_2, GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
		GPIO.wait_for_edge(SIGNAL_DETECTOR_PIN, GPIO.RISING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration

    GPIO.output(COLOR_DETECTOR_PIN_1, GPIO.HIGH)
    GPIO.output(COLOR_DETECTOR_2, GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
		GPIO.wait_for_edge(SIGNAL_DETECTOR_PIN, GPIO.RISING)
    duration = time.time() - start
    green = NUM_CYCLES / duration

    #print ("red: ", red," | blue: ", blue," | green: ", green)

    if( (18000 <= red <= 20500) and (19500 <= blue <= 21200) and (14100 <= green <= 16700)):
            return "orange"
    if( (16000 <= red <= 17950) and (18000 <= blue <= 20000) and (14000 <= green <= 15100)):
            return "rouge"
    if( (18500 <= red <= 21600) and (20000 <= blue <= 22500) and (17500 <= green <= 20000)):
            return "jaune"
    if( (14700 <= red <= 15900) and (19500 <= blue <= 20500) and (14200 <= green <= 15000)):
            return "violet"
    if( (15001 <= red <= 16900) and (19500 <= blue <= 20500) and (15300 <= green <= 17700)):
            return "vert"
    return "inconnu"

def suiveur_ligne():
	# Return HIGH when black line is detected, and LOW when white line is detected
    if GPIO.input(LINE_FINDER) == 1:
        # print ("black line detected")
        return True
    else:
        # print ("white line detected")
        return False

def loop(nom = ""):
	print("Quelle couleur ? -->")
	compteur = 0
	while compteur < 10:
		savoir_couleur()
		compteur += 1
	compteur = 0
	color = "inconnu"
	while (color == "inconnu" and compteur < 30):
		color = savoir_couleur()
		if(color != "inconnu"):
			print("reponse capteur : ", color)
			compteur += 1
    if(compteur >= 30):
		print("reponse capteur : inconnu")
	pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
    pwm.start(DUTY_CYCLE)
    GPIO.setwarnings(False)
    founded = False
    angle = (float(ANGLE)/10 + 5)
    pwm.ChangeDutyCycle(angle)
    debut = time.time()
    while founded === False:
		founded = suiveur_ligne()
		chrono = time.time()-debut
		if(chrono < 0.25 and founded==False):
			debut = time.time()
	pwm.stop()
	return debut

def endprogram():
	GPIO.cleanup()

if __name__=='__main__':

	setup()

	try:
		i = 0
		while (i < 18):
			loop()
			i += 1;
		endprogram()
	except KeyboardInterrupt:
		endprogram()
