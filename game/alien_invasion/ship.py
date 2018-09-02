# -*- coding: utf-8 -*-
import pygame

__author__ = '朱文赵'


class Ship:

    def __init__(self, ai_settings, screen):
        """加载飞船 并且设置他的初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        """加载飞船图像，并且获得其外接矩形"""
        self.image = pygame.image.load_basic("images/ship.bmp")
        self.rect = self.image.get_rect()
        # 屏幕的属性 整个屏幕在 坐标轴的第四象限 初始化飞船在 右下方的位置
        self.screen_rect = screen.get_rect()

        """ 将每艘新飞船放在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 居中显示
        # self.rect.center = self.screen_rect.center

        # 飞船自己的center属性中 存储一个小数值
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 增加一个标志位
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """ 通过一个标志位来决定是否进行移动"""
        """右移"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        """左移"""
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        """上移 初始为 五百多"""
        if self.move_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor

        """下移 初始为最大高度"""
        if self.move_down and self.rect.bottom < self.screen_rect.height:
            self.bottom += self.ai_settings.ship_speed_factor

        # 根据自己的center中的属性更新rect对象
        #  self.rect.centerx 将只存储 self.center 的整数部分，但对显示飞船而言，这问题不大
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def bit_me(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
