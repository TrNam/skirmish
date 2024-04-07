from Fighter import *

ATTACK_CD = 2000

class King(Fighter):
    def __init__(self, f2, data, sprite_sheet, actions):
        super().__init__(f2, data, sprite_sheet, actions)
        self.bonus_damage = 0
    
    # attack logic
    def update_attack(self, surface, target, k1, k2, k3, k4):
        # check if key is pressed, and go to else
        if self.attacking == False and self.hurting == False:
            if k1:
                self.attack_start(10)
                self.attack_type = 1
            if k2:
                self.attack_start(10)
                self.is_holding = True
                self.attack_type = 2
        else: # when attack is starting, handle logic of the frames

            # if not attacking, start first attack
            if self.action != 4 and self.action != 5 and self.action != 6:
                if self.attack_type == 1:
                    self.action = 4
                elif self.attack_type == 2:
                    self.action = 5

            # first attack
            if self.action == 4:

                # frame 1
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        if (self.k1_released == True and k1) or self.k1 == True:
                            if self.chain_attack(10):
                                self.action = 6
                            else:
                                self.action = 0
                                self.attacking = False
                                self.attack_type = 0
                        else:
                            self.attacking = False
                            self.action = 0
                            self.attack_type = 0
                        self.k1_released = False
                        self.attack_anim_finished = False

                    if k1 == False:
                        self.k1_released = True

                # frame 2
                elif self.frame_index == 1:
                    if k1 == False:
                        self.k1_released = True

                # frame 3
                elif self.frame_index == 2:
                    self.attack1(surface, target) # this hits for 6 frames so it would actually be target.health - 1 six times
                    if k1 == False:
                        self.k1_released = True
                    if k1 == True and self.k1_released == True:
                        self.k1 = True

                # frame 4
                elif self.frame_index == 3: 
                    self.attack_anim_finished = True
                    if k1 == True and self.k1_released == True:
                        self.k1 = True

            # chain attack
            elif self.action == 6:
                # frame 1
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        self.attacking = False
                        self.action = 0
                        self.k1_released = False
                        self.attack_anim_finished = False
                        self.k1 = False
                        self.attack_type = 0
                
                # frame 2 -> do nothing

                # frame 3
                elif self.frame_index == 2:
                    self.attack2(surface, target) # this hits for 6 frames so it would actually be target.health - 1 six times

                # frame 4
                elif self.frame_index == 3: 
                    self.attack_anim_finished = True
            
            # hold attack
            elif self.action == 5:
                if self.frame_index == 0:
                    if self.attack_anim_finished == True:
                        self.attacking = False
                        self.action = 0
                        self.k1_released = False
                        self.attack_anim_finished = False
                        self.k1 = False
                        self.attack_type = 0
                        self.bonus_damage = 0
                        self.is_holding = True

                if k2 == False:
                    self.is_holding = False
                    
                if k2 == True and self.stamina >= 0 and self.is_holding == True:
                    self.frame_index = 0
                    if self.stamina >= 0:
                        self.stamina -= 1
                    self.bonus_damage += 0.05

                if self.frame_index == 2:
                    self.attack3(surface, target)
                if self.frame_index == 3:
                    self.attack_anim_finished = True

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
                self.action = 8
                if self.f2 == False and self.frame_index == 1:
                    self.rect.x -= HURT_MOVE
                elif self.f2 == True and self.frame_index == 1:
                    self.rect.x += HURT_MOVE

    # attack action (do damage)
    def attack1(self, surface, target):
        if self.f2 == False:
            attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y + 50, 4 * self.rect.width, self.rect.height / 2)
        else:
            attacking_rect = pygame.Rect(self.rect.centerx - 4 * self.rect.width, self.rect.y + 50, 4 * self.rect.width, self.rect.height / 2)
        if attacking_rect.colliderect(target.rect):
            if target.health > 0:
                target.health -= 1 + self.bonus_damage 
        # draw weapon hitbox
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

     # attack action (do damage)
    def attack2(self, surface, target):
        if self.f2 == False:
            attacking_rect = pygame.Rect(self.rect.centerx + 220, self.rect.y - 120, 2 * self.rect.width, self.rect.height - 50)
        else:
            attacking_rect = pygame.Rect((self.rect.centerx - 2 * self.rect.width) - 220, self.rect.y - 120, 2 * self.rect.width, self.rect.height - 50)
        if attacking_rect.colliderect(target.rect):
            if target.health > 0:
                target.health -= 1 + self.bonus_damage 
        # draw weapon hitbox
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

     # attack action (do damage)
    def attack3(self, surface, target):
        if self.f2 == False:
            attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 4.5 * self.rect.width, self.rect.height)
        else:
            attacking_rect = pygame.Rect(self.rect.centerx - 4.5 * self.rect.width, self.rect.y, 4.5 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            if target.health > 0:
                target.health -= 1 + self.bonus_damage 
        # draw weapon hitbox
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def set_rect(self, x, y):
        self.rect = pygame.Rect((x, y, 100, 270))

