import pygame

pygame.init()
pygame.joystick.init()

print("Joysticks found:", pygame.joystick.get_count())

for i in range(pygame.joystick.get_count()):
    j = pygame.joystick.Joystick(i)
    j.init()
    print(f"Joystick {i}: {j.get_name()}")
