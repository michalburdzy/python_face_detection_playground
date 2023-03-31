# https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo.py

from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
# servo1 = Servo(6)

GPIO.setmode(GPIO.BCM)

servo2 = Servo(26)
servo3 = Servo(6)

def wave():
    print('I am waving at you.')
    # servo1.mid()
    servo2.value = 1
    servo3.value = 1

wave()