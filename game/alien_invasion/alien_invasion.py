# -*- coding: utf-8 -*-
import pygame

import game.alien_invasion.game_functions as gf
from game.alien_invasion.settings import Settings
from game.alien_invasion.ship import Ship

__author__ = '朱文赵'


def run_game():
    # 初始化游戏并创建一个屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    # 开始新的循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
