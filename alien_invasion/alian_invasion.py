# -*- coding:utf-8 -*-
#import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():    
    #初始化游戏并创建一个屏幕对象           
    gf.pygame.init()            
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alian_Invasion")
    #创建一艘飞船
    ship = Ship(screen)
    
    
    #开始游戏的主循环
    while True:
            
        #~ #监视键盘和鼠标事件
        #~ for event in pygame.event.get():
            #~ if event.type == pygame.QUIT:
                #~ sys.exit()
        
        gf.check_events()
                
        #~ #每次循环时重绘屏幕
        #~ screen.fill(ai_settings.bg_color)
        #~ ship.blitme()
        #~ #让最近绘制的屏幕可见
        #~ pygame.display.flip()
        
        gf.update_screen(ai_settings, screen, ship)

run_game()
