import pygame

from pygame.sprite import Sprite

#1）Bullet 类继承了我们从模块pygame.sprite 中导入的Sprite 类。
#通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素

#2）为创建子弹实例，需要 向__init__() 传递ai_settings 、screen 和ship 实例，
#还调用了super() 来继承Sprite 。


class Bullet(Sprite):
    #一个对飞船发射的子弹进行管理的类

    def __init__(self,ai_settings,screen,ship):

        #在飞船所属的位置创建一个子弹对象
        super(Bullet,self).__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                 ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx 
        self.rect.top = ship.rect.top 

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

       
        
        

    def update(self):
        #"向上移动子弹
        #更新表示子弹位置的小数值 
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置 
        self.rect.y = self.y
        
    def draw_bullet(self):
        #在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)



        
