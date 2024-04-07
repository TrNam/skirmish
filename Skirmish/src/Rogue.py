from Fighter import *

ATTACK_CD = 1200

class Rogue(Fighter):
    def __init__(self, f2, data, sprite_sheet, actions):
        super().__init__(f2, data, sprite_sheet, actions)
        self.defense = 1/6
        self.keys_pressed = [False, False, False, False]

    def update_attack(self, surface, target, k1, k2, k3, k4):
        # check if key is pressed, and go to else
        if self.attacking == False:
            if k1:
                self.attack_start(7, 0)
            if k2:
                self.attack_start(7, 1)
            if k3:
                self.attack_start(7, 2)
            if k4:
                self.attack_start(7, 3)
                
        else: # when attack is starting, handle logic of the frames
            if self.action != 4 and self.action != 5 and self.action != 6 and self.action != 7:
                self.action = self.keys_pressed.index(True) + 4
            
            # first attack 
            if self.action == 4:
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        if self.chain_attack(7, 1):
                            print('we got here')
                        if self.k2 == True and self.chain_attack(7, 1) and self.k1_released == True:
                            self.action == 5
                        elif self.k3 == True and self.chain_attack(7, 2) and self.k1_released == True:
                            self.action == 6
                        elif self.k4 == True and self.chain_attack(7, 3) and self.k1_released == True:
                            self.action == 7
                        else:
                            self.action = 0
                            self.attacking = False
                            self.attack_type = 0
                            self.attack_anim_finished = False
                            self.keys_pressed[0] = False
                            self.k1 = False
                            self.k2 = False
                            self.k3 = False
                            self.k4 = False
                            self.k1_released = False
                            self.k2_released = False
                            self.k3_released = False
                            self.k4_released = False
                    if k1 == False:
                        self.k1_released = True
                if self.frame_index == 1:
                    if k1 == False:
                        self.k1_released = True
                if self.frame_index == 2:
                    self.attack(surface, target)
                    if k1 == False:
                        self.k1_released = True
                    if k2 == True:
                        self.k2 == True
                    elif k3 == True:
                        self.k3 == True
                    elif k4 == True:
                        self.k4 == True
                if self.frame_index == 3:
                    self.attack_anim_finished = True
                    if k2 == True:
                        self.k2 == True
                    elif k3 == True:
                        self.k3 == True
                    elif k4 == True:
                        self.k4 == True

            # second attack 
            if self.action == 5:
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        self.action = 0
                        self.attacking = False
                        self.attack_type = 0
                        self.attack_anim_finished = False
                        self.keys_pressed[1] = False
                if self.frame_index == 2:
                    self.attack(surface, target)
                if self.frame_index == 3:
                    self.attack_anim_finished = True


            # third attack 
            if self.action == 6:
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        self.action = 0
                        self.attacking = False
                        self.attack_type = 0
                        self.attack_anim_finished = False
                        self.keys_pressed[2] = False
                if self.frame_index == 2:
                    self.attack(surface, target)
                if self.frame_index == 3:
                    self.attack_anim_finished = True


            # fourth attack 
            if self.action == 7:
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        self.action = 0
                        self.attacking = False
                        self.attack_type = 0
                        self.attack_anim_finished = False
                        self.keys_pressed[3] = False
                if self.frame_index == 2:
                    self.attack(surface, target)
                if self.frame_index == 3:
                    self.attack_anim_finished = True
                
            if all(self.keys_pressed):
                self.last_attack = pygame.time.get_ticks()
                for i in range(len(self.keys_pressed)):
                    self.keys_pressed[i] = False

    def attack(self, surface, target):
        # only attack if has stamina, reset cd and reduce current stamina
        if self.f2 == False:
            attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        else:
            attacking_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width, self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            if target.health > 0:
                target.health -= 1
        # draw weapon hitbox
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def attack_start(self, amount, key):
    # only attack if not the same attack was done
    # only attack if has stamina, reset cd and reduce current stamina
        if self.stamina >= amount and pygame.time.get_ticks() - self.last_attack > ATTACK_CD:
            self.stamina -= amount
            self.attacking = True
            self.stamina_cd = 70
            self.last_attack = pygame.time.get_ticks()
            self.keys_pressed[key] = True

    def chain_attack(self, amount, key):
    # only attack if not the same attack was done
    # only attack if has stamina
        if self.keys_pressed[key] == False:
            if self.stamina >= amount:
                self.stamina -= amount
                self.attacking = True
                self.stamina_cd = 70
                self.last_attack = pygame.time.get_ticks()
                self.keys_pressed[key] = True
                return True
        return False
    
    def update_hurt(self):
        if self.previous_health != self.health:
            self.previous_health = self.health
            self.hurt_anim_finished = False
            self.hurting = True
        if self.hurt_anim_finished == False:
            # if self.frame_index == 0 and self.hurt_anim_finished == True:
                
            if self.frame_index == 3:
                self.hurt_anim_finished = True
                self.hurting = False
            else:
                self.action = 9
                if self.f2 == False and self.frame_index == 1:
                    self.rect.x -= HURT_MOVE
                elif self.f2 == True and self.frame_index == 1:
                    self.rect.x += HURT_MOVE