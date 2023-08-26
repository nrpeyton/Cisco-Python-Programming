# NOTE: Did not use pip to install the pygame package (as the Windows based course material instructed) due to Ubuntu's integration/reliance with Python and dependency risks.
# Used `sudo apt install python3-xyz` (xyz = package to install).
# This won't be available for all pip repisitory packages, therefore, a venv can also be utilised.

import pygame

run = True
width = 600
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame: testing testingggg", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
