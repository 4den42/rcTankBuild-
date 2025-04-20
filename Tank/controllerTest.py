import pygame
import RPi.GPIO as GPIO
import time

# Setup LED pin
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Init pygame and joystick
pygame.init()
pygame.joystick.init()

# Make sure at least one joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick detected.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Detected joystick: {joystick.get_name()}")

print("Listening for controller input... (CTRL+C to quit)")

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
                if event.button == 0:  # Usually BtnA or BtnB on Joy-Con (R)
                    GPIO.output(LED_PIN, GPIO.HIGH)
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")
                if event.button == 0:
                    GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()
    pygame.quit()
