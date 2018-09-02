# -*- coding: utf-8 -*-
__author__ = '朱文赵'

import sys
import pygame


def check_events(ship):
    # 监听鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 按下按键
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        # 放开按键
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 设置为false 键盘弹起 停止移动
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True



def check_keyup_events(event, ship):
    # 判断是不是右键
    if event.key == pygame.K_RIGHT:
        # 设置为true 进行移动
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False



def update_screen(ai_settings, screen, ship):
    """ 每次更新屏幕上的对象，并且切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.bit_me()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
