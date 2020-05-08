import pygame
pygame.init()
# screen variables
swidth = 1600
sheight = 1000
pwid = 73
phei = 64
font = pygame.font.SysFont('comicsans', 50)
font1 = pygame.font.SysFont('comicsans', 100)
# all images
walkRight = [
    pygame.image.load('./img/R1.png'),
    pygame.image.load('./img/R2.png'),
    pygame.image.load('./img/R3.png'),
    pygame.image.load('./img/R4.png'),
    pygame.image.load('./img/R5.png'),
    pygame.image.load('./img/R6.png'),
    pygame.image.load('./img/R7.png'),
    pygame.image.load('./img/R8.png')]
walkLeft = [
    pygame.transform.flip(
        pygame.image.load('./img/R1.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R2.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R3.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R4.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R5.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R6.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R7.png'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/R8.png'),
        1,
        0)]

walkRight2 = [pygame.image.load('./img/DR1.png'),
              pygame.image.load('./img/DR2.png'),
              pygame.image.load('./img/DR3.png'),
              pygame.image.load('./img/DR4.png'),
              pygame.image.load('./img/DR5.png'),
              pygame.image.load('./img/DR6.png'),
              pygame.image.load('./img/DR7.png'),
              pygame.image.load('./img/DR8.png')]
walkleft2 = [pygame.transform.flip(pygame.image.load('./img/DR1.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR2.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR3.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR4.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR5.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR6.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR7.png'), 1, 0),
             pygame.transform.flip(pygame.image.load('./img/DR8.png'), 1, 0)]
bg = pygame.image.load('./img/back.png')
carleft1 = pygame.image.load('./img/LC1.jpg')
carright1 = pygame.image.load('./img/RC1.png')
carleft2 = pygame.image.load('./img/LC2.jpg')
carright2 = pygame.image.load('./img/RC2.png')
SR = pygame.image.load('./img/RS.jpg')
SL = pygame.transform.flip(pygame.image.load('./img/RS.jpg'), 1, 0)

frogright = [
    pygame.image.load('./img/RF1.gif'),
    pygame.image.load('./img/RF2.gif'),
    pygame.image.load('./img/RF3.gif'),
    pygame.image.load('./img/RF4.gif'),
    pygame.image.load('./img/RF5.gif'),
]
frogleft = [
    pygame.transform.flip(
        pygame.image.load('./img/RF1.gif'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/RF2.gif'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/RF3.gif'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/RF4.gif'),
        1,
        0),
    pygame.transform.flip(
        pygame.image.load('./img/RF5.gif'),
        1,
        0),
]
birdright = [pygame.image.load('./img/RB1.png'),
             pygame.image.load('./img/RB2.png'),
             pygame.image.load('./img/RB3.png'),
             pygame.image.load('./img/RB4.png'),
             pygame.image.load('./img/RB5.png'),
             pygame.image.load('./img/RB6.png'),
             pygame.image.load('./img/RB7.png'),
             pygame.image.load('./img/RB8.png'),
             pygame.image.load('./img/RB9.png'),
             pygame.image.load('./img/RB10.png'), ]
birdleft = [pygame.transform.flip(pygame.image.load('./img/RB1.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB2.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB3.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB4.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB5.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB6.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB7.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB8.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB9.png'), 1, 0),
            pygame.transform.flip(pygame.image.load('./img/RB10.png'), 1, 0), ]
B = pygame.image.load('./img/Bomb.png')
box = pygame.image.load('./img/Box.png')
Bombl = [
    pygame.image.load('./img/tile001.png'),
    pygame.image.load('./img/tile002.png'),
    pygame.image.load('./img/tile003.png'),
    pygame.image.load('./img/tile004.png'),
    pygame.image.load('./img/tile005.png'),
    pygame.image.load('./img/tile006.png'),
    pygame.image.load('./img/tile007.png'),
    pygame.image.load('./img/tile008.png'),
    pygame.image.load('./img/tile009.png'),
    pygame.image.load('./img/tile010.png'),
    pygame.image.load('./img/tile011.png'),
    pygame.image.load('./img/tile012.png')]
Boxbl = [pygame.image.load('./img/t1.png'),
         pygame.image.load('./img/t2.png'),
         pygame.image.load('./img/t3.png'),
         pygame.image.load('./img/t4.png'),
         pygame.image.load('./img/t5.png'),
         pygame.image.load('./img/t6.png'),
         pygame.image.load('./img/t7.png'),
         pygame.image.load('./img/t8.png'),
         pygame.image.load('./img/t9.png'),
         pygame.image.load('./img/t10.png'),
         pygame.image.load('./img/t11.png'),
         pygame.image.load('./img/t12.png'),
         pygame.image.load('./img/t13.png'),
         pygame.image.load('./img/t14.png'),
         pygame.image.load('./img/t15.png'),
         pygame.image.load('./img/t16.png'),
         pygame.image.load('./img/t17.png'),

         ]
Ruby = pygame.image.load('./img/RUBY.png')
# all strings
P1Score = 'P1 Score:'
P2Score = 'P2 Score:'
START = 'START'
END = 'END'
P1level = 'P1 level:'
P2level = 'P2 level:'
Time = 'Time:'
Player1win = 'Player1 win'
Player2win = 'Player2 win'
Tie = "It's a Tie"
# velocities of objects
car1velo = 10
car2velo = 12
shipvelo = 11
frogvelo = 13
birdvelo = 10
manvelo = 10
