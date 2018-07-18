import pygame, sys
from pygame.locals import *
import math

def drawRegularPolygon(surface, color, numSides, tiltAngle, x, y, radius):
  pts = []
  for i in range(numSides):
    x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
    y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / numSides)
    pts.append([int(x), int(y)])
  pygame.draw.polygon(surface, color, pts)

# It's a red stop sign
pygame.init()
pygame.display.set_caption('Schmacc Board')
DISPLAYSURF = pygame.display.set_mode((800, 800))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DISPLAYSURF.fill(WHITE)
# boardx = 0
# boardy = 0
# board = pygame.image.load('SchmaccPictures/Board-1.png')
# board = pygame.transform.scale(board, (800, 800))
# DISPLAYSURF.blit(board, (boardx, boardy))
drawRegularPolygon(DISPLAYSURF, RED, 12, 0, 399, 399, 200)


while True: # main game loop


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


