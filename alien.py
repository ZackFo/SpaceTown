import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color,x,y):
        file_path = color + ".png"
        super().__init__()
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

        if color == "Gunter": self.value = 100
        elif color == "Ricardio": self.value = 200
        else: self.value = 300

    def update(self,direction):
        self.rect.x += direction

class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load("Lady.png").convert_alpha()

        if side == "right":
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft = (x,80))

    def update(self):
        self.rect.x += self.speed
