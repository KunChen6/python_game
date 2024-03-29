

class GameStats():
   # """跟踪游戏的统计信息"""
   
    def __init__(self, ai_settings):
        #"""初始化统计信息"""
        self.ai_settings = ai_settings 
        self.reset_stats()
        
        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

        
    def reset_stats(self):
            #"""初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        #为在每次开始游戏时都重置得分，
        #我们在reset_stats() 而不是__init__() 中初始化score 。

        self.level = 1

