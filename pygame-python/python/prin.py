from config import*
import pygame
pygame.init()

win = pygame.display.set_mode((swidth, sheight))

# for printing time


class prin(object):
    def scprin(self, crt):
        text = font.render(Time + str(crt // 1000), 100, (0, 0, 0))
        win.blit(text, (1150, 20))
