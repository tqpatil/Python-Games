##import pygame
##import math
##import random
##
##pygame.init()
##dwidth = 1280
##dheight = 720
##gameDisplay = pygame.display.set_mode((dwidth, dheight))
##pygame.display.set_caption('Arrow Game')
##
#### add collision detection, varying arrow speeds, background graphics, music, homing arrows, levels, stages of endless mode, end/retry screen, more slots, quadratic falling
##
##slot1 = True
##s1x = 0
##slt = None
##s1c = None
##slot2 = True
##s2x = 0
##s2t = None
##s2c = None
##slot3 = True
##s3x = 0
##s3t = None
##s3c = None
##slot4 = True
##s4x = 0
##s4t = None
##s4c = None
##slot5 = True
##s5x = 0
##s5t = None
##s5c = None
##slot6 = True
##s6x = 0
##s6t = None
##s6c = None
##slot7 = True
##s7x = 0
##s7t = None
##s7c = None
##slot8 = True
##s8x = 0
##s8t = None
##s8c = None
##slot9 = True
##s9x = 0
##s9t = None
##s9c = None
##slot10 = True
##s10x = 0
##s10t = None
##s10c = None
##
##skyBlue = (164, 218, 235)
##
##clock = pygame.time.Clock()
##
##crashed = False
##
##flipStatus = False
##
##bird = pygame.transform.scale(pygame.image.load('bird2.png'), (150, 150))
##f1 = pygame.transform.scale(pygame.image.load('f1.png'), (150, 150))
##f2 = pygame.transform.scale(pygame.image.load('f2.png'), (150, 150))
##f3 = pygame.transform.scale(pygame.image.load('f3.png'), (150, 150))
##f4 = pygame.transform.scale(pygame.image.load('f4.png'), (150, 150))
##redArrow = pygame.transform.scale(pygame.image.load('redArrow.png'), (100, 140))
##orangeArrow = pygame.transform.scale(pygame.image.load('orangeArrow.png'), (100, 140))
##yellowArrow = pygame.transform.scale(pygame.image.load('yellowArrow.png'), (100, 140))
##purpleArrow = pygame.transform.scale(pygame.image.load('purpleArrow.png'), (100, 140))
##lightGreenArrow = pygame.transform.scale(pygame.image.load('lightGreenArrow.png'), (100, 140))
##deepBlueArrow = pygame.transform.scale(pygame.image.load('deepBlueArrow.png'), (100, 140))
##aquaArrow = pygame.transform.scale(pygame.image.load('aquaArrow.png'), (100, 140))
##pinkArrow = pygame.transform.scale(pygame.image.load('pinkArrow.png'), (100, 140))
##gArrow = pygame.transform.scale(pygame.image.load('greenArrow.png'), (100, 140))
##bArrow = pygame.transform.scale(pygame.image.load('blueArrow.png'), (100, 140))
##whiteArrow = pygame.transform.scale(pygame.image.load('whiteArrow.png'), (100, 140))
##
##
##def placeBird(a,x,y):
##    global redArrow
##    global orangeArrow
##    global yellowArrow
##    global gArrow
##    global bArrow
##    global aquaArrow
##    global purpleArrow
##    global pinkArrow
##    global lightGreenArrow
##    global deepBlueArrow
##    global whiteArrow
##    gameDisplay.blit(a, (x,y))
##
##def flapWing(a):
##    if a == 1:
##        return f1
##    elif a == 2:
##        return f2
##    elif a == 3:
##        return f3
##    elif a == 4:
##        return f4
##
##
##
##lastTime = pygame.time.get_ticks()
##lastFlip = pygame.time.get_ticks()
##flipCooldown = 500
##cooldown = 200
##flapCooldown = 500
##
##x = (dwidth*0.4)
##y=(dheight*0.4)
##
##b = 12
##
##c1 = False
##
##diffX = 0
##diffY = 0
##
##def valueSetter(color):
##    global redArrow
##    global orangeArrow
##    global lightGreenArrow
##    global deepBlueArrow
##    global yellowArrow
##    global gArrow
##    global bArrow
##    global aquaArrow
##    global purpleArrow
##    global pinkArrow
##    global whiteArrow
##    if color is purpleArrow:
##        delay = 2000
##        dps = 150
##    elif color is deepBlueArrow:
##        delay = 1400
##        dps = 300
##    elif color is lightGreenArrow:
##        delay = 1000
##        dps = 400
##    elif color is aquaArrow:
##        delay = 750
##        dps = 600
##    elif color is redArrow:
##        delay = 500
##        dps = 800
##    elif color is yellowArrow:
##        delay = 250
##        dps = 950
##    elif color is pinkArrow:
##        delay = 100
##        dps = 1100
##    elif color is whiteArrow:
##        delay = 0
##        dps = 1300
##    return (delay, dps)
##
##
##def text_objects(text, font):
##    textSurface = font.render(text, True, (0,0,0))
##    return textSurface, textSurface.get_rect()
##
##def message_display(text, n, m, size, font):
##    font = pygame.font.SysFont(font, size)
##    ##largeText = pygame.font.Font('freesansbold.ttf',size)
##    TextSurf, TextRect = text_objects(text, font)
##    TextRect.center = ((int(dwidth/n)),(int(dheight/m)))
##    gameDisplay.blit(TextSurf, TextRect)
##
##def arrowSpawn(color, startTime, location, slot):
##    global redArrow
##    global orangeArrow
##    global yellowArrow
##    global gArrow
##    global bArrow
##    global aquaArrow
##    global purpleArrow
##    global whiteArrow
##    global pinkArrow
##    global lightGreenArrow
##    global deepBlueArrow
##    global dheight
##    global slot1
##    global slot2
##    global slot3
##    global slot4
##    global slot5
##    global slot6
##    global slot7
##    global slot8
##    global slot9
##    global slot10
##    global s1c
##    global s2c
##    global s3c
##    global s4c
##    global s5c
##    global s6c
##    global s7c
##    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
##
##    eTime=pygame.time.get_ticks()-startTime
##
##    if slot == 1:
##        (delay, dps) = valueSetter(s1c)
##    if slot == 2:
##        (delay, dps) = valueSetter(s2c)
##    if slot == 3:
##        (delay, dps) = valueSetter(s3c)
##    if slot == 4:
##        (delay, dps) = valueSetter(s4c)
##    if slot == 5:
##        (delay, dps) = valueSetter(s5c)
##    if slot == 6:
##        (delay, dps) = valueSetter(s6c)
##    if slot == 7:
##        (delay, dps) = valueSetter(s7c)
##    if slot == 8:
##        (delay, dps) = valueSetter(s8c)
##    if slot == 9:
##        (delay, dps) = valueSetter(s9c)
##    if slot == 10:
##        (delay, dps) = valueSetter(s10c)
##
##    xx = ((eTime-delay*5/4)/100)
##    if(eTime < delay/4):
##        placeBird(color,location,0)
##    elif(eTime>=delay/4 and eTime < delay/2):
##        placeBird(orangeArrow,location,0)
##    elif(eTime>=delay/2 and eTime < delay*3/4):
##        placeBird(color,location,0)
##    elif(eTime>=delay*3/4 and eTime < delay):
##        placeBird(orangeArrow,location,0)
##    elif(eTime<=delay+delay/4):
##        placeBird(color,location,0)
##    elif(eTime > delay + delay/4):
##        placeBird(color,location,((xx**2 + 5*xx)*(dps/100)))
##
##    if ((xx**2 + 5*xx)*(dps/100)) > dheight + 100:
##        if slot == 1:
##            slot1 = True
##        if slot == 2:
##            slot2 = True
##        if slot == 3:
##            slot3 = True
##        if slot == 4:
##            slot4 = True
##        if slot == 5:
##            slot5 = True
##        if slot == 6:
##            slot6 = True
##        if slot == 7:
##            slot7 = True
##        if slot == 8:
##            slot8 = True
##        if slot == 9:
##            slot9 = True
##        if slot == 10:
##            slot10 = True
##
##
##
##
##def titleLoop():
##    global c1
##    global skyBlue
##    global gameDisplay
##    global bArrow
##    global redArrow
##    global orangeArrow
##    global gArrow
##    global whiteArrow
##    global aquaArrow
##    global pinkArrow
##    global purpleArrow
##    global yellowArrow
##    global lightGreenArrow
##    global deepBlueArrow
##    while not c1:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##        gameDisplay.fill(skyBlue)
##        placeBird(redArrow, 605, 235)
##        message_display("Arrows", 2, 2.2, 200, "franklingothicdemicond")
##        message_display("click to start", 2, 1.6, 50, "georgia")
##        pygame.display.update()
##        z = 2000*98*456
##        clock.tick(60)
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            c1 = True
##
##def gameLoop():
##    global crashed
##    global x
##    global y
##    global b
##    global flipStatus
##    global bird
##    global skyBlue
##    global f1
##    global f2
##    global f3
##    global f4
##    global flipCooldown
##    global lastFlip
##    global cooldown
##    global flapCooldown
##    global lastTime
##    global dwidth
##    global dheight
##    global diffX
##    global diffY
##    global redArrow
##    global orangeArrow
##    global yellowArrow
##    global gArrow
##    global bArrow
##    global whiteArrow
##    global aquaArrow
##    global lightGreenArrow
##    global deepBlueArrow
##    global purpleArrow
##    global pinkArrow
##    global slot1
##    global slot2
##    global slot3
##    global slot4
##    global slot5
##    global slot6
##    global slot7
##    global slot8
##    global slot9
##    global slot10
##    global s1c
##    global s2c
##    global s3c
##    global s4c
##    global s5c
##    global s6c
##    global s7c
##    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
##    while not crashed:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                crashed = True
##
##            ##print(event)
##
##            ##if event.type == pygame.MOUSEMOTION:
##        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
##                    ##x = pygame.mouse.get_pos()[0] - 75
##                    ##y = pygame.mouse.get_pos()[1] - 75
##            diffX = (pygame.mouse.get_pos()[0] - 75) - x
##            diffY = (pygame.mouse.get_pos()[1] - 75) - y
##            x += 0.1*diffX
##            y += 0.1*diffY
##
##        currentTime = pygame.time.get_ticks()
##
##        if pygame.mouse.get_pos()[0] - 75 < x - 30:
##            if not flipStatus:
##                if currentTime - lastFlip > flipCooldown:
##                    bird = pygame.transform.flip(bird, True, False)
##                    f1 = pygame.transform.flip(f1, True, False)
##                    f2 = pygame.transform.flip(f2, True, False)
##                    f3 = pygame.transform.flip(f3, True, False)
##                    f4 = pygame.transform.flip(f4, True, False)
##                    flipStatus = True
##        elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
##            if flipStatus:
##                if currentTime - lastFlip > flipCooldown:
##                    bird = pygame.transform.flip(bird, True, False)
##                    f1 = pygame.transform.flip(f1, True, False)
##                    f2 = pygame.transform.flip(f2, True, False)
##                    f3 = pygame.transform.flip(f3, True, False)
##                    f4 = pygame.transform.flip(f4, True, False)
##                    flipStatus = False
##
##
##        gameDisplay.fill(skyBlue)
##
##        if (currentTime - lastTime) > cooldown:
##            if (currentTime - lastTime) < cooldown + flapCooldown/5:
##                c = flapWing(1)
##                placeBird(c, x,y)
##            elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
##                c = flapWing(2)
##                placeBird(c, x,y)
##            elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
##                c = flapWing(3)
##                placeBird(c, x,y)
##            elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
##                c = flapWing(4)
##                placeBird(c, x,y)
##            else:
##                lastTime = currentTime
##                placeBird(bird, x,y)
##
##
##        else:
##            placeBird(bird, x,y)
##
##        r = int((random.random())*1000 + 1)
##        if r < 50:
##            if slot1:
##                s1t = currentTime
##                s1c = purpleArrow
##                ##colorChooser(1 for stage 1)
##                s1x = int((random.random())*1280 + 1)
##                arrowSpawn(s1c, s1t, s1x, 1)
##                slot1 = False
##            elif slot2:
##                s2t = currentTime
##                s2x = int((random.random())*1280 + 1)
##                s2c = deepBlueArrow
##                arrowSpawn(s2c, s2t, s2x, 2)
##                slot2 = False
##            elif slot3:
##                s3t = currentTime
##                s3x = int((random.random())*1280 + 1)
##                s3c = lightGreenArrow
##                arrowSpawn(s3c, s3t, s3x, 3)
##                slot3 = False
##            elif slot4:
##                s4t = currentTime
##                s4x = int((random.random())*1280 + 1)
##                s4c = aquaArrow
##                arrowSpawn(s4c, s4t, s4x, 4)
##                slot4 = False
##            elif slot5:
##                s5t = currentTime
##                s5x = int((random.random())*1280 + 1)
##                s5c = redArrow
##                arrowSpawn(s5c, s5t, s5x, 5)
##                slot5 = False
##            elif slot6:
##                s6t = currentTime
##                s6x = int((random.random())*1280 + 1)
##                s6c = yellowArrow
##                arrowSpawn(s6c, s6t, s6x, 6)
##                slot6 = False
##            elif slot7:
##                s7t = currentTime
##                s7x = int((random.random())*1280 + 1)
##                s7c = pinkArrow
##                arrowSpawn(s7c, s7t, s7x, 7)
##                slot7 = False
##            elif slot8:
##                s8t = currentTime
##                s8x = int((random.random())*1280 + 1)
##                s8c = whiteArrow
##                arrowSpawn(s8c, s8t, s8x, 8)
##                slot8 = False
##            elif slot9:
##                s9t = currentTime
##                s9x = int((random.random())*1280 + 1)
##                s9c = redArrow
##                arrowSpawn(s9c, s9t, s9x, 9)
##                slot9 = False
##            elif slot10:
##                s10t = currentTime
##                s10x = int((random.random())*1280 + 1)
##                s10c = redArrow
##                arrowSpawn(s10c, s10t, s10x, 10)
##                slot10 = False
##
##        if not slot1:
##            arrowSpawn(s1c, s1t, s1x, 1)
##        if not slot2:
##            arrowSpawn(s2c, s2t, s2x, 2)
##        if not slot3:
##            arrowSpawn(s3c, s3t, s3x, 3)
##        if not slot4:
##            arrowSpawn(s4c, s4t, s4x, 4)
##        if not slot5:
##            arrowSpawn(s5c, s5t, s5x, 5)
##        if not slot6:
##            arrowSpawn(s6c, s6t, s6x, 6)
##        if not slot7:
##            arrowSpawn(s7c, s7t, s7x, 7)
##        if not slot8:
##            arrowSpawn(s8c, s8t, s8x, 8)
##        if not slot9:
##            arrowSpawn(s9c, s9t, s9x, 9)
##        if not slot10:
##            arrowSpawn(s10c, s10t, s10x, 10)
##
##
##
##
##
##
##        pygame.display.update()
##        clock.tick(60)
##
##
##titleLoop()
##gameLoop()
##pygame.quit()
##quit()

import pygame
import math
import random
import copy
import time
#!python
pygame.mixer.pre_init(44100, 16, 8, 4096)
pygame.init()
dwidth = 1280
dheight = 720
gameDisplay = pygame.display.set_mode((dwidth, dheight), pygame.FULLSCREEN)
pygame.display.set_caption('Arrow Game')

## background graphics, music, levels,

currentTime = pygame.time.get_ticks()
passed = False
slot1 = True
s1x = 0
slt = None
s1c = None
slot2 = True
s2x = 0
s2t = None
s2c = None
slot3 = True
s3x = 0
s3t = None
s3c = None
slot4 = True
s4x = 0
s4t = None
s4c = None
slot5 = True
s5x = 0
s5t = None
s5c = None
slot6 = True
s6x = 0
s6t = None
s6c = None
slot7 = True
s7x = 0
s7t = None
s7c = None
slot8 = True
s8x = 0
s8t = None
s8c = None
slot9 = True
s9x = 0
s9t = None
s9c = None
slot10 = True
s10x = 0
s10t = None
s10c = None
s1s = False
s2s = False
s3s = False
s4s = False
s5s = False
s6s = False
s7s = False
s8s = False
s9s = False
s10s = False
s11s = False
s12s = False
s13s = False
s14s = False
slot11 = True
s11y = 0
sllt = None
s11c = None
slot12 = True
s12y = 0
sl2t = None
s12c = None
slot13 = True
s13y = 0
sl3t = None
s13c = None
slot14 = True
s14y = 0
sl4t = None
s14c = None
s11sd = None
s12sd = None
s13sd = None
s14sd = None


cslot1 = True
c1y = 0
c1t = None
c1c = None
c1s = None
cslot2 = True
c2y = 0
c2t = None
c2c = None
c2s = None
cslot3 = True
c3y = 0
c3t = None
c3c = None
c3s = None


isInvinc = False
usedInvinc = False
invincTime = 0

isDouble = False
doubleTime = 0

levelUnlocked = 1
level5Complete = False

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
p10 = 0
p11 = 0
p12 = 0
p13 = 0
p14 = 0

##skyBlue = (164, 218, 235)
skyBlue = (88, 173, 245)
##skyBlue = (120, 182, 239)
clock = pygame.time.Clock()

crashed = False

flipStatus = False

firstTime = 0
cloud7=pygame.transform.scale(pygame.image.load('cloud7.png'),(40,30))
cloud6=pygame.transform.scale(pygame.image.load('cloud6.png'),(90,48))
cloud5=pygame.transform.scale(pygame.image.load('cloud5.png'),(160,128))
cloud4=pygame.transform.scale(pygame.image.load('cloud4.png'),(400,138))
cloud3=pygame.transform.scale(pygame.image.load('cloud3.png'),(280,75))
cloud2=pygame.transform.scale(pygame.image.load('cloud2.png'), (310,130))
cloud1=pygame.transform.scale(pygame.image.load('cloud1.png'),(280,130))
bird = pygame.transform.scale(pygame.image.load('bird2.png'), (150, 150))
birdt=pygame.transform.scale(pygame.image.load('bird2t.png'), (150,150))
f1 = pygame.transform.scale(pygame.image.load('f1.png'), (150, 150))
f1t=pygame.transform.scale(pygame.image.load('f1t.png'),(150,150))
f2 = pygame.transform.scale(pygame.image.load('f2.png'), (150, 150))
f2t=pygame.transform.scale(pygame.image.load('f2t.png'), (150,150))
f3 = pygame.transform.scale(pygame.image.load('f3.png'), (150, 150))
f3t= pygame.transform.scale(pygame.image.load('f3t.png'),(150,150))
f4 = pygame.transform.scale(pygame.image.load('f4.png'), (150, 150))
f4t=pygame.transform.scale(pygame.image.load('f4t.png'),(150,150))
redArrow = pygame.transform.scale(pygame.image.load('redArrow.png'), (100, 140))
orangeArrow = pygame.transform.scale(pygame.image.load('orangeArrow.png'), (100, 140))
yellowArrow = pygame.transform.scale(pygame.image.load('yellowArrow.png'), (100, 140))
purpleArrow = pygame.transform.scale(pygame.image.load('purpleArrow.png'), (100, 140))
lightGreenArrow = pygame.transform.scale(pygame.image.load('lightGreenArrow.png'), (100, 140))
deepBlueArrow = pygame.transform.scale(pygame.image.load('deepBlueArrow.png'), (100, 140))
aquaArrow = pygame.transform.scale(pygame.image.load('aquaArrow.png'), (100, 140))
pinkArrow = pygame.transform.scale(pygame.image.load('pinkArrow.png'), (100, 140))
gArrow = pygame.transform.scale(pygame.image.load('greenArrow.png'), (100, 140))
bArrow = pygame.transform.scale(pygame.image.load('blueArrow.png'), (100, 140))
whiteArrow = pygame.transform.scale(pygame.image.load('whiteArrow.png'), (100, 140))
grayArrow = pygame.transform.scale(pygame.image.load('grayArrow.png'), (100, 140))
shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
snail = pygame.transform.scale(pygame.image.load('snail.png'), (66, 48))
orange90 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('orangeArrow.png'), (100, 140)), 90)
orange_90 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('orangeArrow.png'), (100, 140)), -90)
portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
gift = pygame.transform.scale(pygame.image.load('gifteo.png'), (60, 60))
doublePoints = pygame.transform.scale(pygame.image.load('2x.png'), (40,40))
endless = pygame.transform.scale(pygame.image.load('endless.png'), (300, 155))
endlessLight = pygame.transform.scale(pygame.image.load('endlessLight.png'), (300, 155))
level = pygame.transform.scale(pygame.image.load('level.png'), (210, 155))
levelLight = pygame.transform.scale(pygame.image.load('levelLight.png'), (210, 155))
levelRed = pygame.transform.scale(pygame.image.load('levelRed.png'), (210, 155))
levelBlue = pygame.transform.scale(pygame.image.load('levelBlue.png'), (210, 155))
levelDarkBlue = pygame.transform.scale(pygame.image.load('levelDarkBlue.png'), (210, 155))
rules = pygame.transform.scale(pygame.image.load('rules.png'), (1280, 720))
invincSound = pygame.mixer.Sound('invincibilitySound.wav')
invincSound.set_volume(0.08)
deathSound = pygame.mixer.Sound('deathSound.wav')
deathSound.set_volume(0.15)
teleportSound = pygame.mixer.Sound('teleportSound.wav')
teleportSound.set_volume(0.35)
slowDownSound = pygame.mixer.Sound('slowdown.wav')
slowDownSound.set_volume(0.25)
speedUpSound = pygame.mixer.Sound('speedup.wav')
speedUpSound.set_volume(0.25)
powerupSound = pygame.mixer.Sound('powerup.wav')
powerupSound.set_volume(0.15)
doublePointsSound = pygame.mixer.Sound('doublePointsSound.wav')
doublePointsSound.set_volume(0.15)

legendary = pygame.mixer.Sound('legendary.ogg')
legendary.set_volume(0.03)
hope = pygame.mixer.Sound('hope.ogg')
hope.set_volume(0.03)
fire = pygame.mixer.Sound('fire.ogg')
fire.set_volume(0.03)
arrow = pygame.mixer.Sound('arrow.ogg')
arrow.set_volume(0.03)
firefly = pygame.mixer.Sound('firefly.ogg')
firefly.set_volume(0.03)
force = pygame.mixer.Sound('force.ogg')
force.set_volume(0.03)

musicArray = [fire, hope, legendary, arrow, firefly, force]



##landscape = pygame.transform.scale(pygame.image.load('landscape.png'), (1280, 70))

c = bird
frames = 50
def greenMaker(target, current):
    global skyBlue
    global frames
    if frames > 0:
        r = current[0]
        g = current[1]
        b = current[2]
        r1 = target[0]
        g1 = target[1]
        b1 = target[2]
        skyBlue = (r + (r1-r)/frames, g + (g1-g)/frames, b + (b1-b)/frames)
        frames -= 1

def cloudChooser():
    global cloud1
    global cloud2
    global cloud3
    global cloud4
    global cloud5
    global cloud6
    global cloud7
    koko=(random.random()*7)+1
    kaka=int(koko)
    if(kaka==1):
        return cloud1
    if(kaka==2):
        return cloud2
    if(kaka==3):
        return cloud3
    if(kaka==4):
        return cloud4
    if(kaka==5):
        return cloud5
    if(kaka==6):
        return cloud6
    if(kaka==7):
        return cloud7

def cloudGen(cloud,y,slot, startTime,speed):
    global cloud1
    global cloud2
    global cloud3
    global cloud4
    global cloud5
    global cloud6
    global cloud7
    global cslot1
    global cslot2
    global cslot3
    global currentTime
    elt = (currentTime - startTime)/1000
    placeBird(cloud,speed*elt - 500,y)
    if(speed*elt - 500 > dwidth+500):
        if slot == 1:
            cslot1 = True
        elif slot == 2:
            cslot2 = True
        elif slot == 3:
            cslot3 = True



def placeBird(a,x,y):
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global aquaArrow
    global purpleArrow
    global pinkArrow
    global lightGreenArrow
    global deepBlueArrow
    global whiteArrow
    gameDisplay.blit(a, (x,y))

def flapWing(a):
    if a == 1:
        return f1
    elif a == 2:
        return f2
    elif a == 3:
        return f3
    elif a == 4:
        return f4

def flaptWing(a):
    if a == 1:
        return f1t
    elif a == 2:
        return f2t
    elif a == 3:
        return f3t
    elif a == 4:
        return f4t



lastTime = pygame.time.get_ticks()
lastFlip = pygame.time.get_ticks()
flipCooldown = 500
cooldown = 200
flapCooldown = 500

probability = 10

probability2 = 1

probabilityt = 15

x = (dwidth*0.4)
y=(dheight*0.4)

b = 0

c1 = False

diffX = 0
diffY = 0

stage = 1

loc = 0

isSlow = False
usedSlow = False
slowTime = None

isTeleport = False
usedTeleport = False
teleportTime = None
teleportDelay = 0

counter = 0

dead = False

score = 0

def valueSetter(color):
    global redArrow
    global orangeArrow
    global lightGreenArrow
    global deepBlueArrow
    global yellowArrow
    global gArrow
    global bArrow
    global aquaArrow
    global purpleArrow
    global pinkArrow
    global whiteArrow
    global gift
    if color is purpleArrow:
        delay = 2000
        dps = 150
    elif color is deepBlueArrow:
        delay = 1400
        dps = 300
    elif color is lightGreenArrow:
        delay = 1000
        dps = 400
    elif color is aquaArrow:
        delay = 750
        dps = 600
    elif color is redArrow:
        delay = 500
        dps = 800
    elif color is yellowArrow:
        delay = 250
        dps = 950
    elif color is pinkArrow:
        delay = 100
        dps = 1100
    elif color is whiteArrow:
        delay = 0
        dps = 1300
    elif color is grayArrow:
        delay = 1000
        dps = 850
    elif color is gift:
        delay = 0
        dps = 700
    elif color is doublePoints:
        delay = 0
        dps = 700
    return (delay, dps)

def colorChooser(stage):
    r = random.random()*100 + 1
    if stage == 1:
        if r <= 25:
            return purpleArrow
        elif r <= 50:
            return deepBlueArrow
        elif r <= 75:
            return lightGreenArrow
        else:
            return aquaArrow
    elif stage == 2:
        if r <= 15:
            return purpleArrow
        elif r <= 30:
            return deepBlueArrow
        elif r <= 50:
            return lightGreenArrow
        elif r <= 70:
            return aquaArrow
        elif r <= 85:
            return redArrow
        else:
            return yellowArrow
    elif stage == 3:
        if r <= 5:
            return purpleArrow
        elif r <= 10:
            return deepBlueArrow
        elif r <= 20:
            return lightGreenArrow
        elif r <= 35:
            return aquaArrow
        elif r <= 65:
            return redArrow
        elif r <= 85:
            return yellowArrow
        else:
            return pinkArrow
    elif stage == 4:
        if r <= 10:
            return lightGreenArrow
        elif r <= 25:
            return aquaArrow
        elif r <= 50:
            return redArrow
        elif r <= 75:
            return yellowArrow
        elif r <= 95:
            return pinkArrow
        else:
            return grayArrow
    elif stage == 5:
        if r <= 11:
            return aquaArrow
        elif r <= 27:
            return redArrow
        elif r <= 48:
            return yellowArrow
        elif r <= 74:
            return pinkArrow
        elif r <= 95:
            return whiteArrow
        else:
            return grayArrow
    elif stage == 6:
        if r <= 15:
            return redArrow
        elif r <= 31:
            return yellowArrow
        elif r <= 63:
            return pinkArrow
        elif r <= 95:
            return whiteArrow
        else:
            return grayArrow
    elif stage == 7:
        if r <= 26:
            return yellowArrow
        elif r <= 58:
            return pinkArrow
        elif r <= 95:
            return whiteArrow
        else:
            return grayArrow
    else:
        if r <= 42:
            return pinkArrow
        elif r <= 95:
            return whiteArrow
        else:
            return grayArrow


def sideColorChooser(stage):
    r = random.random()*100 + 1
    if stage == 5 or stage == 6:
        if r <= 20:
            return aquaArrow
        elif r <= 40:
            return redArrow
        elif r <= 60:
            return yellowArrow
        elif r <= 80:
            return pinkArrow
        elif r <= 94:
            return grayArrow
        elif r <= 97:
            return gift
        else:
            return doublePoints
    elif stage >= 6:
        if r <= 23:
            return redArrow
        elif r <= 46:
            return yellowArrow
        elif r <= 69:
            return pinkArrow
        elif r <= 92:
            return grayArrow
        elif r <= 96:
            return gift
        else:
            return doublePoints



def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text, n, m, size, font):
    font = pygame.font.SysFont(font, size)
    ##largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((int(dwidth/n)),(int(dheight/m)))
    gameDisplay.blit(TextSurf, TextRect)

def pFinder(slot, x):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10, p11, p12, p13, p14
    if slot == 1:
        p1 = math.floor(x)
        return p1
    if slot == 2:
        p2 = math.floor(x)
        return p2
    if slot == 3:
        p3 = math.floor(x)
        return p3
    if slot == 4:
        p4 = math.floor(x)
        return p4
    if slot == 5:
        p5 = math.floor(x)
        return p5
    if slot == 6:
        p6 = math.floor(x)
        return p6
    if slot == 7:
        p7 = math.floor(x)
        return p7
    if slot == 8:
        p8 = math.floor(x)
        return p8
    if slot == 9:
        p9 = math.floor(x)
        return p9
    if slot == 10:
        p10 = math.floor(x)
        return p10
    if slot == 11:
        p11 = math.floor(x)
        return p11
    if slot == 12:
        p12 = math.floor(x)
        return p12
    if slot == 13:
        p13 = math.floor(x)
        return p13
    if slot == 14:
        p14 = math.floor(x)
        return p14

def pLocator(slot):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10, p11, p12, p13, p14
    if slot == 1:
        return p1
    if slot == 2:
        return p2
    if slot == 3:
        return p3
    if slot == 4:
        return p4
    if slot == 5:
        return p5
    if slot == 6:
        return p6
    if slot == 7:
        return p7
    if slot == 8:
        return p8
    if slot == 9:
        return p9
    if slot == 10:
        return p10
    if slot == 11:
        return p11
    if slot == 12:
        return p12
    if slot == 13:
        return p13
    if slot == 14:
        return p14


def arrowSpawn(color, startTime, location, slot, slow):
    global crashed
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global aquaArrow
    global purpleArrow
    global whiteArrow
    global pinkArrow
    global lightGreenArrow
    global deepBlueArrow
    global gift
    global dheight
    global x
    global y
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global c
    global counter
    global loc
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
    global isInvinc
    global currentTime

    eTime=currentTime-startTime

    if slot == 1:
        (delay, dps) = valueSetter(s1c)
    if slot == 2:
        (delay, dps) = valueSetter(s2c)
    if slot == 3:
        (delay, dps) = valueSetter(s3c)
    if slot == 4:
        (delay, dps) = valueSetter(s4c)
    if slot == 5:
        (delay, dps) = valueSetter(s5c)
    if slot == 6:
        (delay, dps) = valueSetter(s6c)
    if slot == 7:
        (delay, dps) = valueSetter(s7c)
    if slot == 8:
        (delay, dps) = valueSetter(s8c)
    if slot == 9:
        (delay, dps) = valueSetter(s9c)
    if slot == 10:
        (delay, dps) = valueSetter(s10c)

    if slow:
        dps /= 2
    xx = ((eTime-delay*5/4)/100)
    if eTime < delay*5/4:
        loc = copy.deepcopy(x)
    if(color==grayArrow):
        if(eTime < delay/4):
            placeBird(color,x,0)
        elif(eTime>=delay/4 and eTime < delay/2):
            placeBird(orangeArrow,x,0)
        elif(eTime>=delay/2 and eTime < delay*3/4):
            placeBird(color,x,0)
        elif(eTime>=delay*3/4 and eTime < delay):
            placeBird(orangeArrow,x,0)
        elif(eTime<=delay+delay/4):
            placeBird(color,x,0)
        elif(eTime > delay + delay/4) and(eTime<=(delay+delay/4 + 50)):
            pFinder(slot, x)
            placeBird(color,pLocator(slot),((xx**2 + 5*xx)*(dps/100)))
        else:
            placeBird(color, pLocator(slot) ,((xx**2 + 5*xx)*(dps/100)))

    else:

        if(eTime < delay/4):
            placeBird(color,location,0)
        elif(eTime>=delay/4 and eTime < delay/2):
            placeBird(orangeArrow,location,0)
        elif(eTime>=delay/2 and eTime < delay*3/4):
            placeBird(color,location,0)
        elif(eTime>=delay*3/4 and eTime < delay):
            placeBird(orangeArrow,location,0)
        elif(eTime<=delay+delay/4):
            placeBird(color,location,0)
        elif(eTime > delay + delay/4):
            placeBird(color,location,((xx**2 + 5*xx)*(dps/100)))


##    if color is grayArrow:
##        if abs(x - loc) < 150:
##            if abs(y - xx) < 140:
##                rect1 = c.get_rect()
##                rect1.inflate(-30, -30)
##                rect1.center = (x,y)
##                rect6 = color.get_rect()
##                rect6.inflate(-50, -30)
##                rect6.center = (loc ,(xx**2 + 5*xx)*(dps/100))
##                if (rect6.colliderect(rect1)):
##                    if counter > 0:
##                        print("crappus")
##                        counter -= 1
##                    elif counter <= 0:
##                        pygame.quit()
##                        quit()
##
##    else:
##        if abs(x - loc) < 150:
##            if abs(y - xx) < 140:
##                rect1 = c.get_rect()
##                rect1.inflate(-30, -30)
##                rect1.center = (x,y)
##                rect6 = color.get_rect()
##                rect6.inflate(-50, -30)
##                rect6.center = (location ,(xx**2 + 5*xx)*(dps/100))
##                if (rect6.colliderect(rect1)):
##                    if counter > 0:
##                        print("crappus")
##                        counter -= 1
##                    elif counter <= 0:
##                        pygame.quit()
##                        quit()


    if ((xx**2 + 5*xx)*(dps/100)) > dheight + 100:
        if slot == 1:
            slot1 = True
        if slot == 2:
            slot2 = True
        if slot == 3:
            slot3 = True
        if slot == 4:
            slot4 = True
        if slot == 5:
            slot5 = True
        if slot == 6:
            slot6 = True
        if slot == 7:
            slot7 = True
        if slot == 8:
            slot8 = True
        if slot == 9:
            slot9 = True
        if slot == 10:
            slot10 = True




    rect1 = copy.deepcopy(c.get_rect())
    rect1.inflate_ip(-90, -130)
    rect1.center = (x + 75,y + 80)

    rect6 = copy.deepcopy(color.get_rect())
    rect6.inflate_ip(-90, -70)
    if color is grayArrow:
        if eTime <= delay*5/4:
            rect6.center = (x + 51.5, 60)
        else:
            rect6.center = (pLocator(slot) + 51.5 ,(xx**2 + 5*xx)*(dps/100) + 60)
    else:
        if eTime <= delay*5/4:
            rect6.center = (location + 51.5, 60)
        else:
            rect6.center = (location + 51.5, (xx**2 + 5*xx)*(dps/100) + 60)
##    pygame.draw.rect(gameDisplay, (0,0,0),rect1)
##    pygame.draw.rect(gameDisplay, (0,0,0),rect6)
    ##print(rect1, rect6, sep=', ')


    if not isInvinc:
        if (rect6.colliderect(rect1)):
            if counter > 0:
                print("crappus")
                print(rect1, rect6, sep=', ')
                counter -= 1
            elif counter <= 0:
                crashed = True
                pygame.mixer.Channel(4).play(deathSound)

def sideArrowSpawn(color, startTime, location, slot, slow, side):
    global crashed
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global aquaArrow
    global purpleArrow
    global whiteArrow
    global pinkArrow
    global lightGreenArrow
    global deepBlueArrow
    global dheight
    global x
    global y
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global c
    global counter
    global loc
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10, p11, p12, p13, p14
    global isInvinc
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t
    global usedSlow, usedInvinc, usedTeleport
    global isDouble, doubleTime

    eTime=currentTime-startTime
    if slot == 1:
        (delay, dps) = valueSetter(s1c)
    if slot == 2:
        (delay, dps) = valueSetter(s2c)
    if slot == 3:
        (delay, dps) = valueSetter(s3c)
    if slot == 4:
        (delay, dps) = valueSetter(s4c)
    if slot == 5:
        (delay, dps) = valueSetter(s5c)
    if slot == 6:
        (delay, dps) = valueSetter(s6c)
    if slot == 7:
        (delay, dps) = valueSetter(s7c)
    if slot == 8:
        (delay, dps) = valueSetter(s8c)
    if slot == 9:
        (delay, dps) = valueSetter(s9c)
    if slot == 10:
        (delay, dps) = valueSetter(s10c)
    if slot == 11:
        (delay, dps) = valueSetter(s11c)
    if slot == 12:
        (delay, dps) = valueSetter(s12c)
    if slot == 13:
        (delay, dps) = valueSetter(s13c)
    if slot == 14:
        (delay, dps) = valueSetter(s14c)

    if slow:
        dps /= 2
    xx = ((eTime-delay*5/4)/100)
    if side == 1:
        if color is gift or color is doublePoints:
            color2 = color
        elif eTime > delay*5/4:
            color2 = pygame.transform.rotate(color, int(90 -  (eTime -delay*5/4)/(dps**2/4250)))
        else:
            color2 = pygame.transform.rotate(color, 90)
        if(color==grayArrow):
            if(eTime < delay/4):
                placeBird(color2,0,y)
            elif(eTime>=delay/4 and eTime < delay/2):
                placeBird(orange90,0,y)
            elif(eTime>=delay/2 and eTime < delay*3/4):
                placeBird(color2,0,y)
            elif(eTime>=delay*3/4 and eTime < delay):
                placeBird(orange90,0,y)
            elif(eTime<=delay+delay/4):
                placeBird(color2,0,y)
            elif(eTime > delay + delay/4) and(eTime<=(delay+delay/4 + 50)):
                pFinder(slot, y)
                placeBird(color2,((eTime - delay*5/4)*dps/1000 * 3/2),pLocator(slot) + (eTime-delay*5/4)**2/(15*dps))
            else:
                placeBird(color2,((eTime - delay*5/4)*dps/1000 * 3/2),pLocator(slot) + (eTime-delay*5/4)**2/(15*dps))

        else:

            if(eTime < delay/4):
                placeBird(color2,0,location)
            elif(eTime>=delay/4 and eTime < delay/2):
                placeBird(orange90,0,location)
            elif(eTime>=delay/2 and eTime < delay*3/4):
                placeBird(color2,0,location)
            elif(eTime>=delay*3/4 and eTime < delay):
                placeBird(orange90,0,location)
            elif(eTime<=delay+delay/4):
                placeBird(color2,0,location)
            elif(eTime > delay + delay/4):
                placeBird(color2,((eTime - delay*5/4)*dps/1000 * 3/2),location + (eTime-delay*5/4)**2/(15*dps))
    if side == 2:
        if color is gift or color is doublePoints:
            color2 = color
        elif eTime > delay*5/4:
            color2 = pygame.transform.rotate(color, int(-90 +  (eTime -delay*5/4)/(dps**2/4250)))
        else:
            color2 = pygame.transform.rotate(color, -90)
        if(color==grayArrow):
            if(eTime < delay/4):
                placeBird(color2,1140,y)
            elif(eTime>=delay/4 and eTime < delay/2):
                placeBird(orange_90,1140,y)
            elif(eTime>=delay/2 and eTime < delay*3/4):
                placeBird(color2,1140,y)
            elif(eTime>=delay*3/4 and eTime < delay):
                placeBird(orange_90,1140,y)
            elif(eTime<=delay+delay/4):
                placeBird(color2,1140,y)
            elif(eTime > delay + delay/4) and(eTime<=(delay+delay/4 + 50)):
                pFinder(slot, y)
                placeBird(color2,1140 - ((eTime - delay*5/4)*dps/1000 * 3/2),pLocator(slot) + (eTime-delay*5/4)**2/(15*dps))
            else:
                placeBird(color2,1140 - ((eTime - delay*5/4)*dps/1000 * 3/2),pLocator(slot) + (eTime-delay*5/4)**2/(15*dps))

        else:

            if(eTime < delay/4):
                placeBird(color2,1140,location)
            elif(eTime>=delay/4 and eTime < delay/2):
                placeBird(orange_90,1140,location)
            elif(eTime>=delay/2 and eTime < delay*3/4):
                placeBird(color2,1140,location)
            elif(eTime>=delay*3/4 and eTime < delay):
                placeBird(orange_90,1140,location)
            elif(eTime<=delay+delay/4):
                placeBird(color2,1140,location)
            elif(eTime > delay + delay/4):
                placeBird(color2,1140 - ((eTime - delay*5/4)*dps/1000 * 3/2),location + (eTime-delay*5/4)**2/(15*dps))
##    if eTime < delay*5/4:
##        loc = copy.deepcopy(x)
##    if(color==grayArrow):
##        if(eTime < delay/4):
##            placeBird(color,x,0)
##        elif(eTime>=delay/4 and eTime < delay/2):
##            placeBird(orangeArrow,x,0)
##        elif(eTime>=delay/2 and eTime < delay*3/4):
##            placeBird(color,x,0)
##        elif(eTime>=delay*3/4 and eTime < delay):
##            placeBird(orangeArrow,x,0)
##        elif(eTime<=delay+delay/4):
##            placeBird(color,x,0)
##        elif(eTime > delay + delay/4) and(eTime<=(delay+delay/4 + 50)):
##            pFinder(slot, x)
##            placeBird(color,pLocator(slot),((xx**2 + 5*xx)*(dps/100)))
##        else:
##            placeBird(color, pLocator(slot) ,((xx**2 + 5*xx)*(dps/100)))
##
##    else:
##
##        if(eTime < delay/4):
##            placeBird(color,location,0)
##        elif(eTime>=delay/4 and eTime < delay/2):
##            placeBird(orangeArrow,location,0)
##        elif(eTime>=delay/2 and eTime < delay*3/4):
##            placeBird(color,location,0)
##        elif(eTime>=delay*3/4 and eTime < delay):
##            placeBird(orangeArrow,location,0)
##        elif(eTime<=delay+delay/4):
##            placeBird(color,location,0)
##        elif(eTime > delay + delay/4):
##            placeBird(color,location,((xx**2 + 5*xx)*(dps/100)))


##    if color is grayArrow:
##        if abs(x - loc) < 150:
##            if abs(y - xx) < 140:
##                rect1 = c.get_rect()
##                rect1.inflate(-30, -30)
##                rect1.center = (x,y)
##                rect6 = color.get_rect()
##                rect6.inflate(-50, -30)
##                rect6.center = (loc ,(xx**2 + 5*xx)*(dps/100))
##                if (rect6.colliderect(rect1)):
##                    if counter > 0:
##                        print("crappus")
##                        counter -= 1
##                    elif counter <= 0:
##                        pygame.quit()
##                        quit()
##
##    else:
##        if abs(x - loc) < 150:
##            if abs(y - xx) < 140:
##                rect1 = c.get_rect()
##                rect1.inflate(-30, -30)
##                rect1.center = (x,y)
##                rect6 = color.get_rect()
##                rect6.inflate(-50, -30)
##                rect6.center = (location ,(xx**2 + 5*xx)*(dps/100))
##                if (rect6.colliderect(rect1)):
##                    if counter > 0:
##                        print("crappus")
##                        counter -= 1
##                    elif counter <= 0:
##                        pygame.quit()
##                        quit()


    if side == 1:
        if ((eTime - delay*5/4)*dps/1000 * 3/2) > dwidth + 100 or (eTime-delay*5/4)**2/(15*dps) > dheight + 100:
            if slot == 11:
                slot11 = True
            if slot == 12:
                slot12 = True
            if slot == 13:
                slot13 = True
            if slot == 14:
                slot14 = True
        if color is gift:
            rect6 = copy.deepcopy(color2.get_rect())
            rect6.inflate_ip(-15, -15)
            rect6.center = ((eTime - delay*5/4)*dps/1000 * 3/2 + 30, location + (eTime-delay*5/4)**2/(15*dps) + 30)
        elif color is doublePoints:
            rect6 = copy.deepcopy(color2.get_rect())
            rect6.center = ((eTime - delay*5/4)*dps/1000 * 3/2 + 20, location + (eTime-delay*5/4)**2/(15*dps) + 20)
        else:
            rect6 = copy.deepcopy(color2.get_rect())
            rect6.inflate_ip(-70, -90)
            if color is grayArrow:
                if eTime <= delay*5/4:
                    rect6.center = (75, y+51.5)
                else:
                    rect6.center = ((eTime - delay*5/4)*dps/1000 * 3/2 + 60, pLocator(slot) + (eTime-delay*5/4)**2/(15*dps) + 51.5)
            else:
                if eTime <= delay*5/4:
                    rect6.center = (75, location + 51.5)
                else:
                    rect6.center = ((eTime - delay*5/4)*dps/1000 * 3/2 + 60, location + (eTime-delay*5/4)**2/(15*dps) + 51.5)

    else:
        if 1140 - ((eTime - delay*5/4)*dps/1000 * 3/2) <  -240 or (eTime-delay*5/4)**2/(15*dps) > dheight + 100:
            if slot == 11:
                slot11 = True
            if slot == 12:
                slot12 = True
            if slot == 13:
                slot13 = True
            if slot == 14:
                slot14 = True
        if color is gift:
            rect6 = copy.deepcopy(color2.get_rect())
            rect6.inflate_ip(-15, -15)
            rect6.center = ((1140 - (eTime - delay*5/4)*dps/1000 * 3/2) + 30,(location + (eTime-delay*5/4)**2/(15*dps) + 30))
        elif color is doublePoints:
            rect6 = copy.deepcopy(color2.get_rect())
            rect6.center = ((1140 - (eTime - delay*5/4)*dps/1000 * 3/2) + 20,(location + (eTime-delay*5/4)**2/(15*dps) + 20))
        else:
            rect6 = copy.deepcopy(color2.get_rect())
            rect6.inflate_ip(-70, -90)
            if color is grayArrow:
                if eTime <= delay*5/4:
                    rect6.center = (1220, y+51.5)
                else:
                    rect6.center = ((1140 - (eTime - delay*5/4)*dps/1000 * 3/2) + 80,(pLocator(slot) + (eTime-delay*5/4)**2/(15*dps) + 51.5))
            else:
                if eTime <= delay*5/4:
                    rect6.center = (1220, location+51.5)
                else:
                    rect6.center = ((1140 - (eTime - delay*5/4)*dps/1000 * 3/2) + 80,(location + (eTime-delay*5/4)**2/(15*dps) + 51.5))




    rect1 = copy.deepcopy(c.get_rect())
    rect1.inflate_ip(-90, -130)
    rect1.center = (x + 75,y + 80)

##    rect6 = copy.deepcopy(color.get_rect())
##    rect6.inflate_ip(-70, -70)
##    if color is grayArrow:
##        if eTime <= delay*5/4:
##            rect6.center = (x + 50, 60)
##        else:
##            rect6.center = (pLocator(slot) + 50 ,(xx**2 + 5*xx)*(dps/100) + 60)
##    else:
##        if eTime <= delay*5/4:
##            rect6.center = (location + 50, 60)
##        else:
##            rect6.center = (location + 50, (xx**2 + 5*xx)*(dps/100) + 60)
##    pygame.draw.rect(gameDisplay, (0,0,0),rect1)
##    pygame.draw.rect(gameDisplay, (0,0,0),rect6)
    ##print(rect1, rect6, sep=', ')


    if color is gift:
        if (rect6.colliderect(rect1)):
            if counter > 0:
                print("crappus")
                print(rect1, rect6, sep=', ')
                counter -= 1
            elif counter <= 0:
                if not isInvinc:
                    usedInvinc = False
                if not isTeleport:
                    usedTeleport = False
                if not isSlow:
                    usedSlow = False
                pygame.mixer.Channel(5).play(powerupSound)
                if slot == 11:
                    slot11 = True
                elif slot == 12:
                    slot12 = True
                elif slot == 13:
                    slot13 = True
                elif slot == 14:
                    slot14 = True
    elif color is doublePoints:
         if (rect6.colliderect(rect1)):
            if counter > 0:
                print("crappus")
                print(rect1, rect6, sep=', ')
                counter -= 1
            elif counter <= 0:
                isDouble = True
                doubleTime = currentTime
                pygame.mixer.Channel(6).play(doublePointsSound)
                if slot == 11:
                    slot11 = True
                elif slot == 12:
                    slot12 = True
                elif slot == 13:
                    slot13 = True
                elif slot == 14:
                    slot14 = True

    else:
        if not isInvinc:
            if (rect6.colliderect(rect1)):
                if counter > 0:
                    print("crappus")
                    print(rect1, rect6, sep=', ')
                    counter -= 1
                elif counter <= 0:
                    crashed = True
                    pygame.mixer.Channel(4).play(deathSound)




def titleLoop():
    global c1
    global skyBlue
    global gameDisplay
    global bArrow
    global redArrow
    global orangeArrow
    global gArrow
    global whiteArrow
    global aquaArrow
    global pinkArrow
    global purpleArrow
    global yellowArrow
    global lightGreenArrow
    global deepBlueArrow
    global musicArray
    skyBlue = (88, 173, 245)
    while not c1:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
##            pygame.mixer.music.load(musicArray[int(random.random()*len(musicArray))] + '.mp3')
##            pygame.mixer.music.set_volume(0.05)
##            pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                c1 = True
        gameDisplay.fill(skyBlue)
        placeBird(redArrow, 605, 218)
        message_display("Arrows", 2, 2.2, 180, "franklingothicdemicond")
        message_display("click to start", 2, 1.5, 50, "georgia")
        pygame.display.update()
        z = 2000*98*456
        clock.tick(60)

usedSlowSound = False
bonus = 0
def gameLoop():
    global score
    global crashed
    global x
    global y
    global b
    global flipStatus
    global bird
    global birdt
    global skyBlue
    global f1
    global f1t
    global f2
    global f2t
    global f3
    global f3t
    global f4
    global f4t
    global flipCooldown
    global lastFlip
    global cooldown
    global flapCooldown
    global lastTime
    global dwidth
    global dheight
    global diffX
    global diffY
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global whiteArrow
    global aquaArrow
    global lightGreenArrow
    global deepBlueArrow
    global purpleArrow
    global pinkArrow
    global gift
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global stage
    global firstTime
    global probability
    global c
    global isDouble, doubleTime
    global dead
    global isInvinc
    global usedInvinc
    global invincTime
    global c1c, c1y, cslot1, c1t, c1s,c2c, c2y, cslot2, c2t, c2s,c3c, c3y, cslot3, c3t, c3s
    global isSlow
    global usedSlow
    global slowTime
    global isTeleport, usedTeleport, teleportTime
    global s1s, s2s,s3s,s4s,s5s,s6s,s7s,s8s,s9s,s10s
    global frames
    global portal
    global currentTime, teleportDelay
    global usedSlowSound
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t, s11s, s12s, s13s, s14s, s11sd, s12sd, s13sd, s14sd
    global bonus
    shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
    snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
    portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
    currentTime = pygame.time.get_ticks()
    firstTime = pygame.time.get_ticks()
    slot1 = True
    s1x = 0
    slt = None
    s1c = None
    slot2 = True
    s2x = 0
    s2t = None
    s2c = None
    slot3 = True
    s3x = 0
    s3t = None
    s3c = None
    slot4 = True
    s4x = 0
    s4t = None
    s4c = None
    slot5 = True
    s5x = 0
    s5t = None
    s5c = None
    slot6 = True
    s6x = 0
    s6t = None
    s6c = None
    slot7 = True
    s7x = 0
    s7t = None
    s7c = None
    slot8 = True
    s8x = 0
    s8t = None
    s8c = None
    slot9 = True
    s9x = 0
    s9t = None
    s9c = None
    slot10 = True
    s10x = 0
    s10t = None
    s10c = None
    cslot1 = True
    c1y = 0
    c1t = None
    c1c = None
    c1s = None
    cslot2 = True
    c2y = 0
    c2t = None
    c2c = None
    c2s = None
    cslot3 = True
    c3y = 0
    c3t = None
    c3c = None
    c3s = None
    s1s = False
    s2s = False
    s3s = False
    s4s = False
    s5s = False
    s6s = False
    s7s = False
    s8s = False
    s9s = False
    s10s = False
    s11s = False
    s12s = False
    s13s = False
    s14s = False
    slot11 = True
    s11y = 0
    sllt = None
    s11c = None
    slot12 = True
    s12y = 0
    sl2t = None
    s12c = None
    slot13 = True
    s13y = 0
    sl3t = None
    s13c = None
    slot14 = True
    s14y = 0
    sl4t = None
    s14c = None
    s11sd = None
    s12sd = None
    s13sd = None
    s14sd = None
    isInvinc = False
    usedInvinc = False
    invincTime = None
    isSlow = False
    usedSlow = False
    slowTime = None
    isTeleport = False
    usedTeleport = False
    teleportTime = None
    teleportDelay = 0
    frames = 50
    skyBlue = (88, 173, 245)
    isDouble = False
    doubleTime = 0
    bonus = 0
    while not crashed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
##            pygame.mixer.music.load(musicArray[int(random.random()*len(musicArray))] + '.ogg')
##            pygame.mixer.music.set_volume(0.03)
##            pygame.mixer.music.play()
        currentTime = pygame.time.get_ticks() - teleportDelay
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and usedInvinc == False and isInvinc == False:
                pygame.mixer.Channel(0).play(invincSound)
                isInvinc = True
                invincTime = currentTime
                shield = pygame.transform.scale(shield, (60, 60))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and usedSlow == False and isSlow == False or event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and usedSlow == False and isSlow == False:
                pygame.mixer.Channel(1).play(slowDownSound)
                usedSlowSound = False
                isSlow = True
                slowTime = currentTime
                snail = pygame.transform.scale(snail, (94, 68))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and usedTeleport == False and isTeleport == False:
                isTeleport = True
                teleportTime = currentTime
                portal = pygame.transform.scale(portal, (90, 90))
                placeBird(portal, 18, dheight - 285)
                pygame.display.update()
                while isTeleport:
                    if pygame.time.get_ticks() - teleportTime >= 5000:
                        isTeleport = False
                        usedTeleport = True
                        teleportDelay += 5000
                        portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pygame.mixer.Channel(2).play(teleportSound)
                            x = pygame.mouse.get_pos()[0] - 75
                            y = pygame.mouse.get_pos()[1] - 75
                            isTeleport = False
                            usedTeleport = True
                            portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                            teleportDelay += (pygame.time.get_ticks() - teleportDelay - teleportTime)
                    clock.tick(60)


            ##print(event)

            ##if event.type == pygame.MOUSEMOTION:
        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
                    ##x = pygame.mouse.get_pos()[0] - 75
                    ##y = pygame.mouse.get_pos()[1] - 75
            diffX = (pygame.mouse.get_pos()[0] - 75) - x
            diffY = (pygame.mouse.get_pos()[1] - 75) - y
            x += 6/fps*diffX
            y += 6/fps*diffY

        if isInvinc:
            if currentTime - invincTime >= 4500 and currentTime - invincTime <= 5000:
                usedInvinc = True
            elif currentTime - invincTime <= 5500:
                usedInvinc = False
            elif currentTime - invincTime <= 6000:
                usedInvinc = True
            elif currentTime - invincTime <= 6250:
                usedInvinc = False
            elif currentTime - invincTime <= 6500:
                usedInvinc = True
            elif currentTime - invincTime <= 6750:
                usedInvinc = False
            elif currentTime - invincTime <= 7000:
                usedInvinc = True
            if currentTime - invincTime >= 7000:
                shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
                invincTime = 0
                isInvinc = False
                usedInvinc = True
        if isSlow:
            if frames > 0 and currentTime - slowTime <= 1000:
                greenMaker((0, 194, 103), skyBlue)
            if currentTime - slowTime >= 9500 and currentTime - slowTime <= 10000:
                usedSlow = True
            elif currentTime - slowTime <= 10500:
                usedSlow = False
            elif currentTime - slowTime <= 11000:
                usedSlow = True
                frames = 50
            elif currentTime - slowTime <= 11250:
                usedSlow = False
            elif currentTime - slowTime <= 11500:
                usedSlow = True
            elif currentTime - slowTime <= 11750:
                usedSlow = False
            elif currentTime - slowTime <= 12000:
                usedSlow = True
            if currentTime - slowTime >= 12000:
                snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
                slowTime = 0
                isSlow = False
                usedSlow = True
                frames = 50
        if isSlow and currentTime - slowTime >= 12000 - 1200*(frames/100):
            greenMaker((88, 173, 245), skyBlue)
        if isSlow and currentTime - slowTime >= 10950 and not usedSlowSound :
            pygame.mixer.Channel(3).play(speedUpSound)
            usedSlowSound = True
        if not isInvinc:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = False
        else:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = False


        gameDisplay.fill(skyBlue)
##        placeBird(landscape, 0, 650)

        momo = int((random.random())*1000 + 1)
        if momo <= probability2:
            if(cslot1):
                c1t=currentTime
                c1c = cloudChooser()
                c1s = random.random()*80 + 120
                c1y = random.random()* 70 + 60
                cslot1 = False
                cloudGen(c1c, c1y, 1, c1t, c1s)
            elif(cslot2):
                c2t=currentTime
                c2c = cloudChooser()
                c2s = random.random()*80 + 80
                c2y = random.random()* 70 + 40
                cslot2 = False
                cloudGen(c2c, c2y, 2, c2t, c2s)
            if(cslot3):
                c3t=currentTime
                c3c = cloudChooser()
                c3s = random.random()*80 + 40
                c3y = random.random()* 70 + 20
                cslot3 = False
                cloudGen(c3c, c3y, 3, c3t, c3s)

        if not cslot1:
            cloudGen(c1c, c1y, 1, c1t, c1s)
        if not cslot2:
            cloudGen(c2c, c2y, 2, c2t, c2s)
        if not cslot3:
            cloudGen(c3c, c3y, 3, c3t, c3s)

        if not usedInvinc:
            if not isInvinc:
                placeBird(shield, 35, dheight - 130)
            else:
                placeBird(shield, 30, dheight - 135)

        if not usedSlow:
            if not isSlow:
                placeBird(snail, 23, dheight - 195)
            else:
                placeBird(snail, 17, dheight - 200)

        if not usedTeleport:
            placeBird(portal, 28, dheight - 275)



        if not isInvinc:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flapWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flapWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flapWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flapWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(bird, x,y)
                    c = bird
            else:
                placeBird(bird, x,y)
        else:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flaptWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flaptWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flaptWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flaptWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(birdt, x,y)
                    c = birdt
            else:
                placeBird(birdt, x,y)




        elTime = (currentTime - firstTime)/1000

        if elTime < 15:
            stage = 1
            probability = 900/fps
        elif elTime < 30:
            stage = 1
            probability = 1200/fps
        elif elTime < 45:
            stage = 2
            probability = 1200/fps
        elif elTime < 60:
            stage = 2
            probability = 1500/fps
        elif elTime < 75:
            stage = 3
            probability = 1500/fps
        elif elTime < 90:
            stage = 3
            probability  = 1800/fps
        elif elTime < 120:
            stage = 4
            probability = 1800/fps
        elif elTime < 140:
            stage = 5
            probability = 1800/fps
            probabilityt = 300/fps
        elif elTime < 160:
            stage = 5
            probability = 2100/fps
            probabilityt = 400/fps
        elif elTime < 180:
            stage = 5
            probability = 2400/fps
            probabilityt = 480/fps
        elif elTime < 200:
            stage = 6
            probability = 2100/fps
            probabilityt = 450/fps
        elif elTime < 220:
            stage = 6
            probability = 2400/fps
            probabilityt = 500/fps
        elif elTime < 240:
            stage = 6
            probability = 2700/fps
            probabilityt = 600/fps
        elif elTime < 260:
            stage = 7
            probability = 2400/fps
            probabilityt = 600/fps
        elif elTime < 280:
            stage = 7
            probability = 2700/fps
            probabilityt = 675/fps
        elif elTime < 300:
            stage = 7
            probability = 3000/fps
            probabilityt = 750/fps
        elif elTime < 330:
            stage = 8
            probability = 2700/fps
            probabilityt = 675/fps
        elif elTime < 360:
            stage = 8
            probability = 3200/fps
            probabilityt = 800/fps
        elif elTime < 390:
            stage = 8
            probability = 3700/fps
            probabilityt = 1000/fps
        elif elTime < 420:
            stage = 9
            probability = 3500/fps
            probabilityt = 1000/fps
        elif elTime < 450:
            stage = 9
            probability = 4200/fps
            probabilityt = 1350/fps
        elif elTime < 480:
            stage = 9
            probability = 4900/fps
            probabilityt = 1600/fps
        else:
            stage = 9
            probability = 4900/fps + (elTime - 480)/5
            probabilityt = 1600/fps + (elTime - 540)/15



        r = int((random.random())*1000 + 1)
        if r <= probability:
            if slot1:
                s1t = currentTime
                s1c = colorChooser(stage)
                s1x = int((random.random())*1280 + 1)
                s1s = isSlow
                arrowSpawn(s1c, s1t, s1x, 1, s1s)
                slot1 = False
            elif slot2:
                s2t = currentTime
                s2x = int((random.random())*1280 + 1)
                s2c = colorChooser(stage)
                s2s = isSlow
                arrowSpawn(s2c, s2t, s2x, 2, s2s)
                slot2 = False
            elif slot3:
                s3t = currentTime
                s3x = int((random.random())*1280 + 1)
                s3c = colorChooser(stage)
                s3s = isSlow
                arrowSpawn(s3c, s3t, s3x, 3, s3s)
                slot3 = False
            elif slot4:
                s4t = currentTime
                s4x = int((random.random())*1280 + 1)
                s4c = colorChooser(stage)
                s4s = isSlow
                arrowSpawn(s4c, s4t, s4x, 4, s4s)
                slot4 = False
            elif slot5:
                s5t = currentTime
                s5x = int((random.random())*1280 + 1)
                s5c = colorChooser(stage)
                s5s = isSlow
                arrowSpawn(s5c, s5t, s5x, 5, s5s)
                slot5 = False
            elif slot6:
                s6t = currentTime
                s6x = int((random.random())*1280 + 1)
                s6c = colorChooser(stage)
                s6s = isSlow
                arrowSpawn(s6c, s6t, s6x, 6, s6s)
                slot6 = False
            elif slot7:
                s7t = currentTime
                s7x = int((random.random())*1280 + 1)
                s7c = colorChooser(stage)
                s7s = isSlow
                arrowSpawn(s7c, s7t, s7x, 7, s7s)
                slot7 = False
            elif slot8:
                s8t = currentTime
                s8x = int((random.random())*1280 + 1)
                s8c = colorChooser(stage)
                s8s = isSlow
                arrowSpawn(s8c, s8t, s8x, 8, s8s)
                slot8 = False
            elif slot9:
                s9t = currentTime
                s9x = int((random.random())*1280 + 1)
                s9c = colorChooser(stage)
                s9s = isSlow
                arrowSpawn(s9c, s9t, s9x, 9, s9s)
                slot9 = False
            elif slot10:
                s10t = currentTime
                s10x = int((random.random())*1280 + 1)
                s10c = colorChooser(stage)
                s10s = isSlow
                arrowSpawn(s10c, s10t, s10x, 10, s10s)
                slot10 = False
        if stage >= 5:
            rn = int((random.random())*1000 + 1)
            if rn <= probabilityt:
                if slot11:
                    s11t = currentTime
                    s11c = sideColorChooser(stage)
                    s11y = int((random.random())*600 + 1)
                    s11s = isSlow
                    s11sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
                    slot11 = False
                elif slot12:
                    s12t = currentTime
                    s12y = int((random.random())*600 + 1)
                    s12c = sideColorChooser(stage)
                    s12s = isSlow
                    s12sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
                    slot12 = False
                elif slot13:
                    s13t = currentTime
                    s13y = int((random.random())*600 + 1)
                    s13c = sideColorChooser(stage)
                    s13s = isSlow
                    s13sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
                    slot13 = False
                elif slot14:
                    s14t = currentTime
                    s14y = int((random.random())*600 + 1)
                    s14c = sideColorChooser(stage)
                    s14s = isSlow
                    s14sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)
                    slot14 = False

        if not slot1:
            arrowSpawn(s1c, s1t, s1x, 1, s1s)
        if not slot2:
            arrowSpawn(s2c, s2t, s2x, 2, s2s)
        if not slot3:
            arrowSpawn(s3c, s3t, s3x, 3, s3s)
        if not slot4:
            arrowSpawn(s4c, s4t, s4x, 4, s4s)
        if not slot5:
            arrowSpawn(s5c, s5t, s5x, 5, s5s)
        if not slot6:
            arrowSpawn(s6c, s6t, s6x, 6, s6s)
        if not slot7:
            arrowSpawn(s7c, s7t, s7x, 7, s7s)
        if not slot8:
            arrowSpawn(s8c, s8t, s8x, 8, s8s)
        if not slot9:
            arrowSpawn(s9c, s9t, s9x, 9, s9s)
        if not slot10:
            arrowSpawn(s10c, s10t, s10x, 10, s10s)
        if not slot11:
            sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
        if not slot12:
            sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
        if not slot13:
            sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
        if not slot14:
            sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)

        if isDouble:
            placeBird(doublePoints, 120, dheight - 55)
            bonus += ((elTime * 1.005**elTime) - ((elTime - 1) * 1.005**(elTime - 1)))/fps
            if currentTime - doubleTime >= 20000:
                isDouble = False

        score = round(elTime * 1.005**elTime + bonus)
        message_display("Score: " + str(score), 16, 1.05, 30, "franklingothicdemicond")





        pygame.display.update()
        clock.tick()
##        if round(currentTime - firstTime) % 5000 > 0 and round(currentTime - firstTime) % 5000 < 100:
##            print(clock.get_fps())

    dead = True
    deathLoop()

def levelOne():
    global score
    global crashed
    global x
    global y
    global b
    global flipStatus
    global bird
    global birdt
    global skyBlue
    global f1
    global f1t
    global f2
    global f2t
    global f3
    global f3t
    global f4
    global f4t
    global flipCooldown
    global lastFlip
    global cooldown
    global flapCooldown
    global lastTime
    global dwidth
    global dheight
    global diffX
    global diffY
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global whiteArrow
    global aquaArrow
    global lightGreenArrow
    global deepBlueArrow
    global purpleArrow
    global pinkArrow
    global gift
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global stage
    global firstTime
    global probability
    global c
    global isDouble, doubleTime
    global dead
    global isInvinc
    global usedInvinc
    global invincTime
    global c1c, c1y, cslot1, c1t, c1s,c2c, c2y, cslot2, c2t, c2s,c3c, c3y, cslot3, c3t, c3s
    global isSlow
    global usedSlow
    global slowTime
    global isTeleport, usedTeleport, teleportTime
    global s1s, s2s,s3s,s4s,s5s,s6s,s7s,s8s,s9s,s10s
    global frames
    global portal
    global currentTime, teleportDelay
    global usedSlowSound
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t, s11s, s12s, s13s, s14s, s11sd, s12sd, s13sd, s14sd
    global bonus
    global passed, levelUnlocked
    shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
    snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
    portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
    currentTime = pygame.time.get_ticks()
    firstTime = pygame.time.get_ticks()
    slot1 = True
    s1x = 0
    slt = None
    s1c = None
    slot2 = True
    s2x = 0
    s2t = None
    s2c = None
    slot3 = True
    s3x = 0
    s3t = None
    s3c = None
    slot4 = True
    s4x = 0
    s4t = None
    s4c = None
    slot5 = True
    s5x = 0
    s5t = None
    s5c = None
    slot6 = True
    s6x = 0
    s6t = None
    s6c = None
    slot7 = True
    s7x = 0
    s7t = None
    s7c = None
    slot8 = True
    s8x = 0
    s8t = None
    s8c = None
    slot9 = True
    s9x = 0
    s9t = None
    s9c = None
    slot10 = True
    s10x = 0
    s10t = None
    s10c = None
    cslot1 = True
    c1y = 0
    c1t = None
    c1c = None
    c1s = None
    cslot2 = True
    c2y = 0
    c2t = None
    c2c = None
    c2s = None
    cslot3 = True
    c3y = 0
    c3t = None
    c3c = None
    c3s = None
    s1s = False
    s2s = False
    s3s = False
    s4s = False
    s5s = False
    s6s = False
    s7s = False
    s8s = False
    s9s = False
    s10s = False
    s11s = False
    s12s = False
    s13s = False
    s14s = False
    slot11 = True
    s11y = 0
    sllt = None
    s11c = None
    slot12 = True
    s12y = 0
    sl2t = None
    s12c = None
    slot13 = True
    s13y = 0
    sl3t = None
    s13c = None
    slot14 = True
    s14y = 0
    sl4t = None
    s14c = None
    s11sd = None
    s12sd = None
    s13sd = None
    s14sd = None
    isInvinc = False
    usedInvinc = True
    invincTime = None
    isSlow = False
    usedSlow = True
    slowTime = None
    isTeleport = False
    usedTeleport = True
    teleportTime = None
    teleportDelay = 0
    frames = 50
    skyBlue = (88, 173, 245)
    isDouble = False
    doubleTime = 0
    bonus = 0
    while not crashed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        currentTime = pygame.time.get_ticks() - teleportDelay
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and usedInvinc == False and isInvinc == False:
                pygame.mixer.Channel(0).play(invincSound)
                isInvinc = True
                invincTime = currentTime
                shield = pygame.transform.scale(shield, (60, 60))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and usedSlow == False and isSlow == False or event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and usedSlow == False and isSlow == False:
                pygame.mixer.Channel(1).play(slowDownSound)
                usedSlowSound = False
                isSlow = True
                slowTime = currentTime
                snail = pygame.transform.scale(snail, (94, 68))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and usedTeleport == False and isTeleport == False:
                isTeleport = True
                teleportTime = currentTime
                portal = pygame.transform.scale(portal, (90, 90))
                placeBird(portal, 18, dheight - 285)
                pygame.display.update()
                while isTeleport:
                    if pygame.time.get_ticks() - teleportTime >= 5000:
                        isTeleport = False
                        usedTeleport = True
                        teleportDelay += 5000
                        portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pygame.mixer.Channel(2).play(teleportSound)
                            x = pygame.mouse.get_pos()[0] - 75
                            y = pygame.mouse.get_pos()[1] - 75
                            isTeleport = False
                            usedTeleport = True
                            portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                            teleportDelay += (pygame.time.get_ticks() - teleportDelay - teleportTime)
                    clock.tick(60)


            ##print(event)

            ##if event.type == pygame.MOUSEMOTION:
        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
                    ##x = pygame.mouse.get_pos()[0] - 75
                    ##y = pygame.mouse.get_pos()[1] - 75
            diffX = (pygame.mouse.get_pos()[0] - 75) - x
            diffY = (pygame.mouse.get_pos()[1] - 75) - y
            x += 6/fps*diffX
            y += 6/fps*diffY

        if isInvinc:
            if currentTime - invincTime >= 4500 and currentTime - invincTime <= 5000:
                usedInvinc = True
            elif currentTime - invincTime <= 5500:
                usedInvinc = False
            elif currentTime - invincTime <= 6000:
                usedInvinc = True
            elif currentTime - invincTime <= 6250:
                usedInvinc = False
            elif currentTime - invincTime <= 6500:
                usedInvinc = True
            elif currentTime - invincTime <= 6750:
                usedInvinc = False
            elif currentTime - invincTime <= 7000:
                usedInvinc = True
            if currentTime - invincTime >= 7000:
                shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
                invincTime = 0
                isInvinc = False
                usedInvinc = True
        if isSlow:
            if frames > 0 and currentTime - slowTime <= 1000:
                greenMaker((0, 194, 103), skyBlue)
            if currentTime - slowTime >= 9500 and currentTime - slowTime <= 10000:
                usedSlow = True
            elif currentTime - slowTime <= 10500:
                usedSlow = False
            elif currentTime - slowTime <= 11000:
                usedSlow = True
                frames = 50
            elif currentTime - slowTime <= 11250:
                usedSlow = False
            elif currentTime - slowTime <= 11500:
                usedSlow = True
            elif currentTime - slowTime <= 11750:
                usedSlow = False
            elif currentTime - slowTime <= 12000:
                usedSlow = True
            if currentTime - slowTime >= 12000:
                snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
                slowTime = 0
                isSlow = False
                usedSlow = True
                frames = 50
        if isSlow and currentTime - slowTime >= 12000 - 1200*(frames/100):
            greenMaker((88, 173, 245), skyBlue)
        if isSlow and currentTime - slowTime >= 10950 and not usedSlowSound :
            pygame.mixer.Channel(3).play(speedUpSound)
            usedSlowSound = True
        if not isInvinc:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = False
        else:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = False


        gameDisplay.fill(skyBlue)
##        placeBird(landscape, 0, 650)

        momo = int((random.random())*1000 + 1)
        if momo <= probability2:
            if(cslot1):
                c1t=currentTime
                c1c = cloudChooser()
                c1s = random.random()*80 + 120
                c1y = random.random()* 70 + 60
                cslot1 = False
                cloudGen(c1c, c1y, 1, c1t, c1s)
            elif(cslot2):
                c2t=currentTime
                c2c = cloudChooser()
                c2s = random.random()*80 + 80
                c2y = random.random()* 70 + 40
                cslot2 = False
                cloudGen(c2c, c2y, 2, c2t, c2s)
            if(cslot3):
                c3t=currentTime
                c3c = cloudChooser()
                c3s = random.random()*80 + 40
                c3y = random.random()* 70 + 20
                cslot3 = False
                cloudGen(c3c, c3y, 3, c3t, c3s)

        if not cslot1:
            cloudGen(c1c, c1y, 1, c1t, c1s)
        if not cslot2:
            cloudGen(c2c, c2y, 2, c2t, c2s)
        if not cslot3:
            cloudGen(c3c, c3y, 3, c3t, c3s)

        if not usedInvinc:
            if not isInvinc:
                placeBird(shield, 35, dheight - 130)
            else:
                placeBird(shield, 30, dheight - 135)

        if not usedSlow:
            if not isSlow:
                placeBird(snail, 23, dheight - 195)
            else:
                placeBird(snail, 17, dheight - 200)

        if not usedTeleport:
            placeBird(portal, 28, dheight - 275)



        if not isInvinc:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flapWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flapWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flapWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flapWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(bird, x,y)
                    c = bird
            else:
                placeBird(bird, x,y)
        else:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flaptWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flaptWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flaptWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flaptWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(birdt, x,y)
                    c = birdt
            else:
                placeBird(birdt, x,y)




        elTime = (currentTime - firstTime)/1000

        if elTime < 15:
            stage = 1
            probability = 1000/fps
        elif elTime < 30:
            stage = 2
            probability = 1200/fps
        elif elTime < 60:
            stage = 2
            probability = 1500/fps


        if elTime < 55:
            r = int((random.random())*1000 + 1)
            if r <= probability:
                if slot1:
                    s1t = currentTime
                    s1c = colorChooser(stage)
                    s1x = int((random.random())*1280 + 1)
                    s1s = isSlow
                    arrowSpawn(s1c, s1t, s1x, 1, s1s)
                    slot1 = False
                elif slot2:
                    s2t = currentTime
                    s2x = int((random.random())*1280 + 1)
                    s2c = colorChooser(stage)
                    s2s = isSlow
                    arrowSpawn(s2c, s2t, s2x, 2, s2s)
                    slot2 = False
                elif slot3:
                    s3t = currentTime
                    s3x = int((random.random())*1280 + 1)
                    s3c = colorChooser(stage)
                    s3s = isSlow
                    arrowSpawn(s3c, s3t, s3x, 3, s3s)
                    slot3 = False
                elif slot4:
                    s4t = currentTime
                    s4x = int((random.random())*1280 + 1)
                    s4c = colorChooser(stage)
                    s4s = isSlow
                    arrowSpawn(s4c, s4t, s4x, 4, s4s)
                    slot4 = False
                elif slot5:
                    s5t = currentTime
                    s5x = int((random.random())*1280 + 1)
                    s5c = colorChooser(stage)
                    s5s = isSlow
                    arrowSpawn(s5c, s5t, s5x, 5, s5s)
                    slot5 = False
                elif slot6:
                    s6t = currentTime
                    s6x = int((random.random())*1280 + 1)
                    s6c = colorChooser(stage)
                    s6s = isSlow
                    arrowSpawn(s6c, s6t, s6x, 6, s6s)
                    slot6 = False
                elif slot7:
                    s7t = currentTime
                    s7x = int((random.random())*1280 + 1)
                    s7c = colorChooser(stage)
                    s7s = isSlow
                    arrowSpawn(s7c, s7t, s7x, 7, s7s)
                    slot7 = False
                elif slot8:
                    s8t = currentTime
                    s8x = int((random.random())*1280 + 1)
                    s8c = colorChooser(stage)
                    s8s = isSlow
                    arrowSpawn(s8c, s8t, s8x, 8, s8s)
                    slot8 = False
                elif slot9:
                    s9t = currentTime
                    s9x = int((random.random())*1280 + 1)
                    s9c = colorChooser(stage)
                    s9s = isSlow
                    arrowSpawn(s9c, s9t, s9x, 9, s9s)
                    slot9 = False
                elif slot10:
                    s10t = currentTime
                    s10x = int((random.random())*1280 + 1)
                    s10c = colorChooser(stage)
                    s10s = isSlow
                    arrowSpawn(s10c, s10t, s10x, 10, s10s)
                    slot10 = False
            if stage >= 5:
                rn = int((random.random())*1000 + 1)
                if rn <= probabilityt:
                    if slot11:
                        s11t = currentTime
                        s11c = sideColorChooser(stage)
                        s11y = int((random.random())*600 + 1)
                        s11s = isSlow
                        s11sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
                        slot11 = False
                    elif slot12:
                        s12t = currentTime
                        s12y = int((random.random())*600 + 1)
                        s12c = sideColorChooser(stage)
                        s12s = isSlow
                        s12sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
                        slot12 = False
                    elif slot13:
                        s13t = currentTime
                        s13y = int((random.random())*600 + 1)
                        s13c = sideColorChooser(stage)
                        s13s = isSlow
                        s13sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
                        slot13 = False
                    elif slot14:
                        s14t = currentTime
                        s14y = int((random.random())*600 + 1)
                        s14c = sideColorChooser(stage)
                        s14s = isSlow
                        s14sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)
                        slot14 = False

        if not slot1:
            arrowSpawn(s1c, s1t, s1x, 1, s1s)
        if not slot2:
            arrowSpawn(s2c, s2t, s2x, 2, s2s)
        if not slot3:
            arrowSpawn(s3c, s3t, s3x, 3, s3s)
        if not slot4:
            arrowSpawn(s4c, s4t, s4x, 4, s4s)
        if not slot5:
            arrowSpawn(s5c, s5t, s5x, 5, s5s)
        if not slot6:
            arrowSpawn(s6c, s6t, s6x, 6, s6s)
        if not slot7:
            arrowSpawn(s7c, s7t, s7x, 7, s7s)
        if not slot8:
            arrowSpawn(s8c, s8t, s8x, 8, s8s)
        if not slot9:
            arrowSpawn(s9c, s9t, s9x, 9, s9s)
        if not slot10:
            arrowSpawn(s10c, s10t, s10x, 10, s10s)
        if not slot11:
            sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
        if not slot12:
            sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
        if not slot13:
            sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
        if not slot14:
            sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)

        if isDouble:
            placeBird(doublePoints, 120, dheight - 55)
            bonus += ((elTime * 1.005**elTime) - ((elTime - 1) * 1.005**(elTime - 1)))/fps
            if currentTime - doubleTime >= 20000:
                isDouble = False

        score = round((elTime/60)*100)
        message_display("Completion: " + str(score) + "%" , 10, 1.05, 30, "franklingothicdemicond")

        if elTime >= 60:
            passed = True
            if levelUnlocked == 1:
                levelUnlocked = 2
            break





        pygame.display.update()
        clock.tick()
##        if round(currentTime - firstTime) % 5000 > 0 and round(currentTime - firstTime) % 5000 < 100:
##            print(clock.get_fps())

    if passed:
        successLoop()
    else:
        dead = True
        deathLoop()

def levelTwo():
    global score
    global crashed
    global x
    global y
    global b
    global flipStatus
    global bird
    global birdt
    global skyBlue
    global f1
    global f1t
    global f2
    global f2t
    global f3
    global f3t
    global f4
    global f4t
    global flipCooldown
    global lastFlip
    global cooldown
    global flapCooldown
    global lastTime
    global dwidth
    global dheight
    global diffX
    global diffY
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global whiteArrow
    global aquaArrow
    global lightGreenArrow
    global deepBlueArrow
    global purpleArrow
    global pinkArrow
    global gift
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global stage
    global firstTime
    global probability
    global c
    global isDouble, doubleTime
    global dead
    global isInvinc
    global usedInvinc
    global invincTime
    global c1c, c1y, cslot1, c1t, c1s,c2c, c2y, cslot2, c2t, c2s,c3c, c3y, cslot3, c3t, c3s
    global isSlow
    global usedSlow
    global slowTime
    global isTeleport, usedTeleport, teleportTime
    global s1s, s2s,s3s,s4s,s5s,s6s,s7s,s8s,s9s,s10s
    global frames
    global portal
    global currentTime, teleportDelay
    global usedSlowSound
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t, s11s, s12s, s13s, s14s, s11sd, s12sd, s13sd, s14sd
    global bonus
    global passed, levelUnlocked
    shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
    snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
    portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
    currentTime = pygame.time.get_ticks()
    firstTime = pygame.time.get_ticks()
    slot1 = True
    s1x = 0
    slt = None
    s1c = None
    slot2 = True
    s2x = 0
    s2t = None
    s2c = None
    slot3 = True
    s3x = 0
    s3t = None
    s3c = None
    slot4 = True
    s4x = 0
    s4t = None
    s4c = None
    slot5 = True
    s5x = 0
    s5t = None
    s5c = None
    slot6 = True
    s6x = 0
    s6t = None
    s6c = None
    slot7 = True
    s7x = 0
    s7t = None
    s7c = None
    slot8 = True
    s8x = 0
    s8t = None
    s8c = None
    slot9 = True
    s9x = 0
    s9t = None
    s9c = None
    slot10 = True
    s10x = 0
    s10t = None
    s10c = None
    cslot1 = True
    c1y = 0
    c1t = None
    c1c = None
    c1s = None
    cslot2 = True
    c2y = 0
    c2t = None
    c2c = None
    c2s = None
    cslot3 = True
    c3y = 0
    c3t = None
    c3c = None
    c3s = None
    s1s = False
    s2s = False
    s3s = False
    s4s = False
    s5s = False
    s6s = False
    s7s = False
    s8s = False
    s9s = False
    s10s = False
    s11s = False
    s12s = False
    s13s = False
    s14s = False
    slot11 = True
    s11y = 0
    sllt = None
    s11c = None
    slot12 = True
    s12y = 0
    sl2t = None
    s12c = None
    slot13 = True
    s13y = 0
    sl3t = None
    s13c = None
    slot14 = True
    s14y = 0
    sl4t = None
    s14c = None
    s11sd = None
    s12sd = None
    s13sd = None
    s14sd = None
    isInvinc = False
    usedInvinc = True
    invincTime = None
    isSlow = False
    usedSlow = True
    slowTime = None
    isTeleport = False
    usedTeleport = True
    teleportTime = None
    teleportDelay = 0
    frames = 50
    skyBlue = (88, 173, 245)
    isDouble = False
    doubleTime = 0
    bonus = 0
    while not crashed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        currentTime = pygame.time.get_ticks() - teleportDelay
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and usedInvinc == False and isInvinc == False:
                pygame.mixer.Channel(0).play(invincSound)
                isInvinc = True
                invincTime = currentTime
                shield = pygame.transform.scale(shield, (60, 60))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and usedSlow == False and isSlow == False or event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and usedSlow == False and isSlow == False:
                pygame.mixer.Channel(1).play(slowDownSound)
                usedSlowSound = False
                isSlow = True
                slowTime = currentTime
                snail = pygame.transform.scale(snail, (94, 68))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and usedTeleport == False and isTeleport == False:
                isTeleport = True
                teleportTime = currentTime
                portal = pygame.transform.scale(portal, (90, 90))
                placeBird(portal, 18, dheight - 285)
                pygame.display.update()
                while isTeleport:
                    if pygame.time.get_ticks() - teleportTime >= 5000:
                        isTeleport = False
                        usedTeleport = True
                        teleportDelay += 5000
                        portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pygame.mixer.Channel(2).play(teleportSound)
                            x = pygame.mouse.get_pos()[0] - 75
                            y = pygame.mouse.get_pos()[1] - 75
                            isTeleport = False
                            usedTeleport = True
                            portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                            teleportDelay += (pygame.time.get_ticks() - teleportDelay - teleportTime)
                    clock.tick(60)


            ##print(event)

            ##if event.type == pygame.MOUSEMOTION:
        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
                    ##x = pygame.mouse.get_pos()[0] - 75
                    ##y = pygame.mouse.get_pos()[1] - 75
            diffX = (pygame.mouse.get_pos()[0] - 75) - x
            diffY = (pygame.mouse.get_pos()[1] - 75) - y
            x += 6/fps*diffX
            y += 6/fps*diffY

        if isInvinc:
            if currentTime - invincTime >= 4500 and currentTime - invincTime <= 5000:
                usedInvinc = True
            elif currentTime - invincTime <= 5500:
                usedInvinc = False
            elif currentTime - invincTime <= 6000:
                usedInvinc = True
            elif currentTime - invincTime <= 6250:
                usedInvinc = False
            elif currentTime - invincTime <= 6500:
                usedInvinc = True
            elif currentTime - invincTime <= 6750:
                usedInvinc = False
            elif currentTime - invincTime <= 7000:
                usedInvinc = True
            if currentTime - invincTime >= 7000:
                shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
                invincTime = 0
                isInvinc = False
                usedInvinc = True
        if isSlow:
            if frames > 0 and currentTime - slowTime <= 1000:
                greenMaker((0, 194, 103), skyBlue)
            if currentTime - slowTime >= 9500 and currentTime - slowTime <= 10000:
                usedSlow = True
            elif currentTime - slowTime <= 10500:
                usedSlow = False
            elif currentTime - slowTime <= 11000:
                usedSlow = True
                frames = 50
            elif currentTime - slowTime <= 11250:
                usedSlow = False
            elif currentTime - slowTime <= 11500:
                usedSlow = True
            elif currentTime - slowTime <= 11750:
                usedSlow = False
            elif currentTime - slowTime <= 12000:
                usedSlow = True
            if currentTime - slowTime >= 12000:
                snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
                slowTime = 0
                isSlow = False
                usedSlow = True
                frames = 50
        if isSlow and currentTime - slowTime >= 12000 - 1200*(frames/100):
            greenMaker((88, 173, 245), skyBlue)
        if isSlow and currentTime - slowTime >= 10950 and not usedSlowSound :
            pygame.mixer.Channel(3).play(speedUpSound)
            usedSlowSound = True
        if not isInvinc:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = False
        else:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = False


        gameDisplay.fill(skyBlue)
##        placeBird(landscape, 0, 650)

        momo = int((random.random())*1000 + 1)
        if momo <= probability2:
            if(cslot1):
                c1t=currentTime
                c1c = cloudChooser()
                c1s = random.random()*80 + 120
                c1y = random.random()* 70 + 60
                cslot1 = False
                cloudGen(c1c, c1y, 1, c1t, c1s)
            elif(cslot2):
                c2t=currentTime
                c2c = cloudChooser()
                c2s = random.random()*80 + 80
                c2y = random.random()* 70 + 40
                cslot2 = False
                cloudGen(c2c, c2y, 2, c2t, c2s)
            if(cslot3):
                c3t=currentTime
                c3c = cloudChooser()
                c3s = random.random()*80 + 40
                c3y = random.random()* 70 + 20
                cslot3 = False
                cloudGen(c3c, c3y, 3, c3t, c3s)

        if not cslot1:
            cloudGen(c1c, c1y, 1, c1t, c1s)
        if not cslot2:
            cloudGen(c2c, c2y, 2, c2t, c2s)
        if not cslot3:
            cloudGen(c3c, c3y, 3, c3t, c3s)

        if not usedInvinc:
            if not isInvinc:
                placeBird(shield, 35, dheight - 130)
            else:
                placeBird(shield, 30, dheight - 135)

        if not usedSlow:
            if not isSlow:
                placeBird(snail, 23, dheight - 195)
            else:
                placeBird(snail, 17, dheight - 200)

        if not usedTeleport:
            placeBird(portal, 28, dheight - 275)



        if not isInvinc:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flapWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flapWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flapWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flapWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(bird, x,y)
                    c = bird
            else:
                placeBird(bird, x,y)
        else:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flaptWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flaptWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flaptWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flaptWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(birdt, x,y)
                    c = birdt
            else:
                placeBird(birdt, x,y)




        elTime = (currentTime - firstTime)/1000

        if elTime < 15:
            stage = 4
            probability = 2000/fps
        elif elTime < 30:
            stage = 4
            probability = 2200/fps
        elif elTime < 60:
            stage = 4
            probability = 2500/fps


        if elTime < 55:
            r = int((random.random())*1000 + 1)
            if r <= probability:
                if slot1:
                    s1t = currentTime
                    s1c = colorChooser(stage)
                    s1x = int((random.random())*1280 + 1)
                    s1s = isSlow
                    arrowSpawn(s1c, s1t, s1x, 1, s1s)
                    slot1 = False
                elif slot2:
                    s2t = currentTime
                    s2x = int((random.random())*1280 + 1)
                    s2c = colorChooser(stage)
                    s2s = isSlow
                    arrowSpawn(s2c, s2t, s2x, 2, s2s)
                    slot2 = False
                elif slot3:
                    s3t = currentTime
                    s3x = int((random.random())*1280 + 1)
                    s3c = colorChooser(stage)
                    s3s = isSlow
                    arrowSpawn(s3c, s3t, s3x, 3, s3s)
                    slot3 = False
                elif slot4:
                    s4t = currentTime
                    s4x = int((random.random())*1280 + 1)
                    s4c = colorChooser(stage)
                    s4s = isSlow
                    arrowSpawn(s4c, s4t, s4x, 4, s4s)
                    slot4 = False
                elif slot5:
                    s5t = currentTime
                    s5x = int((random.random())*1280 + 1)
                    s5c = colorChooser(stage)
                    s5s = isSlow
                    arrowSpawn(s5c, s5t, s5x, 5, s5s)
                    slot5 = False
                elif slot6:
                    s6t = currentTime
                    s6x = int((random.random())*1280 + 1)
                    s6c = colorChooser(stage)
                    s6s = isSlow
                    arrowSpawn(s6c, s6t, s6x, 6, s6s)
                    slot6 = False
                elif slot7:
                    s7t = currentTime
                    s7x = int((random.random())*1280 + 1)
                    s7c = colorChooser(stage)
                    s7s = isSlow
                    arrowSpawn(s7c, s7t, s7x, 7, s7s)
                    slot7 = False
                elif slot8:
                    s8t = currentTime
                    s8x = int((random.random())*1280 + 1)
                    s8c = colorChooser(stage)
                    s8s = isSlow
                    arrowSpawn(s8c, s8t, s8x, 8, s8s)
                    slot8 = False
                elif slot9:
                    s9t = currentTime
                    s9x = int((random.random())*1280 + 1)
                    s9c = colorChooser(stage)
                    s9s = isSlow
                    arrowSpawn(s9c, s9t, s9x, 9, s9s)
                    slot9 = False
                elif slot10:
                    s10t = currentTime
                    s10x = int((random.random())*1280 + 1)
                    s10c = colorChooser(stage)
                    s10s = isSlow
                    arrowSpawn(s10c, s10t, s10x, 10, s10s)
                    slot10 = False
            if stage >= 5:
                rn = int((random.random())*1000 + 1)
                if rn <= probabilityt:
                    if slot11:
                        s11t = currentTime
                        s11c = sideColorChooser(stage)
                        s11y = int((random.random())*600 + 1)
                        s11s = isSlow
                        s11sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
                        slot11 = False
                    elif slot12:
                        s12t = currentTime
                        s12y = int((random.random())*600 + 1)
                        s12c = sideColorChooser(stage)
                        s12s = isSlow
                        s12sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
                        slot12 = False
                    elif slot13:
                        s13t = currentTime
                        s13y = int((random.random())*600 + 1)
                        s13c = sideColorChooser(stage)
                        s13s = isSlow
                        s13sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
                        slot13 = False
                    elif slot14:
                        s14t = currentTime
                        s14y = int((random.random())*600 + 1)
                        s14c = sideColorChooser(stage)
                        s14s = isSlow
                        s14sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)
                        slot14 = False

        if not slot1:
            arrowSpawn(s1c, s1t, s1x, 1, s1s)
        if not slot2:
            arrowSpawn(s2c, s2t, s2x, 2, s2s)
        if not slot3:
            arrowSpawn(s3c, s3t, s3x, 3, s3s)
        if not slot4:
            arrowSpawn(s4c, s4t, s4x, 4, s4s)
        if not slot5:
            arrowSpawn(s5c, s5t, s5x, 5, s5s)
        if not slot6:
            arrowSpawn(s6c, s6t, s6x, 6, s6s)
        if not slot7:
            arrowSpawn(s7c, s7t, s7x, 7, s7s)
        if not slot8:
            arrowSpawn(s8c, s8t, s8x, 8, s8s)
        if not slot9:
            arrowSpawn(s9c, s9t, s9x, 9, s9s)
        if not slot10:
            arrowSpawn(s10c, s10t, s10x, 10, s10s)
        if not slot11:
            sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
        if not slot12:
            sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
        if not slot13:
            sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
        if not slot14:
            sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)

        if isDouble:
            placeBird(doublePoints, 120, dheight - 55)
            bonus += ((elTime * 1.005**elTime) - ((elTime - 1) * 1.005**(elTime - 1)))/fps
            if currentTime - doubleTime >= 20000:
                isDouble = False

        score = round((elTime/60)*100)
        message_display("Completion: " + str(score) + "%" , 10, 1.05, 30, "franklingothicdemicond")

        if elTime >= 60:
            passed = True
            if levelUnlocked == 2:
                levelUnlocked = 3
            break





        pygame.display.update()
        clock.tick()
##        if round(currentTime - firstTime) % 5000 > 0 and round(currentTime - firstTime) % 5000 < 100:
##            print(clock.get_fps())

    if passed:
        successLoop()
    else:
        dead = True
        deathLoop()


def levelThree():
    global score
    global crashed
    global x
    global y
    global b
    global flipStatus
    global bird
    global birdt
    global skyBlue
    global f1
    global f1t
    global f2
    global f2t
    global f3
    global f3t
    global f4
    global f4t
    global flipCooldown
    global lastFlip
    global cooldown
    global flapCooldown
    global lastTime
    global dwidth
    global dheight
    global diffX
    global diffY
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global whiteArrow
    global aquaArrow
    global lightGreenArrow
    global deepBlueArrow
    global purpleArrow
    global pinkArrow
    global gift
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global stage
    global firstTime
    global probability
    global c
    global isDouble, doubleTime
    global dead
    global isInvinc
    global usedInvinc
    global invincTime
    global c1c, c1y, cslot1, c1t, c1s,c2c, c2y, cslot2, c2t, c2s,c3c, c3y, cslot3, c3t, c3s
    global isSlow
    global usedSlow
    global slowTime
    global isTeleport, usedTeleport, teleportTime
    global s1s, s2s,s3s,s4s,s5s,s6s,s7s,s8s,s9s,s10s
    global frames
    global portal
    global currentTime, teleportDelay
    global usedSlowSound
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t, s11s, s12s, s13s, s14s, s11sd, s12sd, s13sd, s14sd
    global bonus
    global passed, levelUnlocked
    shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
    snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
    portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
    currentTime = pygame.time.get_ticks()
    firstTime = pygame.time.get_ticks()
    slot1 = True
    s1x = 0
    slt = None
    s1c = None
    slot2 = True
    s2x = 0
    s2t = None
    s2c = None
    slot3 = True
    s3x = 0
    s3t = None
    s3c = None
    slot4 = True
    s4x = 0
    s4t = None
    s4c = None
    slot5 = True
    s5x = 0
    s5t = None
    s5c = None
    slot6 = True
    s6x = 0
    s6t = None
    s6c = None
    slot7 = True
    s7x = 0
    s7t = None
    s7c = None
    slot8 = True
    s8x = 0
    s8t = None
    s8c = None
    slot9 = True
    s9x = 0
    s9t = None
    s9c = None
    slot10 = True
    s10x = 0
    s10t = None
    s10c = None
    cslot1 = True
    c1y = 0
    c1t = None
    c1c = None
    c1s = None
    cslot2 = True
    c2y = 0
    c2t = None
    c2c = None
    c2s = None
    cslot3 = True
    c3y = 0
    c3t = None
    c3c = None
    c3s = None
    s1s = False
    s2s = False
    s3s = False
    s4s = False
    s5s = False
    s6s = False
    s7s = False
    s8s = False
    s9s = False
    s10s = False
    s11s = False
    s12s = False
    s13s = False
    s14s = False
    slot11 = True
    s11y = 0
    sllt = None
    s11c = None
    slot12 = True
    s12y = 0
    sl2t = None
    s12c = None
    slot13 = True
    s13y = 0
    sl3t = None
    s13c = None
    slot14 = True
    s14y = 0
    sl4t = None
    s14c = None
    s11sd = None
    s12sd = None
    s13sd = None
    s14sd = None
    isInvinc = False
    usedInvinc = True
    invincTime = None
    isSlow = False
    usedSlow = True
    slowTime = None
    isTeleport = False
    usedTeleport = True
    teleportTime = None
    teleportDelay = 0
    frames = 50
    skyBlue = (88, 173, 245)
    isDouble = False
    doubleTime = 0
    bonus = 0
    while not crashed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        currentTime = pygame.time.get_ticks() - teleportDelay
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and usedInvinc == False and isInvinc == False:
                pygame.mixer.Channel(0).play(invincSound)
                isInvinc = True
                invincTime = currentTime
                shield = pygame.transform.scale(shield, (60, 60))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and usedSlow == False and isSlow == False or event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and usedSlow == False and isSlow == False:
                pygame.mixer.Channel(1).play(slowDownSound)
                usedSlowSound = False
                isSlow = True
                slowTime = currentTime
                snail = pygame.transform.scale(snail, (94, 68))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and usedTeleport == False and isTeleport == False:
                isTeleport = True
                teleportTime = currentTime
                portal = pygame.transform.scale(portal, (90, 90))
                placeBird(portal, 18, dheight - 285)
                pygame.display.update()
                while isTeleport:
                    if pygame.time.get_ticks() - teleportTime >= 5000:
                        isTeleport = False
                        usedTeleport = True
                        teleportDelay += 5000
                        portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pygame.mixer.Channel(2).play(teleportSound)
                            x = pygame.mouse.get_pos()[0] - 75
                            y = pygame.mouse.get_pos()[1] - 75
                            isTeleport = False
                            usedTeleport = True
                            portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                            teleportDelay += (pygame.time.get_ticks() - teleportDelay - teleportTime)
                    clock.tick(60)


            ##print(event)

            ##if event.type == pygame.MOUSEMOTION:
        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
                    ##x = pygame.mouse.get_pos()[0] - 75
                    ##y = pygame.mouse.get_pos()[1] - 75
            diffX = (pygame.mouse.get_pos()[0] - 75) - x
            diffY = (pygame.mouse.get_pos()[1] - 75) - y
            x += 6/fps*diffX
            y += 6/fps*diffY

        if isInvinc:
            if currentTime - invincTime >= 4500 and currentTime - invincTime <= 5000:
                usedInvinc = True
            elif currentTime - invincTime <= 5500:
                usedInvinc = False
            elif currentTime - invincTime <= 6000:
                usedInvinc = True
            elif currentTime - invincTime <= 6250:
                usedInvinc = False
            elif currentTime - invincTime <= 6500:
                usedInvinc = True
            elif currentTime - invincTime <= 6750:
                usedInvinc = False
            elif currentTime - invincTime <= 7000:
                usedInvinc = True
            if currentTime - invincTime >= 7000:
                shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
                invincTime = 0
                isInvinc = False
                usedInvinc = True
        if isSlow:
            if frames > 0 and currentTime - slowTime <= 1000:
                greenMaker((0, 194, 103), skyBlue)
            if currentTime - slowTime >= 9500 and currentTime - slowTime <= 10000:
                usedSlow = True
            elif currentTime - slowTime <= 10500:
                usedSlow = False
            elif currentTime - slowTime <= 11000:
                usedSlow = True
                frames = 50
            elif currentTime - slowTime <= 11250:
                usedSlow = False
            elif currentTime - slowTime <= 11500:
                usedSlow = True
            elif currentTime - slowTime <= 11750:
                usedSlow = False
            elif currentTime - slowTime <= 12000:
                usedSlow = True
            if currentTime - slowTime >= 12000:
                snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
                slowTime = 0
                isSlow = False
                usedSlow = True
                frames = 50
        if isSlow and currentTime - slowTime >= 12000 - 1200*(frames/100):
            greenMaker((88, 173, 245), skyBlue)
        if isSlow and currentTime - slowTime >= 10950 and not usedSlowSound :
            pygame.mixer.Channel(3).play(speedUpSound)
            usedSlowSound = True
        if not isInvinc:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = False
        else:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = False


        gameDisplay.fill(skyBlue)
##        placeBird(landscape, 0, 650)

        momo = int((random.random())*1000 + 1)
        if momo <= probability2:
            if(cslot1):
                c1t=currentTime
                c1c = cloudChooser()
                c1s = random.random()*80 + 120
                c1y = random.random()* 70 + 60
                cslot1 = False
                cloudGen(c1c, c1y, 1, c1t, c1s)
            elif(cslot2):
                c2t=currentTime
                c2c = cloudChooser()
                c2s = random.random()*80 + 80
                c2y = random.random()* 70 + 40
                cslot2 = False
                cloudGen(c2c, c2y, 2, c2t, c2s)
            if(cslot3):
                c3t=currentTime
                c3c = cloudChooser()
                c3s = random.random()*80 + 40
                c3y = random.random()* 70 + 20
                cslot3 = False
                cloudGen(c3c, c3y, 3, c3t, c3s)

        if not cslot1:
            cloudGen(c1c, c1y, 1, c1t, c1s)
        if not cslot2:
            cloudGen(c2c, c2y, 2, c2t, c2s)
        if not cslot3:
            cloudGen(c3c, c3y, 3, c3t, c3s)

        if not usedInvinc:
            if not isInvinc:
                placeBird(shield, 35, dheight - 130)
            else:
                placeBird(shield, 30, dheight - 135)

        if not usedSlow:
            if not isSlow:
                placeBird(snail, 23, dheight - 195)
            else:
                placeBird(snail, 17, dheight - 200)

        if not usedTeleport:
            placeBird(portal, 28, dheight - 275)



        if not isInvinc:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flapWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flapWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flapWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flapWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(bird, x,y)
                    c = bird
            else:
                placeBird(bird, x,y)
        else:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flaptWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flaptWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flaptWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flaptWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(birdt, x,y)
                    c = birdt
            else:
                placeBird(birdt, x,y)




        elTime = (currentTime - firstTime)/1000

        if elTime < 15:
            stage = 5
            probability = 1500/fps
            probabilityt = 500/fps
        elif elTime < 30:
            stage = 5
            probability = 1700/fps
            probabilityt = 550/fps
        elif elTime < 60:
            stage = 5
            probability = 1900/fps
            probabilityt = 600/fps


        if elTime < 57:
            r = int((random.random())*1000 + 1)
            if r <= probability or elTime > 10 and elTime < 11 or elTime > 17 and elTime < 18 or elTime >29 and elTime < 30 or elTime >41 and elTime < 42 or elTime > 45 and elTime < 46 or elTime > 51 and elTime < 52:
                if slot1:
                    s1t = currentTime
                    s1c = yellowArrow
                    s1x = int((random.random())*1280 + 1)
                    s1s = isSlow
                    arrowSpawn(s1c, s1t, s1x, 1, s1s)
                    slot1 = False
                elif slot2:
                    s2t = currentTime
                    s2x = int((random.random())*1280 + 1)
                    s2c = yellowArrow
                    s2s = isSlow
                    arrowSpawn(s2c, s2t, s2x, 2, s2s)
                    slot2 = False
                elif slot3:
                    s3t = currentTime
                    s3x = int((random.random())*1280 + 1)
                    s3c = yellowArrow
                    s3s = isSlow
                    arrowSpawn(s3c, s3t, s3x, 3, s3s)
                    slot3 = False
                elif slot4:
                    s4t = currentTime
                    s4x = int((random.random())*1280 + 1)
                    s4c = yellowArrow
                    s4s = isSlow
                    arrowSpawn(s4c, s4t, s4x, 4, s4s)
                    slot4 = False
                elif slot5:
                    s5t = currentTime
                    s5x = int((random.random())*1280 + 1)
                    s5c = yellowArrow
                    s5s = isSlow
                    arrowSpawn(s5c, s5t, s5x, 5, s5s)
                    slot5 = False
                elif slot6:
                    s6t = currentTime
                    s6x = int((random.random())*1280 + 1)
                    s6c = yellowArrow
                    s6s = isSlow
                    arrowSpawn(s6c, s6t, s6x, 6, s6s)
                    slot6 = False
                elif slot7:
                    s7t = currentTime
                    s7x = int((random.random())*1280 + 1)
                    s7c = yellowArrow
                    s7s = isSlow
                    arrowSpawn(s7c, s7t, s7x, 7, s7s)
                    slot7 = False
                elif slot8:
                    s8t = currentTime
                    s8x = int((random.random())*1280 + 1)
                    s8c = yellowArrow
                    s8s = isSlow
                    arrowSpawn(s8c, s8t, s8x, 8, s8s)
                    slot8 = False
                elif slot9:
                    s9t = currentTime
                    s9x = int((random.random())*1280 + 1)
                    s9c = yellowArrow
                    s9s = isSlow
                    arrowSpawn(s9c, s9t, s9x, 9, s9s)
                    slot9 = False
                elif slot10:
                    s10t = currentTime
                    s10x = int((random.random())*1280 + 1)
                    s10c = yellowArrow
                    s10s = isSlow
                    arrowSpawn(s10c, s10t, s10x, 10, s10s)
                    slot10 = False
            if stage >= 5:
                rn = int((random.random())*1000 + 1)
                if rn <= probabilityt:
                    if slot11:
                        s11t = currentTime
                        s11c = redArrow
                        s11y = int((random.random())*600 + 1)
                        s11s = isSlow
                        s11sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
                        slot11 = False
                    elif slot12:
                        s12t = currentTime
                        s12y = int((random.random())*600 + 1)
                        s12c = redArrow
                        s12s = isSlow
                        s12sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
                        slot12 = False
                    elif slot13:
                        s13t = currentTime
                        s13y = int((random.random())*600 + 1)
                        s13c = redArrow
                        s13s = isSlow
                        s13sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
                        slot13 = False
                    elif slot14:
                        s14t = currentTime
                        s14y = int((random.random())*600 + 1)
                        s14c = redArrow
                        s14s = isSlow
                        s14sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)
                        slot14 = False

        if not slot1:
            arrowSpawn(s1c, s1t, s1x, 1, s1s)
        if not slot2:
            arrowSpawn(s2c, s2t, s2x, 2, s2s)
        if not slot3:
            arrowSpawn(s3c, s3t, s3x, 3, s3s)
        if not slot4:
            arrowSpawn(s4c, s4t, s4x, 4, s4s)
        if not slot5:
            arrowSpawn(s5c, s5t, s5x, 5, s5s)
        if not slot6:
            arrowSpawn(s6c, s6t, s6x, 6, s6s)
        if not slot7:
            arrowSpawn(s7c, s7t, s7x, 7, s7s)
        if not slot8:
            arrowSpawn(s8c, s8t, s8x, 8, s8s)
        if not slot9:
            arrowSpawn(s9c, s9t, s9x, 9, s9s)
        if not slot10:
            arrowSpawn(s10c, s10t, s10x, 10, s10s)
        if not slot11:
            sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
        if not slot12:
            sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
        if not slot13:
            sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
        if not slot14:
            sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)

        if isDouble:
            placeBird(doublePoints, 120, dheight - 55)
            bonus += ((elTime * 1.005**elTime) - ((elTime - 1) * 1.005**(elTime - 1)))/fps
            if currentTime - doubleTime >= 20000:
                isDouble = False

        score = round((elTime/60)*100)
        message_display("Completion: " + str(score) + "%" , 10, 1.05, 30, "franklingothicdemicond")

        if elTime >= 60:
            passed = True
            if levelUnlocked == 3:
                levelUnlocked = 4
            break





        pygame.display.update()
        clock.tick()
##        if round(currentTime - firstTime) % 5000 > 0 and round(currentTime - firstTime) % 5000 < 100:
##            print(clock.get_fps())

    if passed:
        successLoop()
    else:
        dead = True
        deathLoop()

def levelFour():
    global score
    global crashed
    global x
    global y
    global b
    global flipStatus
    global bird
    global birdt
    global skyBlue
    global f1
    global f1t
    global f2
    global f2t
    global f3
    global f3t
    global f4
    global f4t
    global flipCooldown
    global lastFlip
    global cooldown
    global flapCooldown
    global lastTime
    global dwidth
    global dheight
    global diffX
    global diffY
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global whiteArrow
    global aquaArrow
    global lightGreenArrow
    global deepBlueArrow
    global purpleArrow
    global pinkArrow
    global gift
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global stage
    global firstTime
    global probability
    global c
    global isDouble, doubleTime
    global dead
    global isInvinc
    global usedInvinc
    global invincTime
    global c1c, c1y, cslot1, c1t, c1s,c2c, c2y, cslot2, c2t, c2s,c3c, c3y, cslot3, c3t, c3s
    global isSlow
    global usedSlow
    global slowTime
    global isTeleport, usedTeleport, teleportTime
    global s1s, s2s,s3s,s4s,s5s,s6s,s7s,s8s,s9s,s10s
    global frames
    global portal
    global currentTime, teleportDelay
    global usedSlowSound
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t, s11s, s12s, s13s, s14s, s11sd, s12sd, s13sd, s14sd
    global bonus
    global passed, levelUnlocked
    shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
    snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
    portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
    currentTime = pygame.time.get_ticks()
    firstTime = pygame.time.get_ticks()
    slot1 = True
    s1x = 0
    slt = None
    s1c = None
    slot2 = True
    s2x = 0
    s2t = None
    s2c = None
    slot3 = True
    s3x = 0
    s3t = None
    s3c = None
    slot4 = True
    s4x = 0
    s4t = None
    s4c = None
    slot5 = True
    s5x = 0
    s5t = None
    s5c = None
    slot6 = True
    s6x = 0
    s6t = None
    s6c = None
    slot7 = True
    s7x = 0
    s7t = None
    s7c = None
    slot8 = True
    s8x = 0
    s8t = None
    s8c = None
    slot9 = True
    s9x = 0
    s9t = None
    s9c = None
    slot10 = True
    s10x = 0
    s10t = None
    s10c = None
    cslot1 = True
    c1y = 0
    c1t = None
    c1c = None
    c1s = None
    cslot2 = True
    c2y = 0
    c2t = None
    c2c = None
    c2s = None
    cslot3 = True
    c3y = 0
    c3t = None
    c3c = None
    c3s = None
    s1s = False
    s2s = False
    s3s = False
    s4s = False
    s5s = False
    s6s = False
    s7s = False
    s8s = False
    s9s = False
    s10s = False
    s11s = False
    s12s = False
    s13s = False
    s14s = False
    slot11 = True
    s11y = 0
    sllt = None
    s11c = None
    slot12 = True
    s12y = 0
    sl2t = None
    s12c = None
    slot13 = True
    s13y = 0
    sl3t = None
    s13c = None
    slot14 = True
    s14y = 0
    sl4t = None
    s14c = None
    s11sd = None
    s12sd = None
    s13sd = None
    s14sd = None
    isInvinc = False
    usedInvinc = False
    invincTime = None
    isSlow = False
    usedSlow = False
    slowTime = None
    isTeleport = False
    usedTeleport = False
    teleportTime = None
    teleportDelay = 0
    frames = 50
    skyBlue = (88, 173, 245)
    isDouble = False
    doubleTime = 0
    bonus = 0
    while not crashed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        currentTime = pygame.time.get_ticks() - teleportDelay
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and usedInvinc == False and isInvinc == False:
                pygame.mixer.Channel(0).play(invincSound)
                isInvinc = True
                invincTime = currentTime
                shield = pygame.transform.scale(shield, (60, 60))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and usedSlow == False and isSlow == False or event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and usedSlow == False and isSlow == False:
                pygame.mixer.Channel(1).play(slowDownSound)
                usedSlowSound = False
                isSlow = True
                slowTime = currentTime
                snail = pygame.transform.scale(snail, (94, 68))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and usedTeleport == False and isTeleport == False:
                isTeleport = True
                teleportTime = currentTime
                portal = pygame.transform.scale(portal, (90, 90))
                placeBird(portal, 18, dheight - 285)
                pygame.display.update()
                while isTeleport:
                    if pygame.time.get_ticks() - teleportTime >= 5000:
                        isTeleport = False
                        usedTeleport = True
                        teleportDelay += 5000
                        portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pygame.mixer.Channel(2).play(teleportSound)
                            x = pygame.mouse.get_pos()[0] - 75
                            y = pygame.mouse.get_pos()[1] - 75
                            isTeleport = False
                            usedTeleport = True
                            portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                            teleportDelay += (pygame.time.get_ticks() - teleportDelay - teleportTime)
                    clock.tick(60)


            ##print(event)

            ##if event.type == pygame.MOUSEMOTION:
        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
                    ##x = pygame.mouse.get_pos()[0] - 75
                    ##y = pygame.mouse.get_pos()[1] - 75
            diffX = (pygame.mouse.get_pos()[0] - 75) - x
            diffY = (pygame.mouse.get_pos()[1] - 75) - y
            x += 6/fps*diffX
            y += 6/fps*diffY

        if isInvinc:
            if currentTime - invincTime >= 4500 and currentTime - invincTime <= 5000:
                usedInvinc = True
            elif currentTime - invincTime <= 5500:
                usedInvinc = False
            elif currentTime - invincTime <= 6000:
                usedInvinc = True
            elif currentTime - invincTime <= 6250:
                usedInvinc = False
            elif currentTime - invincTime <= 6500:
                usedInvinc = True
            elif currentTime - invincTime <= 6750:
                usedInvinc = False
            elif currentTime - invincTime <= 7000:
                usedInvinc = True
            if currentTime - invincTime >= 7000:
                shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
                invincTime = 0
                isInvinc = False
                usedInvinc = True
        if isSlow:
            if frames > 0 and currentTime - slowTime <= 1000:
                greenMaker((0, 194, 103), skyBlue)
            if currentTime - slowTime >= 9500 and currentTime - slowTime <= 10000:
                usedSlow = True
            elif currentTime - slowTime <= 10500:
                usedSlow = False
            elif currentTime - slowTime <= 11000:
                usedSlow = True
                frames = 50
            elif currentTime - slowTime <= 11250:
                usedSlow = False
            elif currentTime - slowTime <= 11500:
                usedSlow = True
            elif currentTime - slowTime <= 11750:
                usedSlow = False
            elif currentTime - slowTime <= 12000:
                usedSlow = True
            if currentTime - slowTime >= 12000:
                snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
                slowTime = 0
                isSlow = False
                usedSlow = True
                frames = 50
        if isSlow and currentTime - slowTime >= 12000 - 1200*(frames/100):
            greenMaker((88, 173, 245), skyBlue)
        if isSlow and currentTime - slowTime >= 10950 and not usedSlowSound :
            pygame.mixer.Channel(3).play(speedUpSound)
            usedSlowSound = True
        if not isInvinc:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = False
        else:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = False


        gameDisplay.fill(skyBlue)
##        placeBird(landscape, 0, 650)

        momo = int((random.random())*1000 + 1)
        if momo <= probability2:
            if(cslot1):
                c1t=currentTime
                c1c = cloudChooser()
                c1s = random.random()*80 + 120
                c1y = random.random()* 70 + 60
                cslot1 = False
                cloudGen(c1c, c1y, 1, c1t, c1s)
            elif(cslot2):
                c2t=currentTime
                c2c = cloudChooser()
                c2s = random.random()*80 + 80
                c2y = random.random()* 70 + 40
                cslot2 = False
                cloudGen(c2c, c2y, 2, c2t, c2s)
            if(cslot3):
                c3t=currentTime
                c3c = cloudChooser()
                c3s = random.random()*80 + 40
                c3y = random.random()* 70 + 20
                cslot3 = False
                cloudGen(c3c, c3y, 3, c3t, c3s)

        if not cslot1:
            cloudGen(c1c, c1y, 1, c1t, c1s)
        if not cslot2:
            cloudGen(c2c, c2y, 2, c2t, c2s)
        if not cslot3:
            cloudGen(c3c, c3y, 3, c3t, c3s)

        if not usedInvinc:
            if not isInvinc:
                placeBird(shield, 35, dheight - 130)
            else:
                placeBird(shield, 30, dheight - 135)

        if not usedSlow:
            if not isSlow:
                placeBird(snail, 23, dheight - 195)
            else:
                placeBird(snail, 17, dheight - 200)

        if not usedTeleport:
            placeBird(portal, 28, dheight - 275)



        if not isInvinc:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flapWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flapWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flapWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flapWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(bird, x,y)
                    c = bird
            else:
                placeBird(bird, x,y)
        else:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flaptWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flaptWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flaptWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flaptWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(birdt, x,y)
                    c = birdt
            else:
                placeBird(birdt, x,y)




        elTime = (currentTime - firstTime)/1000

        if elTime < 60:
            probabilityt = 2500/fps


        if elTime < 58:
            r = int((random.random())*1000 + 1)
            if r <= probabilityt:
                if slot1:
                    s1t = currentTime
                    s1c = pinkArrow
                    s1y = int((random.random())*600 + 1)
                    s1s = isSlow
                    sideArrowSpawn(s1c, s1t, s1y, 1, s1s, 1)
                    slot1 = False
                elif slot2:
                    s2t = currentTime
                    s2y = int((random.random())*600 + 1)
                    s2c = pinkArrow
                    s2s = isSlow
                    sideArrowSpawn(s2c, s2t, s2y, 2, s2s, 2)
                    slot2 = False
                elif slot3:
                    s3t = currentTime
                    s3y = int((random.random())*600 + 1)
                    s3c = pinkArrow
                    s3s = isSlow
                    sideArrowSpawn(s3c, s3t, s3y, 3, s3s, 1)
                    slot3 = False
                elif slot4:
                    s4t = currentTime
                    s4y = int((random.random())*600 + 1)
                    s4c = pinkArrow
                    s4s = isSlow
                    sideArrowSpawn(s4c, s4t, s4y, 4, s4s, 2)
                    slot4 = False
                elif slot5:
                    s5t = currentTime
                    s5y = int((random.random())*600 + 1)
                    s5c = pinkArrow
                    s5s = isSlow
                    sideArrowSpawn(s5c, s5t, s5y, 5, s5s, 1)
                    slot5 = False
                elif slot6:
                    s6t = currentTime
                    s6y = int((random.random())*600 + 1)
                    s6c = pinkArrow
                    s6s = isSlow
                    sideArrowSpawn(s6c, s6t, s6y, 6, s6s, 2)
                    slot6 = False
                elif slot7:
                    s7t = currentTime
                    s7y = int((random.random())*600 + 1)
                    s7c = pinkArrow
                    s7s = isSlow
                    sideArrowSpawn(s7c, s7t, s7y, 7, s7s, 1)
                    slot7 = False
                elif slot8:
                    s8t = currentTime
                    s8y = int((random.random())*600 + 1)
                    s8c = pinkArrow
                    s8s = isSlow
                    sideArrowSpawn(s8c, s8t, s8y, 8, s8s, 2)
                    slot8 = False
                elif slot9:
                    s9t = currentTime
                    s9y = int((random.random())*600 + 1)
                    s9c = pinkArrow
                    s9s = isSlow
                    sideArrowSpawn(s9c, s9t, s9y, 9, s9s, 1)
                    slot9 = False
                elif slot10:
                    s10t = currentTime
                    s10y = int((random.random())*600 + 1)
                    s10c = pinkArrow
                    s10s = isSlow
                    sideArrowSpawn(s10c, s10t, s10x, 10, s10s, 2)
                    slot10 = False
                elif slot11:
                    s11t = currentTime
                    s11c = pinkArrow
                    s11y = int((random.random())*600 + 1)
                    s11s = isSlow
                    s11sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
                    slot11 = False
                elif slot12:
                    s12t = currentTime
                    s12y = int((random.random())*600 + 1)
                    s12c = pinkArrow
                    s12s = isSlow
                    s12sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
                    slot12 = False
                elif slot13:
                    s13t = currentTime
                    s13y = int((random.random())*600 + 1)
                    s13c = pinkArrow
                    s13s = isSlow
                    s13sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
                    slot13 = False
                elif slot14:
                    s14t = currentTime
                    s14y = int((random.random())*600 + 1)
                    s14c = pinkArrow
                    s14s = isSlow
                    s14sd = int(random.random()*2 + 1)
                    sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)
                    slot14 = False

        if not slot1:
            sideArrowSpawn(s1c, s1t, s1y, 1, s1s,1)
        if not slot2:
            sideArrowSpawn(s2c, s2t, s2y, 2, s2s,2)
        if not slot3:
            sideArrowSpawn(s3c, s3t, s3y, 3, s3s,1)
        if not slot4:
            sideArrowSpawn(s4c, s4t, s4y, 4, s4s,2)
        if not slot5:
            sideArrowSpawn(s5c, s5t, s5y, 5, s5s,1)
        if not slot6:
            sideArrowSpawn(s6c, s6t, s6y, 6, s6s,2)
        if not slot7:
            sideArrowSpawn(s7c, s7t, s7y, 7, s7s,1)
        if not slot8:
            sideArrowSpawn(s8c, s8t, s8y, 8, s8s,2)
        if not slot9:
            sideArrowSpawn(s9c, s9t, s9y, 9, s9s,1)
        if not slot10:
            sideArrowSpawn(s10c, s10t, s10y, 10, s10s,2)
        if not slot11:
            sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
        if not slot12:
            sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
        if not slot13:
            sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
        if not slot14:
            sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)

        if isDouble:
            placeBird(doublePoints, 120, dheight - 55)
            bonus += ((elTime * 1.005**elTime) - ((elTime - 1) * 1.005**(elTime - 1)))/fps
            if currentTime - doubleTime >= 20000:
                isDouble = False

        score = round((elTime/60)*100)
        message_display("Completion: " + str(score) + "%" , 10, 1.05, 30, "franklingothicdemicond")

        if elTime >= 60:
            passed = True
            if levelUnlocked == 4:
                levelUnlocked = 5
            break





        pygame.display.update()
        clock.tick()
##        if round(currentTime - firstTime) % 5000 > 0 and round(currentTime - firstTime) % 5000 < 100:
##            print(clock.get_fps())

    if passed:
        successLoop()
    else:
        dead = True
        deathLoop()

def levelFive():
    global score
    global crashed
    global x
    global y
    global b
    global flipStatus
    global bird
    global birdt
    global skyBlue
    global f1
    global f1t
    global f2
    global f2t
    global f3
    global f3t
    global f4
    global f4t
    global flipCooldown
    global lastFlip
    global cooldown
    global flapCooldown
    global lastTime
    global dwidth
    global dheight
    global diffX
    global diffY
    global redArrow
    global orangeArrow
    global yellowArrow
    global gArrow
    global bArrow
    global whiteArrow
    global aquaArrow
    global lightGreenArrow
    global deepBlueArrow
    global purpleArrow
    global pinkArrow
    global gift
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global s1c
    global s2c
    global s3c
    global s4c
    global s5c
    global s6c
    global s7c
    global s8c,s9c,s10c,s1x,s2x,s3x,s4x,s5x,s6x,s7x,s8x,s9x,s10x,s1t,s2t,s3t,s4t,s5t,s6t,s7t,s8t,s9t,s10t
    global stage
    global firstTime
    global probability
    global c
    global isDouble, doubleTime
    global dead
    global isInvinc
    global usedInvinc
    global invincTime
    global c1c, c1y, cslot1, c1t, c1s,c2c, c2y, cslot2, c2t, c2s,c3c, c3y, cslot3, c3t, c3s
    global isSlow
    global usedSlow
    global slowTime
    global isTeleport, usedTeleport, teleportTime
    global s1s, s2s,s3s,s4s,s5s,s6s,s7s,s8s,s9s,s10s
    global frames
    global portal
    global currentTime, teleportDelay
    global usedSlowSound
    global slot11, slot12, slot13, slot14, s11c, s12c, s13c, s14c, s11y, s12y, s13y, s14y, s11t, s12t, s13t, s14t, s11s, s12s, s13s, s14s, s11sd, s12sd, s13sd, s14sd
    global bonus
    global passed, levelUnlocked, level5Complete
    shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
    snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
    portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
    currentTime = pygame.time.get_ticks()
    firstTime = pygame.time.get_ticks()
    slot1 = True
    s1x = 0
    slt = None
    s1c = None
    slot2 = True
    s2x = 0
    s2t = None
    s2c = None
    slot3 = True
    s3x = 0
    s3t = None
    s3c = None
    slot4 = True
    s4x = 0
    s4t = None
    s4c = None
    slot5 = True
    s5x = 0
    s5t = None
    s5c = None
    slot6 = True
    s6x = 0
    s6t = None
    s6c = None
    slot7 = True
    s7x = 0
    s7t = None
    s7c = None
    slot8 = True
    s8x = 0
    s8t = None
    s8c = None
    slot9 = True
    s9x = 0
    s9t = None
    s9c = None
    slot10 = True
    s10x = 0
    s10t = None
    s10c = None
    cslot1 = True
    c1y = 0
    c1t = None
    c1c = None
    c1s = None
    cslot2 = True
    c2y = 0
    c2t = None
    c2c = None
    c2s = None
    cslot3 = True
    c3y = 0
    c3t = None
    c3c = None
    c3s = None
    s1s = False
    s2s = False
    s3s = False
    s4s = False
    s5s = False
    s6s = False
    s7s = False
    s8s = False
    s9s = False
    s10s = False
    s11s = False
    s12s = False
    s13s = False
    s14s = False
    slot11 = True
    s11y = 0
    sllt = None
    s11c = None
    slot12 = True
    s12y = 0
    sl2t = None
    s12c = None
    slot13 = True
    s13y = 0
    sl3t = None
    s13c = None
    slot14 = True
    s14y = 0
    sl4t = None
    s14c = None
    s11sd = None
    s12sd = None
    s13sd = None
    s14sd = None
    isInvinc = False
    usedInvinc = False
    invincTime = None
    isSlow = False
    usedSlow = False
    slowTime = None
    isTeleport = False
    usedTeleport = False
    teleportTime = None
    teleportDelay = 0
    frames = 50
    skyBlue = (88, 173, 245)
    isDouble = False
    doubleTime = 0
    bonus = 0
    while not crashed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        currentTime = pygame.time.get_ticks() - teleportDelay
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and usedInvinc == False and isInvinc == False:
                pygame.mixer.Channel(0).play(invincSound)
                isInvinc = True
                invincTime = currentTime
                shield = pygame.transform.scale(shield, (60, 60))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and usedSlow == False and isSlow == False or event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and usedSlow == False and isSlow == False:
                pygame.mixer.Channel(1).play(slowDownSound)
                usedSlowSound = False
                isSlow = True
                slowTime = currentTime
                snail = pygame.transform.scale(snail, (94, 68))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and usedTeleport == False and isTeleport == False:
                isTeleport = True
                teleportTime = currentTime
                portal = pygame.transform.scale(portal, (90, 90))
                placeBird(portal, 18, dheight - 285)
                pygame.display.update()
                while isTeleport:
                    if pygame.time.get_ticks() - teleportTime >= 5000:
                        isTeleport = False
                        usedTeleport = True
                        teleportDelay += 5000
                        portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pygame.mixer.Channel(2).play(teleportSound)
                            x = pygame.mouse.get_pos()[0] - 75
                            y = pygame.mouse.get_pos()[1] - 75
                            isTeleport = False
                            usedTeleport = True
                            portal = pygame.transform.scale(pygame.image.load('portal2.png'), (70, 70))
                            teleportDelay += (pygame.time.get_ticks() - teleportDelay - teleportTime)
                    clock.tick(60)


            ##print(event)

            ##if event.type == pygame.MOUSEMOTION:
        if((pygame.mouse.get_pos()[0] < 1280 - b) and (pygame.mouse.get_pos()[0] > b) and (pygame.mouse.get_pos()[1] < 720 - b) and (pygame.mouse.get_pos()[1] > b)):
                    ##x = pygame.mouse.get_pos()[0] - 75
                    ##y = pygame.mouse.get_pos()[1] - 75
            diffX = (pygame.mouse.get_pos()[0] - 75) - x
            diffY = (pygame.mouse.get_pos()[1] - 75) - y
            x += 6/fps*diffX
            y += 6/fps*diffY

        if isInvinc:
            if currentTime - invincTime >= 4500 and currentTime - invincTime <= 5000:
                usedInvinc = True
            elif currentTime - invincTime <= 5500:
                usedInvinc = False
            elif currentTime - invincTime <= 6000:
                usedInvinc = True
            elif currentTime - invincTime <= 6250:
                usedInvinc = False
            elif currentTime - invincTime <= 6500:
                usedInvinc = True
            elif currentTime - invincTime <= 6750:
                usedInvinc = False
            elif currentTime - invincTime <= 7000:
                usedInvinc = True
            if currentTime - invincTime >= 7000:
                shield = pygame.transform.scale(pygame.image.load('shield.png'), (50, 50))
                invincTime = 0
                isInvinc = False
                usedInvinc = True
        if isSlow:
            if frames > 0 and currentTime - slowTime <= 1000:
                greenMaker((0, 194, 103), skyBlue)
            if currentTime - slowTime >= 9500 and currentTime - slowTime <= 10000:
                usedSlow = True
            elif currentTime - slowTime <= 10500:
                usedSlow = False
            elif currentTime - slowTime <= 11000:
                usedSlow = True
                frames = 50
            elif currentTime - slowTime <= 11250:
                usedSlow = False
            elif currentTime - slowTime <= 11500:
                usedSlow = True
            elif currentTime - slowTime <= 11750:
                usedSlow = False
            elif currentTime - slowTime <= 12000:
                usedSlow = True
            if currentTime - slowTime >= 12000:
                snail = pygame.transform.scale(pygame.image.load('snail.png'), (82, 59))
                slowTime = 0
                isSlow = False
                usedSlow = True
                frames = 50
        if isSlow and currentTime - slowTime >= 12000 - 1200*(frames/100):
            greenMaker((88, 173, 245), skyBlue)
        if isSlow and currentTime - slowTime >= 10950 and not usedSlowSound :
            pygame.mixer.Channel(3).play(speedUpSound)
            usedSlowSound = True
        if not isInvinc:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        flipStatus = False
        else:
            if pygame.mouse.get_pos()[0] - 75 < x - 30:
                if not flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = True
            elif pygame.mouse.get_pos()[0] - 75 >= x + 30:
                if flipStatus:
                    if currentTime - lastFlip > flipCooldown:
                        birdt = pygame.transform.flip(birdt, True, False)
                        f1t = pygame.transform.flip(f1t, True, False)
                        f2t = pygame.transform.flip(f2t, True, False)
                        f3t = pygame.transform.flip(f3t, True, False)
                        f4t = pygame.transform.flip(f4t, True, False)
                        bird = pygame.transform.flip(bird, True, False)
                        f1 = pygame.transform.flip(f1, True, False)
                        f2 = pygame.transform.flip(f2, True, False)
                        f3 = pygame.transform.flip(f3, True, False)
                        f4 = pygame.transform.flip(f4, True, False)
                        flipStatus = False


        gameDisplay.fill(skyBlue)
##        placeBird(landscape, 0, 650)

        momo = int((random.random())*1000 + 1)
        if momo <= probability2:
            if(cslot1):
                c1t=currentTime
                c1c = cloudChooser()
                c1s = random.random()*80 + 120
                c1y = random.random()* 70 + 60
                cslot1 = False
                cloudGen(c1c, c1y, 1, c1t, c1s)
            elif(cslot2):
                c2t=currentTime
                c2c = cloudChooser()
                c2s = random.random()*80 + 80
                c2y = random.random()* 70 + 40
                cslot2 = False
                cloudGen(c2c, c2y, 2, c2t, c2s)
            if(cslot3):
                c3t=currentTime
                c3c = cloudChooser()
                c3s = random.random()*80 + 40
                c3y = random.random()* 70 + 20
                cslot3 = False
                cloudGen(c3c, c3y, 3, c3t, c3s)

        if not cslot1:
            cloudGen(c1c, c1y, 1, c1t, c1s)
        if not cslot2:
            cloudGen(c2c, c2y, 2, c2t, c2s)
        if not cslot3:
            cloudGen(c3c, c3y, 3, c3t, c3s)

        if not usedInvinc:
            if not isInvinc:
                placeBird(shield, 35, dheight - 130)
            else:
                placeBird(shield, 30, dheight - 135)

        if not usedSlow:
            if not isSlow:
                placeBird(snail, 23, dheight - 195)
            else:
                placeBird(snail, 17, dheight - 200)

        if not usedTeleport:
            placeBird(portal, 28, dheight - 275)



        if not isInvinc:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flapWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flapWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flapWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flapWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(bird, x,y)
                    c = bird
            else:
                placeBird(bird, x,y)
        else:
            if (currentTime - lastTime) > cooldown:
                if (currentTime - lastTime) < cooldown + flapCooldown/5:
                    c = flaptWing(1)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 2*flapCooldown/5:
                    c = flaptWing(2)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 3*flapCooldown/5:
                    c = flaptWing(3)
                    placeBird(c, x,y)
                elif (currentTime - lastTime) < cooldown + 4*flapCooldown/5:
                    c = flaptWing(4)
                    placeBird(c, x,y)
                else:
                    lastTime = currentTime
                    placeBird(birdt, x,y)
                    c = birdt
            else:
                placeBird(birdt, x,y)




        elTime = (currentTime - firstTime)/1000

        if elTime < 15:
            stage = 20
            probability = 2500/fps
            probabilityt = 700/fps
        elif elTime < 30:
            stage = 20
            probability = 2800/fps
            probabilityt = 850/fps
        elif elTime < 60:
            stage = 20
            probability = 3200/fps
            probabilityt = 1000/fps


        if elTime < 58:
            r = int((random.random())*1000 + 1)
            if r <= probability:
                if slot1:
                    s1t = currentTime
                    s1c = whiteArrow
                    s1x = int((random.random())*1280 + 1)
                    s1s = isSlow
                    arrowSpawn(s1c, s1t, s1x, 1, s1s)
                    slot1 = False
                elif slot2:
                    s2t = currentTime
                    s2x = int((random.random())*1280 + 1)
                    s2c = whiteArrow
                    s2s = isSlow
                    arrowSpawn(s2c, s2t, s2x, 2, s2s)
                    slot2 = False
                elif slot3:
                    s3t = currentTime
                    s3x = int((random.random())*1280 + 1)
                    s3c = whiteArrow
                    s3s = isSlow
                    arrowSpawn(s3c, s3t, s3x, 3, s3s)
                    slot3 = False
                elif slot4:
                    s4t = currentTime
                    s4x = int((random.random())*1280 + 1)
                    s4c = whiteArrow
                    s4s = isSlow
                    arrowSpawn(s4c, s4t, s4x, 4, s4s)
                    slot4 = False
                elif slot5:
                    s5t = currentTime
                    s5x = int((random.random())*1280 + 1)
                    s5c = whiteArrow
                    s5s = isSlow
                    arrowSpawn(s5c, s5t, s5x, 5, s5s)
                    slot5 = False
                elif slot6:
                    s6t = currentTime
                    s6x = int((random.random())*1280 + 1)
                    s6c = whiteArrow
                    s6s = isSlow
                    arrowSpawn(s6c, s6t, s6x, 6, s6s)
                    slot6 = False
                elif slot7:
                    s7t = currentTime
                    s7x = int((random.random())*1280 + 1)
                    s7c = whiteArrow
                    s7s = isSlow
                    arrowSpawn(s7c, s7t, s7x, 7, s7s)
                    slot7 = False
                elif slot8:
                    s8t = currentTime
                    s8x = int((random.random())*1280 + 1)
                    s8c = whiteArrow
                    s8s = isSlow
                    arrowSpawn(s8c, s8t, s8x, 8, s8s)
                    slot8 = False
                elif slot9:
                    s9t = currentTime
                    s9x = int((random.random())*1280 + 1)
                    s9c = whiteArrow
                    s9s = isSlow
                    arrowSpawn(s9c, s9t, s9x, 9, s9s)
                    slot9 = False
                elif slot10:
                    s10t = currentTime
                    s10x = int((random.random())*1280 + 1)
                    s10c = whiteArrow
                    s10s = isSlow
                    arrowSpawn(s10c, s10t, s10x, 10, s10s)
                    slot10 = False
            if stage >= 5:
                rn = int((random.random())*1000 + 1)
                if rn <= probabilityt:
                    if slot11:
                        s11t = currentTime
                        s11c = whiteArrow
                        s11y = int((random.random())*600 + 1)
                        s11s = isSlow
                        s11sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
                        slot11 = False
                    elif slot12:
                        s12t = currentTime
                        s12y = int((random.random())*600 + 1)
                        s12c = whiteArrow
                        s12s = isSlow
                        s12sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
                        slot12 = False
                    elif slot13:
                        s13t = currentTime
                        s13y = int((random.random())*600 + 1)
                        s13c = whiteArrow
                        s13s = isSlow
                        s13sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
                        slot13 = False
                    elif slot14:
                        s14t = currentTime
                        s14y = int((random.random())*600 + 1)
                        s14c = whiteArrow
                        s14s = isSlow
                        s14sd = int(random.random()*2 + 1)
                        sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)
                        slot14 = False

        if not slot1:
            arrowSpawn(s1c, s1t, s1x, 1, s1s)
        if not slot2:
            arrowSpawn(s2c, s2t, s2x, 2, s2s)
        if not slot3:
            arrowSpawn(s3c, s3t, s3x, 3, s3s)
        if not slot4:
            arrowSpawn(s4c, s4t, s4x, 4, s4s)
        if not slot5:
            arrowSpawn(s5c, s5t, s5x, 5, s5s)
        if not slot6:
            arrowSpawn(s6c, s6t, s6x, 6, s6s)
        if not slot7:
            arrowSpawn(s7c, s7t, s7x, 7, s7s)
        if not slot8:
            arrowSpawn(s8c, s8t, s8x, 8, s8s)
        if not slot9:
            arrowSpawn(s9c, s9t, s9x, 9, s9s)
        if not slot10:
            arrowSpawn(s10c, s10t, s10x, 10, s10s)
        if not slot11:
            sideArrowSpawn(s11c, s11t, s11y, 11, s11s, s11sd)
        if not slot12:
            sideArrowSpawn(s12c, s12t, s12y, 12, s12s, s12sd)
        if not slot13:
            sideArrowSpawn(s13c, s13t, s13y, 13, s13s, s13sd)
        if not slot14:
            sideArrowSpawn(s14c, s14t, s14y, 14, s14s, s14sd)

        if isDouble:
            placeBird(doublePoints, 120, dheight - 55)
            bonus += ((elTime * 1.005**elTime) - ((elTime - 1) * 1.005**(elTime - 1)))/fps
            if currentTime - doubleTime >= 20000:
                isDouble = False

        score = round((elTime/60)*100)
        message_display("Completion: " + str(score) + "%" , 10, 1.05, 30, "franklingothicdemicond")

        if elTime >= 60:
            passed = True
            if levelUnlocked == 5:
                level5Complete = True
            break





        pygame.display.update()
        clock.tick_busy_loop()
##        if round(currentTime - firstTime) % 5000 > 0 and round(currentTime - firstTime) % 5000 < 100:
##            print(clock.get_fps())

    if passed:
        successLoop()
    else:
        dead = True
        deathLoop()

def deathLoop():
    global dead
    global crashed
    global c1
    global score
    message_display("Game Over", 2, 4, 150, "franklingothicdemicond")
    message_display("Press Q to quit", 2, 2.45, 30, "georgia")
    message_display("Click anywhere to restart", 2, 2.15, 30, "georgia")
    pygame.display.update()
    while dead:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dead = False
                crashed = False
                c1 = False
##                time.sleep(0.2)
                selectionLoop()

def successLoop():
    global dead
    global crashed
    global c1
    global score
    global passed
    message_display("Level Complete!", 2, 4, 130, "franklingothicdemicond")
    message_display("Press Q to quit", 2, 2.45, 30, "georgia")
    message_display("Click anywhere to proceed", 2, 2.15, 30, "georgia")
    pygame.display.update()
    while passed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                passed = False
                crashed = False
                c1 = False
##                time.sleep(0.2)
                selectionLoop()

def selectionLoop():
    global skyBlue
    global levelUnlocked
    global level5Complete
    skyBlue = (88, 173, 245)
    selected = False
    while not selected:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                rulesLoop()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.mouse.get_pos()[0] > 55 and pygame.mouse.get_pos()[0] < 55 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155 and levelUnlocked >= 1:
                    levelOne()
                elif pygame.mouse.get_pos()[0] > 295 and pygame.mouse.get_pos()[0] < 295 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155 and levelUnlocked >= 2:
                    levelTwo()
                elif pygame.mouse.get_pos()[0] > 535 and pygame.mouse.get_pos()[0] < 535 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155 and levelUnlocked >= 3:
                    levelThree()
                elif pygame.mouse.get_pos()[0] > 775 and pygame.mouse.get_pos()[0] < 775 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155 and levelUnlocked >= 4:
                    levelFour()
                elif pygame.mouse.get_pos()[0] > 1015 and pygame.mouse.get_pos()[0] < 1015 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155 and levelUnlocked >= 5:
                    levelFive()
                elif pygame.mouse.get_pos()[0] > 490 and pygame.mouse.get_pos()[0] < 490 + 300 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 450 + 155:
                    gameLoop()

        gameDisplay.fill(skyBlue)
        message_display("Press ESC to quit", 15, 1.03, 20, "georgia")
        message_display("Press R for how to play", 1.1, 1.03, 20, "georgia")
        message_display("Level Select", 2, 8, 130, "franklingothicdemicond")
        if levelUnlocked == 1:
            placeBird(levelLight, 55, 250)
        elif levelUnlocked > 1:
            placeBird(levelBlue, 55, 250)
        else:
            placeBird(levelRed, 55, 250)
        if levelUnlocked == 2:
            placeBird(levelLight, 295, 250)
        elif levelUnlocked > 2:
            placeBird(levelBlue, 295, 250)
        else:
            placeBird(levelRed, 295, 250)
        if levelUnlocked == 3:
            placeBird(levelLight, 535, 250)
        elif levelUnlocked > 3:
            placeBird(levelBlue, 535, 250)
        else:
            placeBird(levelRed, 535, 250)
        if levelUnlocked == 4:
            placeBird(levelLight, 775, 250)
        elif levelUnlocked > 4:
            placeBird(levelBlue, 775, 250)
        else:
            placeBird(levelRed, 775, 250)
        if levelUnlocked == 5:
            placeBird(levelLight, 1015, 250)
        elif level5Complete:
            placeBird(levelBlue, 1015, 250)
        else:
            placeBird(levelRed, 1015, 250)
        placeBird(endlessLight, 490, 450)
        if pygame.mouse.get_pos()[0] > 55 and pygame.mouse.get_pos()[0] < 55 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155:
            if levelUnlocked == 1:
                placeBird(level, 55, 250)
            elif levelUnlocked > 1:
                placeBird(levelDarkBlue, 55, 250)
            else:
                placeBird(levelRed, 55, 250)
        elif pygame.mouse.get_pos()[0] > 295 and pygame.mouse.get_pos()[0] < 295 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155:
            if levelUnlocked == 2:
                placeBird(level, 295, 250)
            elif levelUnlocked > 2:
                placeBird(levelDarkBlue, 295, 250)
            else:
                placeBird(levelRed, 295, 250)
        elif pygame.mouse.get_pos()[0] > 535 and pygame.mouse.get_pos()[0] < 535 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155:
            if levelUnlocked == 3:
                placeBird(level, 535, 250)
            elif levelUnlocked > 3:
                placeBird(levelDarkBlue, 535, 250)
            else:
                placeBird(levelRed, 535, 250)
        elif pygame.mouse.get_pos()[0] > 775 and pygame.mouse.get_pos()[0] < 775 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155:
            if levelUnlocked == 4:
                placeBird(level, 775, 250)
            elif levelUnlocked > 4:
                placeBird(levelDarkBlue, 775, 250)
            else:
                placeBird(levelRed, 775, 250)
        elif pygame.mouse.get_pos()[0] > 1015 and pygame.mouse.get_pos()[0] < 1015 + 210 and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 250 + 155:
            if levelUnlocked == 5:
                placeBird(level, 1015, 250)
            elif levelUnlocked > 5:
                placeBird(levelDarkBlue, 1015, 250)
            else:
                placeBird(levelRed, 1015, 250)
        elif pygame.mouse.get_pos()[0] > 490 and pygame.mouse.get_pos()[0] < 490 + 300 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 450 + 155:
            placeBird(endless, 490, 450)

        message_display("1", 8, 2.198, 40, "georgia")
        message_display("2", 3.2, 2.198, 40, "georgia")
        message_display("3", 2, 2.198, 40, "georgia")
        message_display("4", 1.4545, 2.198, 40, "georgia")
        message_display("5", 1.143, 2.198, 40, "georgia")
        message_display("Endless", 2, 1.365, 40, "georgia")
        pygame.display.update()
        clock.tick(60)
def rulesLoop():
    global skyBlue
    global rules
    ruleSet = False
    while not ruleSet:
        gameDisplay.fill(skyBlue)
        placeBird(rules, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                selectionLoop()
                ruleSet = True
        pygame.display.update()



titleLoop()
selectionLoop()
pygame.quit()
