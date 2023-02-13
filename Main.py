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
            self.rect.move_ip(8, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-8, 0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 15)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 700:
            self.rect.bottom = 700

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,100,100))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(1000, 1000),
                random.randint(300, 300),
            )
        )

    def update(self):
        self.rect.move_ip(-2, 0)
        if self.rect.left < 0:
            self.rect.left = 0
            self.rect.move_ip(0, 2)
        if self.rect.bottom >= 350:
            self.rect.move_ip(4, 0)
        if self.rect.right > 1000:
            self.rect.right = 1000
            self.rect.move_ip(0, 2)
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
            self.rect.move_ip(-4, 0)
                
                
                


pygame.init()

screen = pygame.display.set_mode([1000,750])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemyCount = 0
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)



    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    enemies.update()

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False

    screen.blit(player.surf, player.rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
