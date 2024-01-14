import pygame

import bullet


class shoot:
    def __init__(self, x, y,w,h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture,(w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture,(w,h))
        self.bullets = []

    def render(self, window):
        pygame.draw.rect(window,(255,0,0), self.hit_box)
        window.blit(self.texture,( self.hit_box.x,  self.hit_box.y))
        for b in self.bullets:
            b.render(window)



    def muve(self):
        for b in self.bullets:
            b.muve()
        keys = pygame.key.get_pressed()
        is_step = False
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
            is_step = True
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed
            is_step = True
        if keys[pygame.K_o]:
            self.bullets.append(bullet.bullet(self.hit_box.x,  self.hit_box.y,20,20,1,("bullet.png")))



