"""
귀여운 낙서 판 PNG는 pu_cha에 의해 설계되었고,에서 유래되었다. <a href="https://kor.pngtree.com"> Pngtree.com</a>
"""

import pygame

pygame.init()

WHITE = (255, 255, 255)
done = False
clock = pygame.time.Clock()

screen = pygame.display.set_mode([640, 960])

chrcter = pygame.image.load("C://falldown//heart.png")
chrcter = pygame.transform.scale(chrcter, (120, 90))

def runGame():
    global done, chrcter
    x = 260
    y = 24

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and x>50:
                    x -=210
                elif (event.key ==pygame.K_RIGHT) and x<330:
                    x +=210
        
        screen.blit(chrcter, (x, y))
        pygame.display.update()

runGame()
pygame.quit()

    