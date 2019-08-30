
import pygame

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        # """初始化飞船，并设置其起始位置""" 

        super(Ship, self).__init__()

        self.screen=screen
        self.ai_settings=ai_settings#为了能够在update()中使用飞船速度设置，形参列表中添加了ai_settings 

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') #这个函数返回一个表示飞船的surface
        self.rect = self.image.get_rect() #get_rect() 获取相应surface的属性rect 
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央 
        self.rect.centerx = self.screen_rect.centerx#（飞船中心的x 坐标）设置为表示屏幕的矩形的属性centerx 
        self.rect.bottom = self.screen_rect.bottom #（飞船下边缘的y 坐标）设置为表示屏幕的矩形的属性bottom 
         #Pygame将使用这些rect 属性来放置飞船图像， 使其与屏幕下边缘对齐并水平居中。 

        # 在飞船的属性center中存储小数值 
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        
        #移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False

        

    def update(self):
        #根据移动标志调整飞船位置

        # 更新飞船的center值，而不是rect；
        #使用 if 并列，其实是为了公平的检测按键，同时按下作用相反的键，则飞船不动；
        #上下左右移动时，注意，屏幕的左上角是原点；
        
        #左右移动
        #self.rect.right 返回飞船外接矩形的右边缘的 x 坐标
        #如果rect 的左边缘的 x 坐标大于零，就说明飞船未触及屏幕左边缘
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            #self.rect.centerx += 10
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= self.ai_settings.ship_speed_factor
            self.center -= self.ai_settings.ship_speed_factor
            
        #上下移动
        #self.rect.bottom 返回飞船外接矩形的下边缘的 y 坐标
        #如果rect 的上边缘的 y 坐标大于零，就说明飞船未触及屏幕上边缘   
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            #self.rect.bottom += 10
            self.bottom += self.ai_settings.ship_speed_factor
        #上边缘时，由于rect获取的是图片的下界限，所以会把图片移出去，所以手动把图片的y方向的像素280加进去，而不是0.
        if self.moving_up and self.rect.bottom > 580: 
            #self.rect.bottom -= 10
            self.bottom -= self.ai_settings.ship_speed_factor
            
         # 根据self.center更新rect对象 
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom 

            
    #定义了方法blitme() ，它根据self.rect 指定的位置将图像绘制到屏幕上。
    def blitme(self):  

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
         # """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx+30
       # self.center = self.screen_rect.bottom






          
 
