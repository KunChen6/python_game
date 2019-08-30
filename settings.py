class Settings():
#'''存储《外星人入侵》的所有设置的类'''
    
    def __init__(self):
#'''初始化游戏的设置'''

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        #self.ship_speed_factor = 3.5#等级制度速度可变
        self.ship_limit = 3 

        #子弹的设置
        self.bullet_speed_factor = 5
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 250,60,60
        #这些设置创建宽3像素、高15像素的深灰色子弹。子弹的速度比飞船稍低。
        self.bullets_allowed = 30#这将未消失的子弹数限制为3颗。

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1，表示向右移，-1表示向左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏 
        self.speedup_scale = 1.5

        # 外星人点数的提高速度 
        self.score_scale = 1.5 
        
        self.initialize_dynamic_settings()


#这个方法设置了飞船、子弹和外星人的初始速度。随游戏的进行，
#我们将提高这些速度，而每当玩家开始新游戏时，都将重置这些速度。
#在这个方法中，我们还设置 了fleet_direction ，使得游戏刚开始时，
#外星人总是向右移动。每当玩家提高一个等级时，
#我们都使用increase_speed() 来提高飞船、子弹和外星人的速度： 
    def initialize_dynamic_settings(self):
         #"""初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50


        
#为提高这些游戏元素的速度，我们将每个速度设置都乘以speedup_scale 的值。 
    def increase_speed(self):
        #"""提高速度设置"""
        #self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # 外星人点数的提高速度 
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)#现在每当提高一个等级时，你都会在终端窗口看到新的点数值。





        
