# -*- coding: utf-8 -*-
__author__ = '朱文赵'

class Settings():
    """存储外星人设置"""
    """初始化控制游戏外观和飞船速度的属性"""

    def __init__(self):
        """初始化游戏设置"""
         # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        """每次循环的时候最多移动的距离 1.5像素"""
        self.ship_speed_factor = 1.5

