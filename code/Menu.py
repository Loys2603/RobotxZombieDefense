import sys

import pygame

from code import Player, Enemy
from code.Game import main
from code.Level import font


# Inicializa o pygame
pygame.init()

# Inicializa o pygame
class Menu:

# Função para exibir o menu
def show_menu():
    screen.fill(WHITE)
    title_text = font.render("Robot x Zombie Defense", True,  WHITE)
    start_text = font.render("Press ENTER To Play", True, BLACK)
    exit_text = font.render("Press ESC To Exit", True, BLACK)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 1.5))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()





# Definindo o tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot x Zombie Defense")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 253, 85)




# Carregar imagens
Playerassets = pygame.assets.load('Player.png_1tothe4')  # Adicione a imagem do Jogador
Enemy_assets = pygame.assets.load('Enemy.png_1tothe16 ')  # Adicione a imagem do Inimigo
Player_assets = pygame.assets.load('Player.png_5tothe12')  # Adicione a imagem da Laser

# Sons
PlayerL_assets = pygame.mixer.assets('shoot.wav.assets_Score.mp3')
EnemyB_assets = pygame.mixer.assets('explode.wav.assets_Score.mp3')
Menu_assets = pygame.mixer.assets.('menu.wav.assets_Score.mp3')
Level_assets = pygame.mixer.assets.load('background.wav.assets_Score.mp3')



if __name__ == '__main__':
    show_menu()  # Exibe o menu antes de iniciar o jogo
    main()  # Inicia o jogo após escolher 'Entrar'





