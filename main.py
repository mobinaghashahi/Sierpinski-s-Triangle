import pygame
import random

def randomChoice():
    num = random.randrange(0, 3)
    return num

def midPoins(x1,y1,x2,y2):
    x=(x1+x2)/2
    y=(y1+y2)/2
    return x,y

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

count=1000000

x=[10,10,500]
y=[10,500,10]


xStart=50
yStart=100

pygame.draw.line(screen, (0, 255, 0), (x[0], y[0]), (x[1], y[1]), 5)
pygame.draw.line(screen, (100, 25, 100), (x[0], y[0]), (x[2],y[2]), 5)
pygame.draw.line(screen, (100, 5, 0), (x[1],y[1]), (x[2], y[2]), 5)
pygame.draw.circle(screen, (0, 255, 0), (xStart, yStart), 4)
while count>0:
    indexRandPoint=randomChoice()
    xStart, yStart=midPoins(x[indexRandPoint],y[indexRandPoint],xStart,yStart)
    count-=1
    pygame.draw.circle(screen, (0, 255, 0), (xStart, yStart), 2)

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
