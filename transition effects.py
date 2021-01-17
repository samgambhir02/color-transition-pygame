# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import time
#SCREEN SETUP
pygame.init()
dis_width=800
dis_height=600
screen=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("***TRANSITION EFFECT***")

r=255
g=255
b=0

#color=(r,g,b)
while True: 
    if g==1:
        g==0
    else:
        g-=1
    if r==1:
        r=0
    elif g<=100 and r>1:
        r-=1
    if r<=100:
        b+=1
    color=(r,g,b)
    #print('working')
    for event in pygame.event.get():
            if event.type==pygame.QUIT or b>=250:
                pygame.quit()
    screen.fill(color)
    pygame.display.update()
    time.sleep(0.1)
    