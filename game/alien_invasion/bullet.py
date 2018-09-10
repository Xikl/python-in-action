# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

__author__ = '朱文赵'


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        """在飞船所属的位置创建一个子弹"""
        # super(Bullet, self).__init__()
        # 和上面一样的语法
        super().__init__()

        self.screen = screen

        #  在 (0,0) 处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 设置子弹的位置 用小数表示
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 减小子弹的y值
        self.y -= self.speed_factor
        # 赋值为 self的rect属性
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制字段"""
        pygame.draw.rect(self.screen, self.color, self.rect)
