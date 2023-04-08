import os
import pygame as pg

setting = {'wid': 950,
           'hei': 950,
           'title': 'gami',
           'bg': 'white',
           'fps': 60
           }

gamefile_folder = os.path.dirname(__file__)
mfiles_folder = os.path.join(gamefile_folder, 'medias')

player_img = pg.image.load(os.path.join(mfiles_folder, 'Player.png' ))



