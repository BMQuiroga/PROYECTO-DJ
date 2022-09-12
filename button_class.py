import pygame

class boton():
    def __init__(self,x,y,img,size):
        
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = pygame.transform.scale(img,(int(self.width * size),int(self.height * size)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.click = False

    def draw(self,screen):
        action = False
        screen.blit(self.img,[self.x,self.y])
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.click:
                self.click = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.click = False
            action = False
        return action
