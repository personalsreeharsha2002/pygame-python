from prin import*
from config import*
import pygame
pygame.init()
win = pygame.display.set_mode((swidth, sheight))
clock = pygame.time.Clock()

to1 = 1
to2 = 1

# class of players


class Player(object):
    pp1score = 0
    pp2score = 0
# constructor of this class

    def __init__(self, x, y, width, height, pp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = manvelo
        self.left = False
        self.right = False
        self.nomove = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.walkCount = 0
        self.pp = pp
# sprites of player
# it will load every image in a frame rate

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.nomove):
            if self.left:
                if self.pp == 1:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                else:
                    win.blit(walkleft2[self.walkCount // 3], (self.x, self.y))

                self.walkCount += 1
            elif self.right:
                if self.pp == 1:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    win.blit(walkRight2[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                if self.pp == 1:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkRight2[0], (self.x, self.y))
            else:
                if self.pp == 1:
                    win.blit(walkLeft[0], (self.x, self.y))
                else:
                    win.blit(walkleft2[0], (self.x, self.y))
        self.hitbox = (self.x + 16, self.y + 6, 40, 58)
# calculating score

    def calcsc(self, Score1, Score2, ll1, ll2):
        if self.pp == 1:
            self.pp1score = ((Score1 * (ll1 + 1)) - 1000*(to1 / 1000))
        if self.pp == 2:
            self.pp2score = ((Score2 * (ll2 + 1)) - 1000*(to2 / 1000))
# if player hits any obstacle
# then it comes to this function

    def hit(self, tt):
        global to1, to2
        if self.pp == 1:
            to1 += tt
        else:
            to2 += tt

        if self.pp == 2:
            if self.pp2score > self.pp1score:
                text = font1.render(Player2win, 1, (0, 0, 0))
                win.blit(text, (swidth // 2, sheight // 2))
                pygame.display.update()
            elif self.pp1score > self.pp2score:
                text = font1.render(Player1win, 1, (0, 0, 0))
                win.blit(text, (swidth // 2, sheight // 2))
                pygame.display.update()
            elif self.pp1score == self.pp2score:
                text = font1.render(Tie, 1, (0, 0, 0))
                win.blit(text, (swidth // 2, sheight // 2))
                pygame.display.update()
        pygame.time.Clock().tick(0.5)
        if self.pp == 1:
            self.x = swidth / 2 - swidth / 32
            self.y = sheight / 200
            self.pp = 2

        else:
            self.x = swidth / 2 - swidth / 32
            self.y = sheight - sheight / 10 - sheight / 200
            self.pp = 1

        to1 = to2 = 1
# if the player reaches the end
# then the player2 should appear
# for this thing it will come to
# this function

    def change(self, ttc):
        global to1, to2
        if self.pp == 1:
            to1 += ttc
        else:
            to2 += ttc
        if self.pp == 1:
            self.x = swidth / 2 - swidth / 32
            self.y = sheight // 500
            self.pp = 2
        else:
            self.x = swidth / 2 - swidth / 32
            self.y = sheight - sheight / 10 - sheight / 200
            self.pp = 1

# it is a class for bullets


class Bulletshoot(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
# it will draw every time when pressed space bar

    def bullet(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# class for cars


class Car(object):
    def __init__(self, x, y, vel, leftc, cn):
        self.x = x
        self.y = y
        self.leftc = leftc
        self.vel = vel
        self.cn = cn
        self.vis = True
        self.hitbox = (self.x, self.y, 120, 64)
# mov function for cars

    def go(self, spd):
        if self.cn == 1:
            if self.leftc:
                if self.x > self.vel + spd:
                    self.x -= self.vel + spd
                else:
                    self.leftc = False
            if not(self.leftc):
                if self.x < swidth - 120 - self.vel + spd:
                    self.x += self.vel + spd
                else:
                    self.leftc = True
            self.hitbox = (self.x, self.y, 120, 64)
        if self.cn == 2:

            if self.leftc:

                if self.x > self.vel + spd:
                    self.x -= self.vel + spd
                else:
                    self.leftc = False
            if not(self.leftc):

                if self.x < swidth - 120 - self.vel + spd:
                    self.x += self.vel + spd
                else:
                    self.leftc = True
            self.hitbox = (self.x, self.y, 120, 64)

# class for ship


class Ship(object):
    def __init__(self, x, y, vel, lefts):
        self.x = x
        self.y = y
        self.lefts = lefts
        self.vel = vel
        self.vis = True
        self.hitbox = (self.x + 5, self.y, 60, 64)
# mov function for ship

    def gos(self, spd):
        if self.lefts:
            if self.x > self.vel + spd:
                self.x -= self.vel + spd
            else:
                self.lefts = False
        if not(self.lefts):
            if self.x < swidth - 120 - self.vel + spd:
                self.x += self.vel + spd
            else:
                self.lefts = True
        self.hitbox = (self.x + 5, self.y, 60, 64)

# class for frog and fox


class Frog(object):
    def __init__(self, x, y, leftf, walkc, vel, fb):
        self.x = x
        self.y = y
        self.vel = vel
        self.leftf = leftf
        self.walkc = walkc
        self.fb = fb
        self.vis = True
        self.hitbox = (self.x, self.y, 64, 64)
# move funtion for frog and fox

    def gof(self, spd):
        if self.fb == 1:
            if self.walkc + 1 >= 15:
                self.walkc = 0
            if self.leftf:
                if self.x > self.vel + spd:
                    self.x -= self.vel + spd
                    self.walkc += 1
                else:
                    self.leftf = False
            else:
                if self.x < swidth - 70 - self.vel + spd:
                    self.x += self.vel + spd
                    self.walkc += 1
                else:
                    self.leftf = True
            self.hitbox = (self.x, self.y, 64, 64)
        if self.fb == 2:
            if self.walkc + 1 >= 30:
                self.walkc = 0
            if self.leftf:
                if self.x > self.vel + spd:
                    self.x -= self.vel + spd
                    self.walkc += 1
                else:
                    self.leftf = False
            else:
                if self.x < swidth - 120 - self.vel + spd:
                    self.x += self.vel + spd
                    self.walkc += 1
                else:
                    self.leftf = True
            self.hitbox = (self.x, self.y, 119, 64)

# class for bombs and boxes


class Bomb(object):
    def __init__(self, x, y, bo):
        self.x = x
        self.y = y
        self.bo = bo
        self.vis = True
        self.walkCount = 0
        self.rvis = False
        if self.bo == 1:
            self.hitbox = (self.x + 14, self.y + 10, 36, 44)
        else:
            self.hitbox = (self.x, self.y, 64, 64)
# when the bullets hit the bomb
# then this function will be called

    def blast(self):
        self.walkcount = 0

        if self.bo == 1:
            for i in range(108):
                if self.walkCount + 1 >= 108:
                    self.walkCount = 0

                win.blit(Bombl[self.walkCount // 9],
                         (self.x - 28, self.y - 28))
                pygame.display.update()
                self.walkCount += 1
        if self.bo == 2:
            self.vis = False
            self.rvis = True
            clock.tick(23)
            for i in range(153):
                if self.walkCount + 1 >= 153:
                    self.walkCount = 0

                win.blit(Boxbl[self.walkCount // 9],
                         (self.x - 32, self.y - 32))
                pygame.display.update()
                self.walkCount += 1
# when bullets hit the box
# then this funtio will be called

    def hit(self):
        self.rvis = False
