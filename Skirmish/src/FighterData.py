IMAGE_SIZE = 768

# Define char values
# Add them to the final dictionary

# KING
KING_SIZE = 160
KING_SCALE = 6
KING_OFFSET_1 = [75, 60]
KING_OFFSET_2 = [68, 60]
KING_DATA = [KING_SIZE, KING_SCALE, KING_OFFSET_1, KING_OFFSET_2]
KING_ANIMATION_ACTIONS = [8, 8, 2, 2, 4, 4, 4, 4, 4, 6]

# KNIGHT
KNIGHT_SIZE = 180
KNIGHT_SCALE = 6
KNIGHT_OFFSET_1 = [80, 97]
KNIGHT_OFFSET_2 = [80, 97]
KNIGHT_DATA = [KNIGHT_SIZE, KNIGHT_SCALE, KNIGHT_OFFSET_1, KNIGHT_OFFSET_2]
KNIGHT_ANIMATION_ACTIONS = [11, 8, 3, 3, 7, 7, 4, 11]

# HUNTRESS
HUNTRESS_SIZE = 150
HUNTRESS_SCALE = 7
HUNTRESS_OFFSET_1 = [72, 83]
HUNTRESS_OFFSET_2 = [72, 83]
HUNTRESS_DATA = [HUNTRESS_SIZE, HUNTRESS_SCALE, HUNTRESS_OFFSET_1, HUNTRESS_OFFSET_2]
HUNTRESS_ANIMATION_ACTIONS = [8, 8, 2, 2, 5, 5, 7, 3, 8]

# SAGE
SAGE_SIZE = 231
SAGE_SCALE = 3.5
SAGE_OFFSET_1 = [115, 113]
SAGE_OFFSET_2 = [115, 113]
SAGE_DATA = [SAGE_SIZE, SAGE_SCALE, SAGE_OFFSET_1, SAGE_OFFSET_2]
SAGE_ANIMATION_ACTIONS = [6, 8, 2, 2, 8, 8, 4, 7]

# DARK_WIZARD
DARK_WIZARD_SIZE = 250
DARK_WIZARD_SCALE = 6
DARK_WIZARD_OFFSET_1 = [120, 150]
DARK_WIZARD_OFFSET_2 = [120, 150]
DARK_WIZARD_DATA = [DARK_WIZARD_SIZE, DARK_WIZARD_SCALE, DARK_WIZARD_OFFSET_1, DARK_WIZARD_OFFSET_2]
DARK_WIZARD_ANIMATION_ACTIONS = [8, 8, 2, 2, 8, 8, 3, 7]

# DEATH_HARBRINGER
DEATH_HARBRINGER_SIZE = 140
DEATH_HARBRINGER_SCALE = 6.5
DEATH_HARBRINGER_OFFSET_1 = [100, 76]
DEATH_HARBRINGER_OFFSET_2 = [100, 76]
DEATH_HARBRINGER_DATA = [DEATH_HARBRINGER_SIZE, DEATH_HARBRINGER_SCALE, DEATH_HARBRINGER_OFFSET_1, DEATH_HARBRINGER_OFFSET_2]
DEATH_HARBRINGER_ANIMATION_ACTIONS = [8, 8, 10, 9, 3, 10]

# FIRE_WIZARD
FIRE_WIZARD_SIZE = 150
FIRE_WIZARD_SCALE = 6.5
FIRE_WIZARD_OFFSET_1 = [70, 86]
FIRE_WIZARD_OFFSET_2 = [70, 86]
FIRE_WIZARD_DATA = [FIRE_WIZARD_SIZE, FIRE_WIZARD_SCALE, FIRE_WIZARD_OFFSET_1, FIRE_WIZARD_OFFSET_2]
FIRE_WIZARD_ANIMATION_ACTIONS = [8, 8, 8, 4, 5]

# MONK 
MONK_SIZE = 126
MONK_SCALE = 6
MONK_OFFSET_1 = [50, 66]
MONK_OFFSET_2 = [50, 66]
MONK_DATA = [MONK_SIZE, MONK_SCALE, MONK_OFFSET_1, MONK_OFFSET_2]
MONK_ANIMATION_ACTIONS = [10, 8, 3, 3, 7, 6, 9, 3, 11]

# ONI
ONI_SIZE = 200
ONI_SCALE = 6
ONI_OFFSET_1 = [90, 111]
ONI_OFFSET_2 = [90, 111]
ONI_DATA = [ONI_SIZE, ONI_SCALE, ONI_OFFSET_1, ONI_OFFSET_2]
ONI_ANIMATION_ACTIONS = [4, 8, 2, 2, 4, 4, 3, 7]

# WARRIOR
WARRIOR_SIZE = 162
WARRIOR_SCALE = 7
WARRIOR_OFFSET_1 = [76, 87]
WARRIOR_OFFSET_2 = [76, 87]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET_1, WARRIOR_OFFSET_2]
WARRIOR_ANIMATION_ACTIONS = [10, 8, 3, 3, 7, 7, 8, 3, 7]

# SAMURAI
SAMURAI_SIZE = 200
SAMURAI_SCALE = 6.5
SAMURAI_OFFSET_1 = [90, 107]
SAMURAI_OFFSET_2 = [90, 107]
SAMURAI_DATA = [SAMURAI_SIZE, SAMURAI_SCALE, SAMURAI_OFFSET_1, SAMURAI_OFFSET_2]
SAMURAI_ANIMATION_ACTIONS = [8, 8, 2, 2, 6, 6, 4, 4, 6]

# ROGUE
ROGUE_SIZE = 150
ROGUE_SCALE = 7
ROGUE_OFFSET_1 = [70, 81]
ROGUE_OFFSET_2 = [70, 81]
ROGUE_DATA = [ROGUE_SIZE, ROGUE_SCALE, ROGUE_OFFSET_1, ROGUE_OFFSET_2]
ROGUE_ANIMATION_ACTIONS = [8, 8, 2, 2, 4, 4, 4, 4, 4, 4, 6]

# SOLDIER
SOLDIER_SIZE = 135
SOLDIER_SCALE = 7.5
SOLDIER_OFFSET_1 = [60, 73]
SOLDIER_OFFSET_2 = [60, 73]
SOLDIER_DATA = [SOLDIER_SIZE, SOLDIER_SCALE, SOLDIER_OFFSET_1, SOLDIER_OFFSET_2]
SOLDIER_ANIMATION_ACTIONS = [10, 6, 2, 2, 4, 4, 5, 3, 9]

ALL_FIGHTER_DATA = {
    'King':[KING_DATA, KING_ANIMATION_ACTIONS],
    'Knight':[KNIGHT_DATA, KNIGHT_ANIMATION_ACTIONS],
    'Huntress':[HUNTRESS_DATA, HUNTRESS_ANIMATION_ACTIONS],
    'Monk':[MONK_DATA, MONK_ANIMATION_ACTIONS],
    'Oni':[ONI_DATA, ONI_ANIMATION_ACTIONS],
    'Rogue':[ROGUE_DATA, ROGUE_ANIMATION_ACTIONS],
    'Samurai':[SAMURAI_DATA, SAMURAI_ANIMATION_ACTIONS],
    'Soldier':[SOLDIER_DATA, SOLDIER_ANIMATION_ACTIONS],
    'Warrior':[WARRIOR_DATA, WARRIOR_ANIMATION_ACTIONS],
    'DarkWizard':[DARK_WIZARD_DATA, DARK_WIZARD_ANIMATION_ACTIONS],
    'FireWizard':[FIRE_WIZARD_DATA, FIRE_WIZARD_ANIMATION_ACTIONS],
    'DeathHarbringer':[DEATH_HARBRINGER_DATA, DEATH_HARBRINGER_ANIMATION_ACTIONS],
    'Sage': [SAGE_DATA, SAGE_ANIMATION_ACTIONS]
}