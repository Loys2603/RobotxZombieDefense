from random import random

import pygame

from code.Game import all_sprites
from code.Menu import WIDTH, HEIGHT, Enemy_assets


# Classe para os zumbis
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.assets = Enemy_assets
        self.rect = self.assets.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -50)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-150, -50)


# Criar zumbis
for _ in range(5):
    Enemy = Enemy()
    all_sprites.add(Enemy)
    Enemy.add(Enemy)

# Variáveis de controle
Enemy_kills = 0
running = True