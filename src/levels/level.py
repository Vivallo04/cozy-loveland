from src.levels.tile import Tile
from src.util.settings import *
import pygame


class Level:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == 'x':
                    Tile((x, y), [self.visible_sprites])

    def run(self):
        # Update and dra the game
        self.visible_sprites.draw(self.display_surface)
