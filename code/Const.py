# Constantes com C
# Cores
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# Constantes com E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}


ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 2,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
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

# Constantes com T
TIMEOUT_LEVEL = 20000  # 20s
TIMEOUT_STEP = 100  # 100ms

# Constantes com W
# Tamanho da janela
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Constantes com S, pós WIN_WIDTH
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190)
}