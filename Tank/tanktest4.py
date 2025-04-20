import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define motor control pins
IN3R = 23  # IN1 is GPIO 23 and first pin on MC Right
#IN4R = 24  # IN2R is GPIO 25 and the second pin on MC Right
IN1L = 25  # IN2 is GPIO 24 and on MC Left

# Set up IN1 and IN2 pins
GPIO.setup(IN3R, GPIO.OUT)
#GPIO.setup(IN4R, GPIO.OUT)
GPIO.setup(IN1L, GPIO.OUT)

# Enable motor (run for forward direction)
print("Motor ON (Forward)...")
GPIO.output(IN3R, GPIO.HIGH)
#GPIO.output(IN4R, GPIO.HIGH)
GPIO.output(IN1L, GPIO.HIGH)
time.sleep(5)  # Motor runs for 5 seconds

# Stop motor
print("Motor OFF")
GPIO.output(IN1L, GPIO.LOW)
GPIO.output(IN3R, GPIO.LOW)
#GPIO.output(IN4R, GPIO.LOW)
time.sleep(4)  # Ensure motor is off

