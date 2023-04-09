import sys, math, random
import pygame
from pygame import mixer

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')

# sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    """ The player class. """
    screen.blit(playerImg, (x, y))  # draw (image, (x/y locations to draw))


# game loop
running = True
while running:

    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            """" if keystroke is pressed, check if its right or left """

            if event.key == pygame.K_LEFT:
                playerX_change = -5
                playerX = playerX_change
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            """ if key is let go: """
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    player(playerX, playerY)
    pygame.display.update()