# okay lets do this
# uhhhh

import random
import pygame
from pypresence import Presence
from datetime import datetime
# v MY FILES v
from fhandler import conRead, startLog, log, endLog, randInit
from tzmath import hypoCalc, radToDeg, degToRad
from playerFuncs import Player

pygame.init()
screen = pygame.display.set_mode((160, 120),conRead("startup.con")[0])
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Null and Vøid | v0.0")
clock = pygame.time.Clock()
discID = "1241919126453227621"
pres = Presence(discID)
pres.connect()
running = True

rand = randInit()


print(rand)
lines=["Terrah is regretting her life choices.", "// why did i st4rt this 464in?", "This really sucks.", "What the FUCK is a binary space partition", "Shade and Furia have it easy. I have to code.", "Triple D! ...I hate it."]
line=random.choice(lines)

plyr = Player()

#startLog()
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    plyr.pUp()
    print(plyr.a)
    pygame.draw.line(screen,"black",(plyr.x,plyr.y),(plyr.dx,plyr.dy))
        
    pygame.display.flip()

    screen.fill("white") #remove this later, i love screen bleed
    
    pres.update(state=line,details="Coding...",large_image="lowrestrans",large_text="trans rights!")
    clock.tick(60) 
pygame.quit()
pres.close()
#endLog()

