from main import *

class PLayer(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speedx = None
        self.image = playr_img
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]
            self.speedx = -0
        if keystate[pg.K_RIGHT]
            self.speedx = 8
        self.rect.x += self.speedx