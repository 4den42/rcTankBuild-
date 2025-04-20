import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO pins
IN3R = 23  # IN1 is GPIO 23 and first pin on MC Right
IN4R = 24
IN1L = 25  # IN2 is GPIO 24 and on MC Left

# Set up IN1 and IN2 pins
GPIO.setup(IN3R, GPIO.OUT)
GPIO.setup(IN4R, GPIO.OUT)
GPIO.setup(IN1L, GPIO.OUT)

# Enable motor (run for forward direction)
print("Motor ON (Forward)...")
GPIO.output(IN3R, GPIO.LOW)
GPIO.output(IN4R, GPIO.HIGH)
GPIO.output(IN1L, GPIO.HIGH)
time.sleep(4)  # Motor runs for 5 seconds

# Stop motor
print("Motor OFF")
GPIO.output(IN1L, GPIO.LOW)
GPIO.output(IN3R, GPIO.LOW)
GPIO.output(IN4R, GPIO.LOW)
GPIO.cleanup()
