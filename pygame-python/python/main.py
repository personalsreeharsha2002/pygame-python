from prin import*
from config import*
from classes import*
import pygame
pygame.init()
win = pygame.display.set_mode((swidth, sheight))


clock = pygame.time.Clock()

# Instruction window


def instruct():
    run = True
    subt = pygame.time.get_ticks()
    pygame.display.set_caption("Instructions")
    while run:
        win.blit(pygame.image.load('./img/ins.png'), (0, 0))
        pygame.display.update()
        kkey = pygame.key.get_pressed()
        if kkey[pygame.K_KP_ENTER]:
            stime = pygame.time.get_ticks() - subt
            return stime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

# Game


def game():
    pygame.display.set_caption("ENDGAME")
    man = Player(
        swidth /
        2 -
        swidth /
        32,
        sheight -
        sheight /
        10 -
        sheight /
        200,
        pwid,
        phei,
        1)
    Score1 = 0
    Score2 = 0
    level1 = 0
    level2 = 0
    # Objects of classes
    car1 = Car(0, 645, car1velo, False, 1)
    car2 = Car(1069, 822, car2velo, False, 2)
    ship = Ship(43, 114, shipvelo, False)
    frog = Frog(58, 468, False, 0, frogvelo, 1)
    bird = Frog(942, 291, False, 0, birdvelo, 2)
    bomb1 = Bomb(51, 203, 1)
    bomb2 = Bomb(1100, 203, 2)
    bomb3 = Bomb(68, 380, 1)
    bomb4 = Bomb(529, 380, 2)
    bomb5 = Bomb(1300, 380, 1)
    bomb6 = Bomb(697, 557, 1)
    bomb7 = Bomb(920, 557, 2)
    bomb8 = Bomb(227, 734, 1)
    bomb9 = Bomb(869, 734, 2)
    bomb10 = Bomb(1125, 734, 1)
    bullets = []
    rt1 = rt2 = rt3 = rt4 = rt5 = rt6 = False
    fl = False
    run = True
    arr = (
        car1,
        car2,
        ship,
        frog,
        bird,
        bomb1,
        bomb2,
        bomb3,
        bomb4,
        bomb5,
        bomb6,
        bomb7,
        bomb8,
        bomb9,
        bomb10)
    bls = (
        bomb1,
        bomb2,
        bomb3,
        bomb4,
        bomb5,
        bomb6,
        bomb7,
        bomb8,
        bomb9,
        bomb10)
    pre = 0
    ppr = prin()

# for every loop Updating the window
    def updateGameWindow():

        win.blit(bg, (0, 0))
        if car1.leftc:
            win.blit(carleft1, (car1.x, car1.y))
        else:
            win.blit(carright1, (car1.x, car1.y))

        if car2.leftc:
            win.blit(carleft2, (car2.x, car2.y))
        else:
            win.blit(carright2, (car2.x, car2.y))

        if ship.lefts:
            win.blit(SL, (ship.x, ship.y))
        else:
            win.blit(SR, (ship.x, ship.y))

        if frog.leftf:
            win.blit(frogleft[frog.walkc // 3], (frog.x, frog.y))
        else:
            win.blit(frogright[frog.walkc // 3], (frog.x, frog.y))

        if bird.leftf:
            win.blit(birdleft[bird.walkc // 3], (bird.x, bird.y))
        else:
            win.blit(birdright[bird.walkc // 3], (bird.x, bird.y))
        text = font.render(P1Score + str(man.pp1score), 100, (0, 0, 0))
        win.blit(text, (1320, 20))
        text = font.render(P2Score + str(man.pp2score), 100, (0, 0, 0))
        win.blit(text, (1320, 60))

        for u in bls:
            if u.bo == 1:
                win.blit(B, (u.x, u.y))
            else:
                if u.vis:
                    win.blit(box, (u.x, u.y))
                else:
                    if u.rvis:
                        win.blit(Ruby, (u.x, u.y))
        ppr.scprin(crt)
        man.draw(win)

        text1 = font.render(START, 100, (0, 0, 0))
        text2 = font.render(END, 100, (0, 0, 0))
        if man.pp == 1:
            win.blit(text1, (1350, 960))
            win.blit(text2, (360, 20))
        if man.pp == 2:
            win.blit(text2, (1350, 960))
            win.blit(text1, (360, 20))

        text = font.render(P1level + str(level1), 100, (0, 0, 0))
        win.blit(text, (130, 20))
        text = font.render(P2level + str(level2), 100, (0, 0, 0))
        win.blit(text, (130, 60))
        for i in bullets:
            i.bullet(win)

        pygame.display.update()

    gl = False
    t0 = pygame.time.get_ticks()
    while run:
        clock.tick(24)
# here I am calculating the hit box
# hit box of man and all obstacles
        for z in arr:
            if man.hitbox[1] < z.hitbox[1] + z.hitbox[3]:
                if man.hitbox[1] + man.hitbox[3] > z.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > z.hitbox[0]:
                        if man.hitbox[0] < z.hitbox[0] + z.hitbox[2]:
                            if z.vis:
                                t1 = pygame.time.get_ticks()
                                fl = True
                                man.hit(t1 - t0)
                                crt = 0

                                pre = pygame.time.get_ticks()
                                gl = True
                                rt1 = rt2 = rt3 = rt4 = rt5 = rt6 = False
                                if man.pp == 1:
                                    Score1 = level1 = level2 = Score2 = 0
                                for i in bls:
                                    i.vis = True
                                    i.rvis = False
                            else:
                                if z.rvis:
                                    z.hit()
                                    if man.pp == 1:
                                        Score1 += 10
                                    else:
                                        Score2 += 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
# here i am multplying levels with 8
# to increase the velocity after levels
        if man.pp == 1:
            car1.go(level1 * 8)
            car2.go(level1 * 8)
            ship.gos(level1 * 8)
            frog.gof(level1 * 8)
            bird.gof(level1 * 8)
        else:
            car1.go(level2 * 8)
            car2.go(level2 * 8)
            ship.gos(level2 * 8)
            frog.gof(level2 * 8)
            bird.gof(level2 * 8)
        # for hitting the bullets
        # As bullets will go to hitbox
        for i in bullets:
            for a in bls:
                if i.y - i.radius < a.hitbox[1] + \
                        a.hitbox[3] and i.y + i.radius > a.hitbox[1]:
                    if i.x + i.radius > a.hitbox[0] and i.x - \
                            i.radius < a.hitbox[0] + a.hitbox[2]:
                        if a.vis:
                            a.blast()

                            bullets.clear()
                            if a.bo == 1:
                                t1 = pygame.time.get_ticks()
                                fl = True
                                man.hit(t1 - t0)
                                crt = 0

                                pre = pygame.time.get_ticks()
                                gl = True
                                rt1 = rt2 = rt3 = rt4 = rt5 = rt6 = False

                                if man.pp == 1:
                                    Score1 = level1 = level2 = Score2 = 0
                                for j in bls:
                                    j.vis = True
                                    j.rvis = False
# direction of bullets is changing here
# according to player
            if man.pp == 1:
                if i.y < sheight and i.y > 0:
                    i.y -= i.vel
                else:
                    bullets.pop(bullets.index(i))
            else:
                if i.y < sheight and i.y > 0:
                    i.y += i.vel
                else:
                    bullets.pop(bullets.index(i))
# If they presses a key
# then it will function according to that
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            man.walkCount = 0
            if len(bullets) < 10:
                bullets.append(
                    Bulletshoot(
                        round(
                            man.x +
                            man.width //
                            2 -
                            man.width //
                            9),
                        round(
                            man.y),
                        4,
                        (0,
                         0,
                         0),
                        1))

        elif keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
        elif keys[pygame.K_RIGHT]and man.x < swidth - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
        elif keys[pygame.K_UP] and man.y > sheight // 200 + man.vel:
            man.y -= man.vel
        elif keys[pygame.K_DOWN]:
            if man.y + man.height < sheight - sheight // 200 - man.vel:
                man.y += man.vel
        else:
            if keys[pygame.K_ESCAPE]:
                inst = instruct()
                t0 += inst
                pre += inst
            man.nomove = 0
            man.walkCount = 0
# Increasing score when it passes obstacles
        if man.y > 886 and man.y < sheight:
            if not rt1:
                if man.pp == 1:
                    Score1 += 0
                else:
                    Score2 += 50
                rt1 = True
        elif man.y > 709 and man.y < 822:
            if not rt2:
                if man.pp == 1:
                    Score1 += 10
                else:
                    Score2 += 40
                rt2 = True
        elif man.y > 532 and man.y < 645:
            if not rt3:
                if man.pp == 1:
                    Score1 += 20
                else:
                    Score2 += 30
                rt3 = True
        elif man.y > 355 and man.y < 468:
            if not rt4:
                if man.pp == 1:
                    Score1 += 30
                else:
                    Score2 += 20
                rt4 = True
        elif man.y > 178 and man.y < 291:
            if not rt5:
                if man.pp == 1:
                    Score1 += 40
                else:
                    Score2 += 10
                rt5 = True
        elif man.y > 0 and man.y < 114:
            if not rt6:
                if man.pp == 1:
                    Score1 += 50
                else:
                    Score2 += 0
                rt6 = True
# If player goes to another side then
# another player should come
        if man.pp == 1 and man.y + man.height < 114:
            t1 = pygame.time.get_ticks()
            fl = True
            man.change(t1 - t0)
            crt = 0

            pre = pygame.time.get_ticks()
            gl = True
            rt1 = rt2 = rt3 = rt4 = rt5 = rt6 = False
            level1 += 1
            for i in bls:
                i.vis = True
                i.rvis = False
        elif man.pp == 2 and man.y > 886:
            t1 = pygame.time.get_ticks()
            fl = True
            man.change(t1 - t0)
            crt = 0

            pre = pygame.time.get_ticks()
            gl = True
            rt1 = rt2 = rt3 = rt4 = rt5 = rt6 = False
            level2 += 1
            for i in bls:
                i.vis = True
                i.rvis = False
        if not gl:
            crt = pygame.time.get_ticks() - pre
# calculting score every time
        man.calcsc(Score1, Score2, level1, level2)
        updateGameWindow()
        if fl:
            t0 = t1
            fl = False
        gl = False
    pygame.quit()

# Main menu window


def mainMenu():
    run = True
    pygame.display.set_caption("Main Menu")
# playing background music
    bgmusic = pygame.mixer.music.load('./img/bgforpy1fastestslow.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    while run:
        win.blit(pygame.image.load('./img/mainmenu.png'), (0, 0))
        pygame.display.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_i]:
            instruct()
        if key[pygame.K_KP_ENTER]:
            game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


mainMenu()
