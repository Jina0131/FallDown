"""
귀여운 낙서 판 PNG는 pu_cha에 의해 설계되었고,에서 유래되었다. <a href="https://kor.pngtree.com"> Pngtree.com</a>
"""

import pygame
import random

def blk_xy(b_y, to_y=0):
    if b_y>-120:
        b_y -=to_y +15
    else:
        b_y=960
    return b_y



class player:
    def __init__(self, body, speed, pos=(0, 0)):
        self.body = body
        self.speed = speed
        self.pos = pos








pygame.init()

WHITE = (255, 255, 255)
done = False
clock = pygame.time.Clock()

screen = pygame.display.set_mode([640, 960])

chrcterBody = pygame.image.load("C://falldown//heart.png")
chrcterBody = pygame.transform.scale(chrcterBody, (120, 90))
chrcter = player(chrcterBody, 15)

blkRight = pygame.image.load("C://falldown//leaf.png")
blkRight = pygame.transform.scale(blkRight, (210, 120))

blkLeft = pygame.image.load("C://falldown//leaf2.png")
blkLeft = pygame.transform.scale(blkLeft, (210, 120))

blkCenter = pygame.image.load("C://falldown//flower.png")
blkCenter = pygame.transform.scale(blkCenter, (180, 120))

def runGame():
    global done, chrcter, blkRight, blkLeft, blkCenter
    x, y = 260, 24
    br_x, br_y = 450, 960
    bl_x, bl_y = -10, 960
    bc_x, bc_y = 250, 960
    to_x = 0

    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and x>50:
                 to_x -=15
                elif (event.key ==pygame.K_RIGHT) and x<330:
                    to_x +=15
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
    
        x +=to_x
        
        br_y = blk_xy(br_y)
        bl_y = blk_xy(bl_y)
        bc_y = blk_xy(bc_y)
    
        screen.blit(chrcter.body, (x, y))
        screen.blit(blkRight, (br_x, br_y))
        screen.blit(blkLeft, (bl_x, bl_y))
        screen.blit(blkCenter, (bc_x, bc_y))
        pygame.display.update()


runGame()
pygame.quit()

    