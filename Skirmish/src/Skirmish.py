import pygame
from moviepy.editor import VideoFileClip
from Fighter import Fighter
import FighterData
from FighterData import ALL_FIGHTER_DATA
import os
import time
import random

# import Fighters
from King import King
from Sage import Sage
from DarkWizard import DarkWizard
from DeathHarbringer import DeathHarbringer
from FireWizard import FireWizard
from Huntress import Huntress
from Knight import Knight
from Monk import Monk
from Oni import Oni
from Rogue import Rogue
from Samurai import Samurai
from Soldier import Soldier
from Warrior import Warrior

pygame.init()

clock = pygame.time.Clock()
fps = 60

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
INTRO_TIME = 6 # set to 3-5 seconds later for the intro
# INTRO_TIME = 0
FADE_OUT_TIME = 5
BACKGROUND_FRAME_COOLDOWN = 2 # higher means frames will be slower

current_bg_frame_cd = 0
current_frame = 0

# map selection screen stuff
MAPS_DIRECTORY = os.path.abspath('../assets/bg/maps/')
chosen_map_index = 0
chosen_map_index = random.randint(0, 8)
maps_list = []

# char selection screen stuff
CHAR_DIRECTORY = os.path.abspath('../assets/FighterSprites/')
fighter1_list = []
fighter2_list = []
# selectors postion for characters
f1_selector_pos = 0
f2_selector_pos = 0

# check for keys
f1_attack_key1_state = False
f1_attack_key2_state = False
f1_attack_key3_state = False
f1_attack_key4_state = False

f2_attack_key1_state = False
f2_attack_key2_state = False
f2_attack_key3_state = False
f2_attack_key4_state = False

# intro stuff
fade_speed = 10
fade_alpha = 255
loading_finished = False
logo_x_pos = SCREEN_WIDTH
logo_y_pos = 0 - 300
fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.set_alpha(fade_alpha)

# get timer for the intro
program_start_timer = time.time()

# game state/screens
CHAR_SELECTION = 0
MAP_SELECTION = 1
IN_GAME = 2
GAME_OVER = 3
game_state = CHAR_SELECTION

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (178, 34, 34)
GREEN = (0,255,0)
TEAL = (0, 255, 255)
GREY = (187,186,181)
NAVY = (35,31,38)
TRANSPARENT = (0, 0, 0, 0)

def draw_stat_bar(amount, x, y, w, h, color):
    ratio = amount / 100
    pygame.draw.rect(screen, color, (x, y, w * ratio, h))

# initiate screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Skirmish')

# load background
for filename in os.listdir(MAPS_DIRECTORY):
    if filename != ".DS_Store":
        filepath = os.path.join(MAPS_DIRECTORY, filename)
        if os.path.isfile(filepath):
            vid = VideoFileClip(filepath)
            video_frames = [pygame.transform.scale(pygame.image.fromstring(frame.tobytes(), vid.size, "RGB"), (SCREEN_WIDTH, SCREEN_HEIGHT))
                        for frame in vid.iter_frames()]
            maps_list.append(video_frames)

# define constants for image dimensions and spacing
image_width, image_height = 300, 150
horizontal_spacing, vertical_spacing = 75, 35
# calculate the number of columns and rows
num_columns = (SCREEN_WIDTH - horizontal_spacing) // (image_width + horizontal_spacing)
# num_rows = (len(maps_list) + num_columns - 1) // num_columns

intro_logo = pygame.transform.scale(pygame.image.load('../assets/logo/logo3.png').convert_alpha(), (300, 300)).convert_alpha()

# load fighter sprites
for filename in os.listdir(CHAR_DIRECTORY):
    if filename != ".DS_Store":
        if filename.endswith(".png"):
            fighter_name = os.path.splitext(filename)[0]
            fighter_sheet = pygame.image.load(os.path.join(CHAR_DIRECTORY, filename)).convert_alpha()
            fighter_class = globals()[fighter_name]
            fighter1_instance = fighter_class(False, ALL_FIGHTER_DATA[fighter_name][0], fighter_sheet, ALL_FIGHTER_DATA[fighter_name][1])
            fighter2_instance = fighter_class(True, ALL_FIGHTER_DATA[fighter_name][0], fighter_sheet, ALL_FIGHTER_DATA[fighter_name][1])
            fighter1_list.append(fighter1_instance)
            fighter2_list.append(fighter2_instance)

# fighter_1 = fighter_list[1]
# fighter_2 = fighter_list[1]

fighter_1 = fighter1_list[0]
fighter_1.set_rect(200, 310)
fighter_2 = fighter2_list[0]
fighter_2.set_rect(700, 310)

placeholder_f1_hp = 500
f1_hp_wait = 500
placeholder_f2_hp = 500
f2_hp_wait = 500

key_delay = 150

run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # keys input for fighting
        if event.type == pygame.KEYDOWN:
            if game_state == IN_GAME:
                if event.key == pygame.K_r:
                    f1_attack_key1_state = True
                elif event.key == pygame.K_t:
                    f1_attack_key2_state = True
                elif event.key == pygame.K_f:
                    f1_attack_key3_state = True
                elif event.key == pygame.K_g:
                    f1_attack_key4_state = True
                if event.key == pygame.K_QUOTE:
                    f2_attack_key1_state = True
                elif event.key == pygame.K_SEMICOLON:
                    f2_attack_key2_state = True
                elif event.key == pygame.K_SLASH:
                    f2_attack_key3_state = True
                elif event.key == pygame.K_PERIOD:
                    f2_attack_key4_state = True
        if event.type == pygame.KEYUP:
            if game_state == IN_GAME:
                if event.key == pygame.K_r:
                    f1_attack_key1_state = False
                elif event.key == pygame.K_t:
                    f1_attack_key2_state = False
                elif event.key == pygame.K_f:
                    f1_attack_key3_state = False
                elif event.key == pygame.K_g:
                    f1_attack_key4_state = False
                if event.key == pygame.K_QUOTE:
                    f2_attack_key1_state = False
                elif event.key == pygame.K_SEMICOLON:
                    f2_attack_key2_state = False
                elif event.key == pygame.K_SLASH:
                    f2_attack_key3_state = False
                elif event.key == pygame.K_PERIOD:
                    f2_attack_key4_state = False
            if game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    game_state = CHAR_SELECTION


    if time.time() - program_start_timer > INTRO_TIME and loading_finished == True:

        # game intro is finished
        # character selection screen
        if game_state == CHAR_SELECTION:
            screen.fill(BLACK)
            f1_select_surf = pygame.Surface((SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            f2_select_surf = pygame.Surface((SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            
            f1_select_surf.blit(fighter1_list[f1_selector_pos].animation_list[0][0], (0, 0))
            f2_select_surf.blit(fighter2_list[f2_selector_pos].animation_list[0][0], (0, 0))

            screen.blit(f1_select_surf, (0, 0))
            screen.blit(f2_select_surf, (SCREEN_WIDTH // 2, 0))

            key = pygame.key.get_pressed()

            if key[pygame.K_a]:
                f1_selector_pos -= 1
                if f1_selector_pos < 0:
                    f1_selector_pos = len(fighter1_list) - 1
                pygame.time.wait(key_delay)
            elif key[pygame.K_d]:
                f1_selector_pos += 1
                if f1_selector_pos > len(fighter1_list) - 1:
                    f1_selector_pos = 0
                pygame.time.wait(key_delay)
            if key[pygame.K_LEFT]:
                f2_selector_pos -= 1
                if f2_selector_pos < 0:
                    f2_selector_pos = len(fighter2_list) - 1
                pygame.time.wait(key_delay)
            elif key[pygame.K_RIGHT]:
                f2_selector_pos += 1
                if f2_selector_pos > len(fighter2_list) - 1:
                    f2_selector_pos = 0
                pygame.time.wait(key_delay)

            if key[pygame.K_RETURN]:
                game_state = 1

            fighter_1 = fighter1_list[f1_selector_pos]
            fighter_1.set_rect(200, 310)
            fighter_2 = fighter2_list[f2_selector_pos]
            fighter_2.f2 = True
            fighter_2.set_rect(700, 310)

            placeholder_f1_hp = 500
            f1_hp_wait = 500
            placeholder_f2_hp = 500
            f2_hp_wait = 500
                
        # map selection screen
        elif game_state == MAP_SELECTION:

            # map selection background
            screen.fill(BLACK)

            # get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()

            # loop through list of maps to display
            for idx, map_image in enumerate(maps_list):
                row = idx // num_columns
                col = idx % num_columns

                x = col * (image_width + horizontal_spacing) + horizontal_spacing
                y = row * (image_height + vertical_spacing) + vertical_spacing

                # draw all maps
                screen.blit(pygame.transform.scale(map_image[0], (image_width, image_height)), (x, y))
                
                # highlighting selected map
                rect_width, rect_height, rect_offset = 310, 160, 5
                rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
                rect_surface.fill(TRANSPARENT)
                pygame.draw.rect(rect_surface, GREY, rect_surface.get_rect(), border_radius=10)
                
                rect_rect = pygame.Rect(x - rect_offset, y - rect_offset, rect_width, rect_height)
                
                if rect_rect.collidepoint(mouse_x, mouse_y):
                    rect_surface.set_alpha(150)
                    screen.blit(rect_surface, (x - rect_offset, y - rect_offset))
                    if mouse_buttons[0]:
                        chosen_map_index = idx
                        game_state = 2
                else:
                    rect_surface.set_alpha(50)
                    screen.blit(rect_surface, (x - rect_offset, y - rect_offset))

        # currently in game
        elif game_state == IN_GAME:

            # display video background
            frame_surface = maps_list[chosen_map_index][current_frame % len(maps_list[chosen_map_index])]

            # scaled_bg = pygame.transform.scale(frame_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(frame_surface, (0, 0))
            
            # HP bar of fighter 1
            pygame.draw.rect(screen, TEAL, (60, 10, placeholder_f1_hp, 30))
            if f1_hp_wait > fighter_1.health/100 * 500:
                f1_hp_wait -= 5
            elif placeholder_f1_hp > fighter_1.health/100 * 500:
                placeholder_f1_hp -= 2
            draw_stat_bar(fighter_1.health, 60, 10, 500, 30, RED)
            draw_stat_bar(fighter_1.stamina, 60, 40, 300, 15, GREEN)
            pygame.draw.rect(screen, GREY, (10, 10, 50, 45))
            pygame.draw.rect(screen, GREY, (60, 10, 500, 30), 2)

            # HP bar of fighter 2
            pygame.draw.rect(screen, TEAL, (SCREEN_WIDTH-10-500, 10, placeholder_f2_hp, 30))
            if f2_hp_wait > fighter_2.health/100 * 500:
                f2_hp_wait -= 5
            elif placeholder_f2_hp > fighter_2.health/100 * 500:
                placeholder_f2_hp -= 2
            draw_stat_bar(fighter_2.health, SCREEN_WIDTH-10-500, 10, 500, 30, RED)
            draw_stat_bar(fighter_2.stamina, SCREEN_WIDTH-10-500, 40, 300, 15, GREEN)
            pygame.draw.rect(screen, GREY, (SCREEN_WIDTH-50-10-500, 10, 50, 45))
            pygame.draw.rect(screen, GREY, (SCREEN_WIDTH-10-500, 10, 500, 30), 2)

            # update functions
            fighter_1.update(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, f1_attack_key1_state, f1_attack_key2_state, f1_attack_key3_state, f1_attack_key4_state)
            fighter_2.update(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, f2_attack_key1_state, f2_attack_key2_state, f2_attack_key3_state, f2_attack_key4_state)

            # update background frames
            if current_bg_frame_cd >= BACKGROUND_FRAME_COOLDOWN:
                current_frame += 1
                current_bg_frame_cd = 0
            current_bg_frame_cd += 1

        # game over screen
        elif game_state == GAME_OVER:
            screen.fill(BLACK)
            # reset selectors postion for next game
            f1_selector_pos = 0
            f2_selector_pos = 0
    
    # plays game intro and load assets
    else:
        screen.fill(BLACK)
        fade_surface.fill(GREY)
        pygame.draw.rect(fade_surface, NAVY, (0, SCREEN_HEIGHT // 2 - 80, SCREEN_WIDTH, 150))
        fade_surface.blit(intro_logo, (logo_x_pos, logo_y_pos))
        screen.blit(fade_surface, (0, 0))
        if logo_x_pos > 500 or logo_y_pos < 130:
            logo_x_pos -= 25
            logo_y_pos += 10

        if time.time() - program_start_timer > FADE_OUT_TIME:
            if fade_alpha > 0:
                fade_alpha -= fade_speed
                if fade_alpha < 0:
                    fade_alpha = 0
                fade_surface.set_alpha(fade_alpha)
        loading_finished = True

    

    pygame.display.update()

pygame.quit()