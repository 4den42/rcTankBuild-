import RPi.GPIO as GPIO
import time

LED_PIN = 23  # GPIO pin connected to the LED
LED_PIN2 = 24
Motor_PIN = 12
Motor_PIN2 = 13

GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set GPIO 18 as an output
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(Motor_PIN, GPIO.OUT) # set gpio 25 as out
GPIO.setup(Motor_PIN2, GPIO.OUT)
try:
    print("Turning LED ON...")
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
    GPIO.output(LED_PIN2, GPIO.LOW)
 #   time.sleep(2)  # Wait for 2 seconds

    print("turning on motor")
    GPIO.output(Motor_PIN, GPIO.HIGH)
    GPIO.output(Motor_PIN2, GPIO.LOW)
    time.sleep(2)

    print("Turning LED OFF...")
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
   # time.sleep(2)

    print("tunrning motor off")
    GPIO.output(Motor_PIN, GPIO.LOW)
    GPIO.output(Motor_PIN2, GPIO.LOW)
    time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()  # Reset GPIO pins
