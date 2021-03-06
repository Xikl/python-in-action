# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Group

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

    #  创建一个用于存储子弹的编组
    bullets = Group()

    # 开始新的循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
