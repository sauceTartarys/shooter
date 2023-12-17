import pygame


class shoot:
    def __init__(self, x, y,w,h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture,(w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture,(w,h))

    def render(self, window):
        pygame.draw.rect(window,(255,0,0), self.hit_box)
        window.blit(self.texture,( self.hit_box.x,  self.hit_box.y))


    def muve(self):
        keys = pygame.key.get_pressed()
        is_step = False
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
            is_step = True
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed
            is_step = True

