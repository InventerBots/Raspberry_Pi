import RPi.GPIO as GPIO
import time

LED_1 = 20
LED_2 = 21
LED_3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)

while True:
	GPIO.output(LED_1, High)
	time.sleep(1)
	GPIO.output(LED_1, LOW)

	GPIO.output(LED_2, HIGH)
	time.sleep(1)
	GPIO.output(LED_2, LOW)

	GPIO.output(LED_3, HIGH)
	time.sleep(1)
	GPIO.output(LED_3, LOW)