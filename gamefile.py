from main import *



pg.init

screen = pg.display.set_mode((setting['wid'], setting['hei']))
pg.display.set_caption(setting['title'])
clock = pg.time.Clock()

all_sprite = pg.sprite

run = True
while run:
    clock.tick(setting['fps'])
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    screen.fill('green')
    all.sprite.draw(screen)
    pg.display.flip()

pg.init()