import sys

import pygame

from code.Menu import screen, WHITE


class Score:

# Exibir o placar
score_text = font.render(f"Dead Zombies: {zombie_kills}", True, WHITE)
screen.blit(score_text, (10, 10))
pygame.display.flip()
pygame.quit()
sys.exit()


# Verificar colisões
for Enemy in Enemy:
    if pygame.sprite.spritecollide(Enemy, Laser, True):
        Enemy.rect.x = random.randint(0, WIDTH - Enemy.rect.width)
        Enemy.rect.y = random.randint(-150, -50)
        EnemyB_assets .play()
        Enemy_kills += 1




# Verificar se matou 20 zumbis
if Enemy_kills >= 20:
    show_congratulations()
    Enemy_kills = 0  # Reinicia o placar

    # Verificar se o robô foi pego
    if pygame.sprite.spritecollide(Player, Enemy, False):
        show_game_over()
        return  # Finaliza a partida, e volta para o menu

