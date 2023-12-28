import pygame
import shoot
import ufoner
import bullet


window = pygame.display.set_mode((800,500))



fone = pygame.image.load("galaxy.jpg")



fps = pygame.time.Clock()


chel = shoot.shoot(48,437,50,60,1,("rocket.png"))
enemies = []
emo = []
enemies.append(ufoner.ufoner(50, 0,50,50,1,"asteroid (1).png"))
enemies.append(ufoner.ufoner(123, 0,50,50,1,"asteroid (1).png"))
enemies.append(ufoner.ufoner(233, 42,50,50,1,"asteroid (1).png"))


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


    for enemy in enemies:
        enemy.muve()
    window.fill((123,123,123))

    for enemy in enemies:
        if enemy.hit_box.colliderect((chel.hit_box)):
            game = False

        if enemy.hit_box.colliderect((chel.hit_box)):
            game = False

    window.blit(fone, (0, 0))
    chel.render(window)

    for enemy in enemies:
        enemy.render(window)
    pygame.display.flip()
    fps.tick()