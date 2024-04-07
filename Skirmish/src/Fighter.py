import pygame

SPEED = 10
GRAVITY = 1
GROUND_OFFSET = 20
JUMP = 20
ATTACK_CD = 2000
HURT_MOVE = 5

class Fighter():
    def __init__(self, f2, data, sprite_sheet, actions):
        self.f2 = f2
        self.size = data[0]
        self.scale = data[1]
        if self.f2 == False:
            self.offset = data[2]
        else:
            self.offset = data[3]
        self.rect = pygame.Rect((0, 0, 1, 1))
        self.vel_y = 0
        self.jumping = False
        self.last_attack = 0
        self.attack_type = 0
        self.attacking = False
        self.running = False
        self.last_action = 0
        self.health = 100
        self.stamina = 100
        self.action = 0 # 0:idle, 1:move/run, 2:jump, 3:fall, 4/5/6:attack, 6/7/8:take hits, 7/8:death
        self.frame_index = 0 # current frame OF current self.action
        self.stamina_cd = 70
        self.animation_list = self.load_images(sprite_sheet, actions) # contains ALL animation actions
        self.image = self.animation_list[self.action][self.frame_index] # the image being displayed for animation
        self.update_time = pygame.time.get_ticks()
        self.k1_released = False
        self.k2_released = False
        self.k3_released = False
        self.k4_released = False
        self.k1 = False
        self.k2 = False
        self.k3 = False
        self.k4 = False
        self.attack_anim_finished = False
        self.hurt_anim_finished = True
        self.is_holding = True
        self.defense = 1/4
        self.previous_health = 100
        self.hurting = False
    
    # set position of fighter when loaded in game
    def set_rect(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 100))

    # handle animation update
    def animate(self):
        animation_cd = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cd:
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    # load animations
    def load_images(self, sheet, actions):
        animation_list = []
        for y, step in enumerate(actions):
            temp_img_list = []
            for x in range(step):
                temp_img = sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img = pygame.transform.scale(temp_img, (self.size * self.scale, self.size * self.scale))
                if self.f2 == True:
                    temp_img = pygame.transform.flip(temp_img, True, False)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list
        
    # display fighter onto screen
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        # self.image = pygame.transform.flip(self.image, self.f2, False)
        surface.blit(self.image, (self.rect.x - (self.offset[0] * self.scale), self.rect.y - (self.offset[1] * self.scale)))
    
    # constantly update y position
    def update_y_pos(self, screen_height):
        
        dy = 0

        key = pygame.key.get_pressed()
        if self.attacking == False and self.hurting == False:
            if self.f2 == False: # player 2
                # jump
                if key[pygame.K_w] and self.jumping == False:
                    self.vel_y = -JUMP
                    self.jumping = True
                    self.action = 2
            else:
                if key[pygame.K_UP] and self.jumping == False:
                    self.vel_y = -JUMP
                    self.jumping = True
                    self.action = 2

        # gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.bottom + dy > screen_height - GROUND_OFFSET:
            self.vel_y = 0
            dy = screen_height - self.rect.bottom - GROUND_OFFSET
            self.jumping = False

        if dy < 0:
            self.action = 2
        elif dy > 0:
            self.action = 3

        self.rect.y += dy

    # constantly update x position
    def update_x_pos(self, screen_width, target):           

        dx = 0

        # get key pressed
        key = pygame.key.get_pressed()

        # if not attacking
        if self.attacking == False and self.hurting == False:
            # check which player
            if self.f2 == False: # player 1
                # check which key
                # left right
                if key[pygame.K_a]:
                    dx = -SPEED
                    if self.jumping == False:
                        self.action = 1
                if key[pygame.K_d]:
                    if self.rect.colliderect(target.rect):
                        dx = 0
                    else:
                        dx = SPEED
                    if self.jumping == False:
                        self.action = 1
                    
            else: # player 2
                # check which key
                # left right
                if key[pygame.K_LEFT]:
                    if self.rect.colliderect(target.rect):
                        dx = 0
                    else:
                        dx = -SPEED
                    if self.jumping == False:
                        self.action = 1
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    if self.jumping == False:
                        self.action = 1

        # restrict character from moving off the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
            
        # update fighter position
        self.rect.x += dx
    
    # condition to start attacking
    def attack_start(self, amount):
        # only attack if has stamina, reset cd and reduce current stamina
        if self.stamina >= amount and pygame.time.get_ticks() - self.last_attack > ATTACK_CD:
            self.stamina -= amount
            self.attacking = True
            self.stamina_cd = 70
            self.last_attack = pygame.time.get_ticks()

    # condition to chain attacking
    def chain_attack(self, amount):
        # only attack if has stamina, reset stamina cd and reduce current stamina
        if self.stamina >= amount:
            self.stamina -= amount
            self.attacking = True
            self.stamina_cd = 70
            return True
        return False

    # attack mechanics, change for each individual character
    def update_attack(self):
        pass

    # attack mechanics, change for each individual character
    def attack(self):
        pass

    # getting hurt mechanic
    def update_hurt(self):
        pass

    # main update function to run all functions
    def update(self, screen_width, screen_height, surface, target, k1, k2, k3, k4):

        if self.attacking == False:
            keys = pygame.key.get_pressed()
            if all(not key for key in keys):
                self.action = 0
            if self.f2 == True:
                if not (keys[pygame.K_w] and keys[pygame.K_a] and keys[pygame.K_s] and keys[pygame.K_d]\
                        and keys[pygame.K_r] and keys[pygame.K_t] and keys[pygame.K_f] and keys[pygame.K_g]):
                    self.action = 0
            else:
                if not (keys[pygame.K_UP] and keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]\
                        and keys[pygame.K_QUOTE] and keys[pygame.K_SLASH] and keys[pygame.K_PERIOD] and keys[pygame.K_SEMICOLON]):
                    self.action = 0

            # stamina regen 
            if self.stamina_cd > 0:
                self.stamina_cd -= 1
            else:
                if self.stamina + 1 > 100:
                    self.stamina = self.stamina + (100 - self.stamina)
                elif self.stamina < 100:
                    self.stamina += 2

        self.update_y_pos(screen_height)
        self.update_x_pos(screen_width, target)
        self.update_attack(surface, target, k1, k2, k3, k4)
        self.update_hurt()

        # reset to first frame every time action is changed
        if self.last_action != self.action:
            self.frame_index = 0
            self.last_action = self.action
        
        self.animate()
        self.draw(surface)