import pygame, random

# Size of the screen
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

# Quantity of the lives
LIVES = 3

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Images
background_image = [None, '../images/backgroud/level1.jpg', '../images/backgroud/level2.jpg', '../images/backgroud/level3.jpg', '../images/backgroud/level4.jpg']
aliens_images = ['../images/invaders/purple.png', '../images/invaders/red-angle.png', '../images/invaders/yellow-icon.png', '../images/invaders/green-angle.png']
spaceship_image = "../images/spaceship.png"
alien_ship = '../images/alien_ship.png'

# Music
bacground_music = [None, "../music/background1.mp3", "../music/background2.mp3", "../music/background3.mp3", "../music/background4.mp3"]
shots_sound = "../music/laser.wav"
collision_sound = "../music/explosion.wav"

pygame.mixer.init()
collision_sound = pygame.mixer.Sound(collision_sound)
shots_sound = pygame.mixer.Sound(shots_sound)

# Set invaders settings
invaders_loop_shots = [None, 2500, 1750, 1000, 500]
invaders_speed_movement = [None, 3, 6, 12, 16]
invader_shot_speeed = 5
invaders_hieght_direction = [None, 10, 15, 20, 30]


# Set alien ships setting
alien_ship_score = [50,100,150,200]
alien_ship_loop_shots = 10000
alien_ship_speed = 8

# # Set spaceship settings
spaceship_shot_time_limit = 200
spaceship_shot_quantity_limit = 5
spaceship_speed = 10
spaceship_shot_speeed = -10

# Set player score per collision
shot_invader_score = [40, 25, 20, 10]
shot_score = 5

# Set massages settings
screen_massage_font = '../fonts/games/Games-Italic.ttf'
dinamic_massage_font = '../fonts/game_over/game_over.ttf'
score_massage_font = '../fonts/gameplay/Gameplay.ttf'
screen_massage_size = 80
dinamic_massage_size = 70
score_massage_size = 30


# Set blocks settings
size_block = 4
x_points = [170, 520, 870, 1220]
y_points = [600] * 4
color_block = (178,255,102)#'white'

shape = [
'       XXXXXXXXXXXXXX       ',
'     XXXXXXXXXXXXXXXXXX     ',
'    XXXXXXXXXXXXXXXXXXXX    ',
'   XXXXXXXXXXXXXXXXXXXXXX   ',
'  XXXXXXXXXXXXXXXXXXXXXXXX  ',
' XXXXXXXXXXXXXXXXXXXXXXXXXX ',
' XXXXXXXXXXXXXXXXXXXXXXXXXX ',
' XXXXXXXXX        XXXXXXXXX ',
' XXXXXXXXX        XXXXXXXXX ',
' XXXXXXXX          XXXXXXXX ',
' XXXXXXXX          XXXXXXXX ',
' XXXXXXXX          XXXXXXXX ',
' XXXXXXX            XXXXXXX ',
' XXXXXXX            XXXXXXX ',
]

