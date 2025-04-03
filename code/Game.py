import sys

import pygame

from code.Level import font
from code.Menu import WHITE, WIDTH, HEIGHT, YELLOW, screen


class Game:

# Função principal para o jogo
def main():


# Criar grupos de sprites
all_sprites = pygame.sprite.Group()
Player = pygame.sprite.Group()
Laser = pygame.sprite.Group()

all_sprites.add(Player)


# Criar grupos de sprites
    all_sprites = pygame.sprite.Group()
    Enemy = pygame.sprite.Group()
    Laser = pygame.sprite.Group()


all_sprites.add(Enemy)

# Função para mostrar a mensagem de "Parabéns"
def show_congratulations():
    screen.fill(WHITE)
    congrats_text = font.render("Congratulations! You Killed 20 Zombies!", True, YELLOW)
    screen.blit(congrats_text, (WIDTH // 2 - congrats_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    pygame.time.wait(2000)  # Exibe a mensagem por 2 segundos



# Função para mostrar o Game Over
def show_game_over():
    screen.fill(WHITE)
    game_over_text = font.render("GAME OVER", True, YELLOW)
    restart_text = font.render("Press R To Restart", True, WHITE)
    quit_text = font.render("Press ESC To Exit", True, YELLOW)

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
    screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 1.5))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()