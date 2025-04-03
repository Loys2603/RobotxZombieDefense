import pygame

from code.Game import all_sprites
from code.Menu import WIDTH, HEIGHT


# Classe para o robô
class Player_assets:
    pass


class Player:
    pass


 # Criar o robô
            Player = Player()


class Laser:
    pass


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Player_assets
        self.rect = self.assets.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        Laser = Laser(self.rect.centerx, self.rect.top)
        all_sprites.add(Laser)
        Laser.add(Laser)
        Player_assets.play()


