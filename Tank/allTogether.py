#!/usr/bin/env python3
import RPi.GPIO as GPIO
import pygame
import time

# --- Pin Definitions ---
# Motor A Forward and Reverse
motor_a_forward = 23  # GPIO pin for Motor A forward
motor_a_reverse = 24  # GPIO pin for Motor A reverse
# Motor B Forward and Reverse
motor_b_forward = 25  # GPIO pin for Motor B forward (modify as needed)
motor_b_reverse = 1  # GPIO pin for Motor B reverse (modify as needed)

# Joystick deadzone to avoid drift
deadzone = 0.1

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor_a_forward, GPIO.OUT)
    GPIO.setup(motor_a_reverse, GPIO.OUT)
    GPIO.setup(motor_b_forward, GPIO.OUT)
    GPIO.setup(motor_b_reverse, GPIO.OUT)


def init_joystick():
    pygame.init()
    if pygame.joystick.get_count() < 1:
        print("No joystick detected. Please connect a joystick.")
        exit(1)
    js = pygame.joystick.Joystick(0)
    js.init()
    return js


def stop_motors():
    GPIO.output(motor_a_forward, GPIO.LOW)
    GPIO.output(motor_a_reverse, GPIO.LOW)
    GPIO.output(motor_b_forward, GPIO.LOW)
    GPIO.output(motor_b_reverse, GPIO.LOW)


def main():
    setup_gpio()
    joystick = init_joystick()
    try:
        print("Control started. Use joystick Y-axis for forward/back and X-axis for steering.")
        while True:
            pygame.event.pump()
            x = joystick.get_axis(0)  # Left/right
            y = joystick.get_axis(1)  # Up/down

            if abs(x) > deadzone:
                # Steering: one motor reverses to turn
                if x > 0:
                    # Turn right: Motor A forward, Motor B reverse
                    GPIO.output(motor_a_forward, GPIO.HIGH)
                    GPIO.output(motor_a_reverse, GPIO.LOW)
                    GPIO.output(motor_b_forward, GPIO.LOW)
                    GPIO.output(motor_b_reverse, GPIO.HIGH)
                else:
                    # Turn left: Motor A reverse, Motor B forward
                    GPIO.output(motor_a_forward, GPIO.LOW)
                    GPIO.output(motor_a_reverse, GPIO.HIGH)
                    GPIO.output(motor_b_forward, GPIO.HIGH)
                    GPIO.output(motor_b_reverse, GPIO.LOW)

            elif y < -deadzone:
                # Move forward: both motors forward
                GPIO.output(motor_a_forward, GPIO.HIGH)
                GPIO.output(motor_a_reverse, GPIO.LOW)
                GPIO.output(motor_b_forward, GPIO.HIGH)
                GPIO.output(motor_b_reverse, GPIO.LOW)

            elif y > deadzone:
                # Move backward: both motors reverse
                GPIO.output(motor_a_forward, GPIO.LOW)
                GPIO.output(motor_a_reverse, GPIO.HIGH)
                GPIO.output(motor_b_forward, GPIO.LOW)
                GPIO.output(motor_b_reverse, GPIO.HIGH)

            else:
                # Stop if within deadzone
                stop_motors()

            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        stop_motors()
        GPIO.cleanup()
        pygame.quit()


if __name__ == '__main__':
    main()
