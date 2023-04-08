import os
import pygame as pg

confing= {
    'w': 600,
     'h': 600,
     'title':'Yurik молодец',
       'bg': " white",
        'fps':60}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder,'media')

player_img = pg.image.load(os.path.join(media_folder,'Player.png'))

object_img=pg.image.load(os.path.join(media_folder,'bruh.png'))
