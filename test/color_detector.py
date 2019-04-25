import RPi.GPIO as GPIO
import time

s2 = 23
s3 = 24
out = 25
NUM_CYCLES = 1000

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(out,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")

def loop():
  temp = 1

  while(1):
    flag = 0
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(out, GPIO.FALLING)
    duration = time.time() - start  #seconds to run for loop
    red  = NUM_CYCLES / duration    #in Hz
    print("red value - ",red)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(out, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print("blue value - ",blue)

    GPIO.output(s2, GPIO.HIGH)
    GPIO.output(s3, GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(out, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("green value - ",green)

    if (24500 <= red <= 25400 and 24000 <= blue <= 25000 and 23700 <= green <= 24900):
      print("GREEN \n")
      flag = 1

    if (25500 <= red <= 26500 and 26400 <= blue <= 27600 and 28400 <= green <= 29400):
      print("VIOLET \n")
      flag = 1

    if (21100 <= red <= 22050 and 22100 <= blue <= 22900 and 21800 <= green <= 22800):
      print("YELLOW \n")
      flag = 1

    if (24500 <= red <= 27500 and 25500 <= blue <= 26500 and 28000 <= green <= 29500):
      print("RED \n")
      flag = 1

    if (20000 <= red <= 22756 and 25500 <= blue <= 26500 and 28500 <= green <= 29100):
      print("ORANGE \n")
      flag = 1

    if (31194 <= red <= 41548 and 32855 <= blue <= 39953 and 42192 <= green <= 50576):
      print("BROWN \n")
      flag = 1

    if (flag != 1):
      print("UNKNOWN \n")

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':

    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
