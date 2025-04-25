# Constantes com C
# Cores
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_PRETO = (0, 0, 0)

# Constantes com E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

# Constantes com M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# Constantes com P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,        # move o Player1 para cima
                 'Player2': pygame.K_w}         # ídem, Player2
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,    # move o Player1 para baixo
                   'Player2': pygame.K_s}       # ídem, Player2
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,    # move o Player1 para a esquerda
                   'Player2': pygame.K_a}       # ídem, Player2
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,  # move o Player1 para a direita
                    'Player2': pygame.K_d}      # ídem, Player2
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,  # para o Player1 atacar
                    'Player2': pygame.K_LCTRL}  # ídem, Player2


# Constantes com S
SPAWN_TIME = 4000


# Constantes com W
# Tamanho da janela
WIN_WIDTH = 576
WIN_HEIGHT = 324
