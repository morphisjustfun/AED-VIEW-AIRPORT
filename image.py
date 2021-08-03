#!/usr/bin/env python3

import sys, pygame, csv
pygame.init()

resize = 5

size = width, height = 360*resize, 180*resize
speed = [2, 2]
white = 255, 255, 255
col_lineG = 255, 0, 0
col_lineA = 0, 0, 255

screen = pygame.display.set_mode(size)

longitudG = []
latidudG = []
longitudA = []
latidudA = []

with open('coordsG.csv', 'r') as csvfile:
    dots = csv.reader(csvfile, delimiter = ';')

    for row in dots:
        longitudG.append(float(row[0]))
        latidudG.append(float(row[1]))

with open('coordsA.csv', 'r') as csvfile:
    dots = csv.reader(csvfile, delimiter = ';')

    for row in dots:
        longitudA.append(float(row[0]))
        latidudA.append(float(row[1]))


def tLongitud(n):
    return (180+n)*resize

def tLAtitud(n):
    return (90-n)*resize


background_image = pygame.image.load("map.png")
background_image = pygame.transform.scale(background_image, (size))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(background_image, [0, 0])

    prevP = []
    for i in range(len(longitudG)):
        lo = tLongitud(longitudG[i])
        la = tLAtitud(latidudG[i])

        if len(prevP) == 0:
            prevP = [lo, la]
        else:
            pygame.draw.line(screen, col_lineG, prevP, (lo, la), 2)
            prevP = [lo, la]

        if i == 0:
            pygame.draw.circle(screen, (0, 200, 0), (lo, la), 5, 4)
        elif i == len(longitudG)-1:
            pygame.draw.circle(screen, (0, 0, 0), (lo, la), 5, 4)
        else:
            pygame.draw.circle(screen, col_lineG, (lo, la), 4, 4)



    prevP = []

    for i in range(len(longitudA)):
        lo = tLongitud(longitudA[i])
        la = tLAtitud(latidudA[i])

        if len(prevP) == 0:
            prevP = [lo, la]
        else:
            pygame.draw.line(screen, col_lineA, prevP, (lo, la), 2)
            prevP = [lo, la]
        if i == 0:
            pygame.draw.circle(screen, (0, 200, 0), (lo, la), 5, 4)
        elif i == len(longitudG)-1:
            pygame.draw.circle(screen, (0, 0, 0), (lo, la), 5, 4)
        else:
            pygame.draw.circle(screen, col_lineA, (lo, la), 3, 3)

    pygame.display.flip()
