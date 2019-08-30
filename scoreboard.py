import pygame.font
#由于Scoreboard 在屏幕上显示文本，因此我们首先导入模块pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard():
      #"""显示得分信息的类"""
    
    def __init__(self, ai_settings, screen, stats):
     # """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置 
        self.text_color = (30, 30, 30) 
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像 
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

        #准备剩下的飞船图像
        self.prep_ships()


    def prep_score(self):
        #"""将得分转换为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        #round() 将圆整到最近的10、100、1000等整数倍
        #在Python 2.7中，round() 总是返回一个小数值，我们要使用int() 来确保报告的得分为整数。
        #如果使用的是Python 3，可省略对int() 的调用
        score_str = 'Score:'+"{:,}".format(rounded_score)
        #此处使用了一个字符串格式设置指令，它让Python将数值转换为字符串时在其中插入逗号，
        #例如，输出1,000,000 而不是1000000
        
        #score_str = str(self.stats.score) #不需要圆整时的表示
        
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # 将得分放在屏幕右上角 
        self.score_rect = self.score_image.get_rect() 
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20


    def prep_high_score(self):        
        #"""将最高得分转换为渲染的图像"""          
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = 'High Score:'+"{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)         

        #将最高得分放在屏幕顶部中央          
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        #"""在屏幕上显示得分、最高分、等级"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)


    def prep_level(self):
          #"""将等级转换为渲染的图像""" 
        self.level_image = self.font.render('Level:'+str(self.stats.level),
                                            True,self.text_color, self.ai_settings.bg_color)
          # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect() 
        self.level_rect.right = self.score_rect.right 
        self.level_rect.top = self.score_rect.bottom + 10




    def prep_ships(self):
        # """显示还余下多少艘飞船""" 
        self.ships = Group() 
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen) 
            ship.rect.x = 10 + ship_number * ship.rect.width 
            ship.rect.y = 10 
            self.ships.add(ship)




















