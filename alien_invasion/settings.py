# -*- coding:utf-8 -*-
class Settings():
    """存储<外星人>的所有设置的类"""
    
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        #飞船的设置
        self.ship_speed_factor = 1.5
        
