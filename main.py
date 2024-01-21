import json

import pygame
import time
import shoot
import ufoner
import bullet

def start_game():
    def read_data():
        global settings
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)


    read_data()

    pygame.init()
    window = pygame.display.set_mode((800,500))





    fone = pygame.image.load("1626767990_23-kartinkin-com-p-galakticheskii-fon-krasivo-36.jpg")



    fps = pygame.time.Clock()

    n = 0
    startTime = time.time()
    timer = int(time.time()-startTime)
    timeText = pygame.font.Font(None, 56).render("Час:" + str(timer), True,(0,0,0))


    level = 1
    leveltext = pygame.font.Font(None, 56).render("Левел:" + str(level), True,(0,0,0))
    losetext = pygame.font.Font(None, 56).render("Ти програв:", True,(0,0,0))
    Wintext = pygame.font.Font(None, 56).render("Ти виграв :", True,(0,0,0))

    chel = shoot.shoot(48,437,50,60,1,settings["skin"])
    chel = shoot.shoot(48,437,50,60,1,("rocked.png"))

    enemies = []
    emo = []
    enemies.append(ufoner.ufoner(50, 0,50,50,1,"asteroid (1).png"))
    enemies.append(ufoner.ufoner(123, 0,50,50,1,"asteroid (1).png"))
    enemies.append(ufoner.ufoner(233, 42,50,50,1,"asteroid (1).png"))
    enemies.append(ufoner.ufoner(332, 6,50,50,1,"asteroid (1).png"))
    enemies.append(ufoner.ufoner(445, 10,50,50,1,"asteroid (1).png"))


    game = True



    while game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        chel.muve()

        if len(enemies) == 0:
            level += 1
            leveltext = pygame.font.Font(None, 56).render("Левел:" + str(level), True, (0, 0, 0))

        timer = int(time.time() - startTime)
        timeText = pygame.font.Font(None, 56).render("Час:" + str(timer), True, (0, 0, 0))

        for enemy in enemies:
            enemy.muve()
        window.fill((123,123,123))

        for enemy in enemies:
            if enemy.hit_box.colliderect((chel.hit_box)):
                game = False






        window.blit(fone, (0, 0))
        chel.render(window)
        for i in range(len(enemies)):
            enemies[i].render(window)
        window.blit(timeText, [0, 0])

        window.blit(leveltext, [150, 0])

        for enemy in enemies:
            enemy.render(window)

        for enemy in enemies:

         for p in chel.bullets:

          for i in range(len(enemies)):
            if enemies[i].rect.y > 500:
                window.fill((255, 0, 0))
                window.blit(losetext, [100, 100])
            if timer > 60:
                window.fill((0, 255, 0))
                window.blit(Wintext, [100, 100])
                game = False
        pygame.display.flip()
        fps.tick()