import pygame
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Motor control pins
IN1 = 23  # Forward direction
IN2 = 24  # Reverse direction
ENB = 25  # Enable pin (PWM)

# Set up GPIO
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# Create PWM instance
pwm = GPIO.PWM(ENB, 1000)  # 1kHz frequency
pwm.start(0)  # Start with 0% duty cycle

# Initialize pygame for joystick input
pygame.init()
pygame.joystick.init()

# Connect to the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

try:
    while True:
        pygame.event.pump()  # Process events
        y_axis = joystick.get_axis(1)  # Get Y-axis (forward/backward)

        if y_axis < -0.5:  # Joystick pushed forward
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            pwm.ChangeDutyCycle(100)  # Full power
        elif y_axis > 0.5:  # Joystick pulled backward
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            pwm.ChangeDutyCycle(100)  # Full power in reverse
        else:  # Neutral position
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            pwm.ChangeDutyCycle(0)  # Stop motor

        time.sleep(0.1)  # Small delay for stability

except KeyboardInterrupt:
    print("Exiting...")
    pwm.stop()
    GPIO.cleanup()
    pygame.quit()

