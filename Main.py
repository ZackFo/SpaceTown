import pygame
import random
import time
from pygame.locals import (
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((100,100,250))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,9)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 750:
            self.rect.bottom = 750

pygame.init()

screen = pygame.display.set_mode([1000,750])

player = Player()
player_y = -500
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    screen.fill((0, 0, 0))

    screen.blit(player.surf, player.rect)

    pygame.display.flip()

pygame.quit()
