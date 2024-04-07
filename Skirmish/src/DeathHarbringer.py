from Fighter import *

class DeathHarbringer(Fighter):
    def __init__(self, f2, data, sprite_sheet, actions):
        super().__init__(f2, data, sprite_sheet, actions)
    
    # have to redefine this method for this class because his sprite is backwards
    def load_images(self, sheet, actions):
        animation_list = []
        for y, step in enumerate(actions):
            temp_img_list = []
            for x in range(step):
                temp_img = sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img = pygame.transform.scale(temp_img, (self.size * self.scale, self.size * self.scale))
                if self.f2 == False:
                    temp_img = pygame.transform.flip(temp_img, True, False)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list