##开始开发游戏《外星人入侵
##2019-08-28

#使用Pygame编写的游戏的基本结构如下：

##import sys
##
##import pygame
##
##def run_game():
##    # 初始化游戏并创建一个屏幕对象 
##    pygame.init() 
##    screen = pygame.display.set_mode((1200, 800))#设置屏幕尺寸
##    pygame.display.set_caption("Alien Invasion")
##    
##    # 开始游戏的主循环 
##    while True:
##        
##        # 监视键盘和鼠标事件 
##        for event in pygame.event.get(): 
##            if event.type == pygame.QUIT:
##                sys.exit()
##                
##      # 让最近绘制的屏幕可见 
##        pygame.display.flip()
##
##run_game()


#1.设置背景色
##    #设置背景颜色
##    bg_color=(230,230,230)#RGB 0…255

#2.创建设置类
##下面来编写一个名为settings 的模块，
##其中包含一个名为Settings 的类，
##用于将所有设置存储在一个地方。
##写一个settings.py文件包含这个类。

#3.添加飞船图像
#ship.bmp 位图 放在项目文件夹的一个新建文件夹images下

 #3.1.创建ship类

##选择用于表示飞船的图像后，需要将其显示到屏幕上。
##我们将创建一个名为ship 的模块，其中包含Ship 类，
##它负责管理飞船的大部分行为。

  #3.2.在屏幕上绘制飞船
#    ship=Ship(screen)，

#4. 重构： 模块game_functions
#在大型项目中，经常需要在添加新代码前重构既有代码
#重构旨在简化既有代码的结构，使其更容易扩展。
#我们将创建一个名为game_functions 的新模块
#game_functions 将存储大量让游戏《外星人入侵》运行的函数
#。通过创建模块game_functions ，可避免alien_invasion.py太长，并使其逻辑更容易理解。

  #4.1.建立函数check_events()
#首先把管理事件的代码移到一个名为check_events() 的函数中,以简化run_game() 并隔离事件管理循环。
#通过隔离事件循环，可将事件管理与游戏的其他方面（如:更新屏幕）分离。 

  #4.2. 建立函数update_screen()
#为进一步简化run_game() ，下面将更新屏幕的代码移到一个名为update_screen() 的函数中；
#并将这个函数放在模块game_functions.py 中；。

#5.驾驶飞船

#我们将编写代码，在用户按左或右箭头键时作出响应。
#我们将首先专注于向右移动；
#再使用同样的原理来控制向左移动；

  #5.1.响应按键
#1)每当用户按键时，都将在Pygame中注册一个事件。
#事件都是通过方法pygame.event.get() 获取的，
#，因此在函数check_events() 中，我们需要指定要检查哪些类型的事件。

#2)每次按键都被注册为一个KEYDOWN 事件,
#检测到KEYDOWN 事件时，我们需要检查按下的是否是特定的键。

#3)例如，如果按下的是右箭头键，我们就增大飞船的rect.centerx 值，将飞船向右移动： 

   #5.2 允许不断移动
#1)玩家按住右箭头键不放时，我们希望飞船不断地向右移动,，直到玩家松开为止。
#我们将让游戏检测pygame.KEYUP 事件，以便玩家松开右箭头键时我们能够知道这一点；

#2)结合使用KEYDOWN 和KEYUP 事件，以及一个名为moving_right 的标志来实现持续移动。
#飞船不动时，标志moving_right 将为False
#*玩家按下右箭头键时，我们将这个标志设置为True
#*而玩家松开时，我们将这个标志重新设置为False 。

#3)飞船的属性都由Ship 类控制，
#因此我们将给这个类添加一个名为moving_right 的属性和一个名为update() 的方法。
#方法update() 检查标志moving_right 的状态，
#如果这个标志为True ，就调整飞船的位置。

#4)每当需要调整飞船的位置时，我们都调用这个方法。

   #5.3.左右移动
#1）飞船能够不断地向右移动后，添加向左移动的逻辑很容易。
#。我们将再次修改Ship 类和函数check_events() 。

#2）Ship 类
#在方法__init__() 中，我们添加了标志self.moving_left
#在方法update() 中，我们添加了一个if 代码块而不是elif 代码块，
#这样如果玩家同时按下了左右箭头 键，将先增大飞船的rect.centerx 值，再降低这个值，即飞船的位置保持不变。
#如果使用一个elif 代码块来处理向左移动的情况，右箭头键将始终处于优先地位。
#

#3）我们还需对check_events() 作两方面的调整
#如果因玩家按下K_LEFT 键而触发了KEYDOWN 事件，我们就将moving_left 设置为True；
#如果因玩家松开K_LEFT 而触发了KEYUP 事件，我们就将moving_left 设置 为False；
#。这里之所以可以使用elif 代码块，是因为每个事件都只与一个键相关联
#；如果玩家同时按下了左右箭头键，将检测到两个不同的事件。

   #5.4 调整飞船的速度
#当前，每次移动的速度是给定的像素值，不可调
#
#1）我们可以在Settings 类中添加属性ship_speed_factor
#  self.ship_speed_factor = 1.5
#，用于控制飞船的速度。我们将根据这个属性决定飞船在 每次循环时最多移动多少距离

#2）为了能够在update()中使用飞船速度设置，Ship()类形参列表中添加了ai_settings
# self.ai_settings=ai_settings

#3)鉴于现在调整飞船的位置时，将增加或减去一个单位为像素的小数值，因此需要将位置存储在一个能够存储小数值的变量中
#。可以使用小数来 设置rect 的属性，但rect 将只存储这个值的整数部分
#。为准确地存储飞船的位置，我们在Ship()中定义了一个可存储小数值的新属性self.center
#。我们使用函数float() 将self.rect.centerx 的值转换为小数，并将结果存储到self.center 中。


#4)现在在update() 中调整飞船的位置时，
#将self.center 的值增加或减去ai_settings.ship_speed_factor 的值
#。更新self.center 后，我们再根据它来 更新控制飞船位置的self.rect.centerx 
#。self.rect.centerx 将只存储self.center 的整数部分，但对显示飞船而言，这问题不大

   #5.5.限制飞船的活动范围
#当前，如果玩家按住箭头键的时间足够长，飞船将移到屏幕外面，消失得无影无踪。
#。下面来修复这种问题，让飞船到达屏幕边缘后停止移动

#1）我们将修改Ship 类的方法update() ：
#右边限制，self.rect.right 返回飞船外接矩形的右边缘的 x 坐标

#  if self.moving_right and self.rect.right < self.screen_rect.right:
#       self.center += self.ai_settings.ship_speed_factor


#左边限制，如果rect 的左边缘的 x 坐标大于零，就说明飞船未触及屏幕左边缘
# if self.moving_left and self.rect.left > 0:
#    self.center -= self.ai_settings.ship_speed_factor 

  #5.6重构check_events()函数
#随着游戏开发的进行，函数check_events() 将越来越长，
#，我们将其部分代码放在两个函数中：一个处理KEYDOWN 事件，另一个处理KEYUP 事件：

  #5.7实现上下移动
#在左右移动的基础上添加上下移动很简单，
#self.rect.bottom = self.screen_rect.bottom
#（飞船下边缘的y 坐标）设置为表示屏幕的矩形的属性bottom，这作为移动的界限；


#1）添加标志
#在functions（）中，判断按键事件
#self.moving_down=False
#self.moving_up=False

#2）判断按键（down、up）
#同样的，在 Ship()类的update(self)方法中确定移动的方向和速度
#注意：上边缘时，由于rect获取的是图片的下界限，所以会把图片移出去，
#所以手动把图片的y方向（高度）的像素48（查看图片属性）加进去，当向上移动时，图片上界限刚好接触屏幕上方

#6.射击
#下面来添加射击功能。我们将编写玩家按空格键时发射子弹（小矩形）的代码。
#子弹将在屏幕中向上穿行，抵达屏幕上边缘后消失。

   #6.1.添加子弹设置
#首先，更新settings.py，在其方法__init__() 末尾存储新类Bullet 所需的值： 

   #6.2.创建Bullet类
#下面来创建存储Bullet 类的文件bullet.py
#1）Bullet 类继承了我们从模块pygame.sprite 中导入的Sprite 类。
#通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素

#2）为创建子弹实例，需要 向__init__() 传递ai_settings 、screen 和ship 实例，
#还调用了super() 来继承Sprite 。

  #6.2 将子弹存储到编组中
#定义Bullet 类和必要的设置后，就可以编写代码了，在玩家每次按空格键时都射出一发子弹。

#1）。首先，我们将在alien_invasion.py中创建一个编组（group），
#用于存储所有有效的子弹，以便能够管理发射出去的所有子弹。
#。这个编组将是pygame.sprite.Group 类的一个实例；
#；pygame.sprite.Group 类类似于列表，但提供了有助于开发游戏的额外功能。
#。在主循环中，我们将使用这个编组在屏幕上绘制子弹，以及更新每颗子弹的位置

  #6.3.开火
#1)在game_functions.py中，我们需要修改check_keydown_events()
#，以便在玩家按空格键时发射一颗子弹。
 #编组bulltes 传递给了check_keydown_events()
 #玩家按空格键时，创建一颗新子弹（一个名为new_bullet 的Bullet 实例)
 #并使用方法add() 将其加入 到编组bullets 中
 #代码bullets.add(new_bullet) 将新子弹存储到编组bullets 中。

 #在check_events() 的定义中，我们需要添加形参bullets
 #调用check_keydown_events() 时，我们也需要将bullets 作为实参传递给它

#2)我们无需修改check_keyup_events()
#因为玩家松开空格键 时什么都不会发生

#3)我们还需修改update_screen() ，确保在调用flip() 前在屏幕上重绘每颗子弹。
  #我们给在屏幕上绘制子弹的update_screen() 添加了形参bullets
  #方法bullets.sprites() 返回一个列表，其中包含编组bullets 中的所有精灵
  #。为在屏幕上绘制发射的所有子弹，我们遍历编组bullets 中的精灵，
  #并对每个精灵都调用draw_bullet()

#4)。可在settings.py中修改子弹的尺寸、 颜色和速度。

   #6.4.删除已消失的子弹
#当前，子弹抵达屏幕顶端后消失，这仅仅是因为Pygame无法在屏幕外面绘制它们;
#。这些子弹实际上依然存在，它们的 y 坐标为负数，且越来越小;
#。这是个问题，因为它们将继续 消耗内存和处理能力。
 #我们需要将这些已消失的子弹删除，否则游戏所做的无谓工作将越来越多，进而变得越来越慢

#1)我们需要检测这样的条件，即表示子弹的rect 的bottom 属性为零
#它表明子弹已穿过屏幕顶端。
#使用for循环，将bullets中的满足bottom 属性为零这个条件的子弹remove()掉即可

   #6.5. 限制子弹数量
#很多射击游戏都对可同时出现在屏幕上的子弹数量进行限制，以鼓励玩家有目标地射击。

#1）首先，在settings.py中存储所允许的最大子弹数：

#2）在game_functions.py的check_keydown_events() 中，
#，我们在创建新子弹前检查未消失的子弹数是否小于该设置：

   #6.6.创建update_bullets()函数
#编写并检查子弹管理代码后，可将其移到模块game_functions 中，
#，以让主程序文件alien_invasion.py尽可能简单。
#我们创建一个名为update_bullets() 的新函数，并将其添 加到game_functions.py的末尾：

   #6.7 创建函数fire_bullet()
#下面将发射子弹的代码移到一个独立的函数中；
#这样，在check_keydown_events() 中只需使用一行代码来发射子弹，
#让elif 代码块变得非常简单：
#函数fire_bullet() 只包含玩家按空格键时用于发射子弹的代码；
#在check_keydown_events() 中，我们在玩家按空格键时调用fire_bullet() 

########### 小 结 ####################

#1）运行alien_invasion.py，确认上下、左右移动以及发射子弹时依然没有错误。
#2）再次回顾每个模块和函数，以及每个强大的类。


#7.外星人
#  在本章中，我们将在游戏《外星人入侵》中添加外星人；
#  首先，我们在屏幕上边缘附近添加一个外星人，然后生成一群外星人；
#  我们让这群外星人向两边和下面移动，并删除被子弹击中的外星人；
#  最后，我们将显示玩家拥有的飞船数量，并在玩家的飞船用完后结束游戏
#，你将更深入地了解Pygame和大型项目的管理。你还将学习如何检测游戏对象之间的碰撞，，如子弹和外星人之间的碰撞。
# 。检测碰撞有助于你定义游戏元素之间的交互：
#：可以将角色限定在迷宫墙壁之内或在两个角色之间传球。
#我们将时不时地查看游戏开发计划，以确保编程工作不偏离轨道。

  #7.1.　回顾项目
#1)研究既有代码，确定实现新功能前是否要进行重构。

#2)在屏幕左上角添加一个外星人，并指定合适的边距。

#3）根据第一个外星人的边距和屏幕尺寸计算屏幕上可容纳多少个外星人。
#我们将编写一个循环来创建一系列外星人，这些外星人填满了屏幕的上半部分。

#4）让外星人群向两边和下方移动，直到外星人被全部击落，有外星人撞到飞船，或有外星人抵达屏幕底端。
#如果整群外星人都被击落，我们将再创建一群外星人。如果有外星 人撞到了飞船或抵达屏幕底端，我们将销毁飞船并再创建一群外星人。

#5）限制玩家可用的飞船数量，配给的飞船用完后，游戏结束。

#6）在给项目添加新功能前，还应审核既有代码。每进入一个新阶段，通常项目都会更复杂，因此最好对混乱或低效的代码进行清理。

#7）因此当前需要做的清理工作不多，但每次为测试新功能而运行这个游戏时，都必须使用鼠标来关闭它，这太讨厌了。
#下面来添加一个结束游 戏的快捷键Q：

   #7.2 创建Alien类
#1）除位置不同外，这个类的大部分代码都与Ship 类相似。每个外星人最初都位于屏幕左上角附近，
#我们将每个外星人的左边距都设置为外星人的宽度，并将上边距设置为外星人的高度。 

#2）下面在alien_invasion.py中创建一个Alien 实例,
#在进入主while 循环前创建了一个Alien 实例 alien = Alien(ai_settings,screen)

#3) 让外星人出现在屏幕上
#为让外星人出现在屏幕上，我们在update_screen() 中调用其方法blitme() ：
#gf.update_screen(ai_settings, screen, ship, alien, bullets)
# alien.blitme()

   #7.3 创建一群外星人
#要绘制一群外星人，需要确定一行能容纳多少个外星人以及要绘制多少行外星人。
#我们将首先计算外星人之间的水平间距，并创建一行外星人，再确定可用的垂直空间，
#并创建 整群外星人。

    #7.3.1 确定一行可容纳多少个外星人 
#1）屏幕宽度存储在ai_settings.screen_width 中，但需要在屏幕两边都留下一定的边距
#，把它设置为 外星人的宽度。由于有两个边距，因此可用于放置外星人的水平空间为屏幕宽度减去外星人宽度的两倍：
#     available_space_x = ai_settings.screen_width – (2 * alien_width)

#2）我们还需要在外星人之间留出一定的空间，即外星人宽度。
#因此，显示一个外星人所需的水平空间为外星人宽度的两倍：：一个宽度用于放置外星人，另一个宽度为外星人右边的 空白区域
#为确定一行可容纳多少个外星人，我们将可用空间除以外星人宽度的两倍：
#     number_aliens_x = available_space_x / (2 * alien_width)

#我们将在创建外星人群时使用这些公式。

    #7.3.2 创建多行外星人
#1）为创建一行外星人，首先在alien_invasion.py中创建一个名为aliens 的空编组，
#用于存储全部外星人，再调用game_functions.py中创建外星人群的函数：

#2）接下来，调用稍后将编写的函数create_fleet() ，并将ai_settings 、对象screen 和空编组aliens传递给它
#。然后，修改对update_screen() 的调用，让它能够访问外星人编组
#我们还需要修改update_screen() ：
#def update_screen(ai_settings,screen,ship,aliens,bullets):
#aliens.draw(screen)
#对编组调用draw() 时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect 决定。
#在这里，aliens.draw(screen) 在屏幕上绘制编组中的每个外星人。 

    #7.3.3 创建外星人群
#1）是新函数create_fleet() ，我们将它放在game_functions.py的末尾。
#我们还需要导入Alien 类，因此务必在文件game_functions.py开头添加相应 的import 语句。

#2）函数create_fleet()中主要负责产生外星人，然后不断的加入在aliens组中，
#并且满足屏幕的尺寸，间隔适当（一个外星人间隔）

#注：这行外星人在屏幕上稍微偏向了左边，这实际上是有好处的，
#因为我们将让外星人群往右移，触及屏幕边缘后稍微往下移，然后往左移，以此类推。
#就像经典游戏《太空入侵者》，相比于只往下移，这种移动方式更有趣。
#我们将让外形人群不断这样移动，直到所有外星人都被击落或有外星人撞上飞船或抵达屏幕底端。

   #7.3.4 重构 create_fleet()
#倘若我们创建了外星人群，也许应该让create_fleet() 保持原样，
#但鉴于创建外星人的工作还未完成，我们稍微清理一下这个函数。

#1）函数get_number_aliens_x() 负责计算适合屏幕的外星人的数量。

#2）函数create_alien() 只是使用刚创建的外星人来获取外星人宽度。

#3）函数create_fleet(),我们将计算可用水平空间的代码替换为对get_number_aliens_x() 的调用，
#使用一个 for 循环创建外星人群，而每个外星人则是在create_alien() 中处理创建的。

#3）通过这样的重构，添加新行进而创建整群外星人将更容易。


   #7.3.5 添加行
#要创建外星人群，需要计算屏幕可容纳多少行，并对创建一行外星人的循环重复相应的次数。

#1）为计算可容纳的行数，我们这样计算可用垂直空间：
 #将屏幕高度减去第一行外星人 的上边距（外星人高度）、
 #   飞船的高度以及最初外星人群与飞船的距离（外星人高度的两倍）：
 #         available_space_y = ai_settings.screen_height – 3 * alien_height – ship_height
 #这将在飞船上方留出一定的空白区域，给玩家留出射杀外星人的时间。

#2）每行下方都要留出一定的空白区域，并将其设置为外星人的高度。
 #为计算可容纳的行数，我们将可用垂直空间除以外星人高度的两倍：
 #number_rows = available_height_y / (2 * alien_height)
 #（同样，如果这样的计算不对，我们马上就 能发现，继而将间距调整为合理的值）。

 #知道可容纳多少行后，便可重复执行创建一行外星人的代码

#3)基于以上分析，创建函数get_number_rows()计算屏幕可容纳多少行外星人
 #可以用随机函数：
 #from random import randint
 #random_number = randint(-10,10)
 #   在随机位置产生外星人
 

  #7.4 让外星人群移动
#下面来让外星人群在屏幕上向右移动，撞到屏幕边缘后下移一定的距离，再沿相反的方向移动。
#我们将不断地移动所有的外星人，直到所有外星人都被消灭，有外星人撞上飞 船，
#或有外星人抵达屏幕底端。下面先来让外星人向右移动

  #7.4.1　向右移动外星人
#为移动外星人，我们将使用alien.py中的方法update() ，
#且对外星人群中的每个外星人都调用它。
 #1)首先，Settings()类中添加一个控制外星人速度的设置，self.alien_speed_factor = 1


 #2)然后，使用这个设置来实现update() ,alien.py中， def update(self)，向右移动外星
  # self.x += self.ai_settings.alien_speed_factor
  # self.rect.x = self.x

 #3）在主while 循环中已调用了更新飞船和子弹的方法，但现在还需更新每个外星人的位置：
   #    gf.update_aliens(aliens)
   #我们在更新子弹后再更新外星人的位置，因为稍后要检查是否有子弹撞到了外星人。 

  #7.4.2 创建表示外星人移动方向的设置
#1）下面来创建让外星人撞到屏幕右边缘后向下移动、再向左移动的设置
   #在Settings()中，外星人设置除继续添加如下代码：
##self.fleet_drop_speed = 10
###fleet_direction为1，表示向右移，-1表示向左移
##self.fleet_direction = 1

   #7.4.3 检查外星人是否撞到了屏幕边缘
#现在需要编写一个方法来检查是否有外星人撞到了屏幕边缘，
#还需修改update() ，以让每个外星人都沿正确的方向移动。
   #1）我们可对任何外星人调用新方法check_edges() ，看看它是否位于屏幕左边缘或右边缘。
#如果外星人的rect 的right 属性大于或等于屏幕的rect 的right 属性，
#就说明外 星人位于屏幕右边缘，左边同理。

   #2）我们修改了方法update() ，将移动量设置为外星人速度和fleet_direction 的乘积，
#让外星人向左或向右移。如果fleet_direction 为1，就将外星人当前的 x 坐标增 大alien_speed_factor 。
#反之亦然

   

   #7.4.4 向下移动外星人群并改变移动方向
#有外星人到达屏幕边缘时，需要将整群外星人下移，并改变它们的移动方向。
#我们需要对game_functions.py做重大修改，
#，因为我们要在这里检查是否有外星人到达了左边缘或右边缘
#为此，我们编写函数check_fleet_edges() 和change_fleet_direction() ，并对update_aliens() 进行修改：

   #1）在check_fleet_edges() 中，我们遍历外星人群，并对其中的每个外星人调用check_edges() 
#如果check_edges() 返回True ，我们就知道相应的外星人位 于屏幕边缘，需要改变外星人群的方向，
   
   #2）因此我们调用change_fleet_direction() 并退出循环。
#在change_fleet_direction() 中，我们遍历所有外星人，将每个外星人下移，下移量为fleet_drop_speed 设置的值   
#然后，将fleet_direction 的值修改为其当前值与-1的乘积。

   #3）我们修改了函数update_aliens() ，在其中通过调用check_fleet_edges() 来确定是否有外星人位于屏幕边缘。
   #  现在，函数update_aliens() 包含形 参ai_settings
   #，因此我们调用它时（主函数循环中调用）指定了与ai_settings 对应的实参。 
#至此，运行程序，可以看到外星人按照我们的设计移动了，遇到边缘就改变方向并向下移动。

#7.5 射杀外星人
#我们创建了飞船和外星人群，但子弹击中外星人时，将穿过外星人，因为我们还没有检查碰撞。
#在游戏编程中，碰撞指的是游戏元素重叠在一起。
#要让子弹能够击落外星人，我们将使用sprite.groupcollide() 检测两个编组的成员之间的碰撞。

  #7.5.1 检测子弹与外星人的碰撞 
#子弹击中外星人时，我们要马上知道，以便碰撞发生后让外星人立即消失。
   #为此，我们将在更新子弹的位置后立即检测碰撞。 

   #1）方法sprite.groupcollide() 将每颗子弹的rect 同每个外星人的rect 进行比较，并返回一个字典，
   #其中包含发生了碰撞的子弹和外星人。
   #在这个字典中，每个键都是一 颗子弹，而相应的值都是被击中的外星人
   #（后面章节实现记分系统时，也会用到这个字典）。

  #2）在函数update_bullets() 中，使用下面的代码来检查碰撞
##     def update_bullets(aliens, bullets):
##       """更新子弹的位置，并删除已消失的子弹"""
##       --snip-
##       # 检查是否有子弹击中了外星人
##       # 如果是这样，就删除相应的子弹和外星人
##         collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
  #新增的这行代码遍历编组bullets 中的每颗子弹，再遍历编组aliens 中的每个外星人。
  #每当有子弹和外星人的rect 重叠时，groupcollide() 就在它返回的字典中添加1个键-值对。
  #两个实参True 告诉Pygame删除发生碰撞的子弹和外星人。

   #3）我们调用update_bullets() 时，传递了实参aliens

  #7.5.2 为测试程序，创建大子弹
#1）只需通过运行这个游戏就可以测试其很多功能，但有些功能在正常情况下测试起来比较烦琐。
   #例如，要测试代码能否正确地处理外星人编组为空的情形，需要花很长时间将屏幕 上的外星人都击落。

#2）测试有些功能时，可以修改游戏的某些设置，以便专注于游戏的特定方面。
   #例如，可以缩小屏幕以减少需要击落的外星人数量，也可以提高子弹的速度，以便能够在单位时间内 发射大量子弹。

#3）测试这个游戏时，我喜欢做的一项修改是超级-大子弹，使其在击中外星人后依然有效，
    #请尝试将bullet_width 设置为300，这行程序collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    #看看将所有外星人都射杀有多快！
#类似这样的修改可提高测试效率，还可能激发出如何赋予玩家更大威力的思想火花。
   #（完成测试后，别忘了将设置恢复正常。）

   #7.5.3 生成新的外星人群 　
#这个游戏的一个重要特点是外星人无穷无尽，一个外星人群被消灭后，又会出现一群外星人。
#要在外星人群被消灭后又显示一群外星人，首先需要检查编组aliens 是否为空。
#如果为空，就调用create_fleet() 。我们将在update_bullets() 中执行这种检查，因为外星人都是在这里被消灭的。

  #7.5.4 重构update_bullets()
#下面来重构update_bullets
#使其不再完成那么多任务。我们将把处理子弹和外星人碰撞的代码移到一个独立的函数中： 

  #7.6 结束游戏
#如果玩家根本不会输，游戏还有什么趣味和挑战性可言？
   #如果玩家没能在足够短的时间内将整群外星人都消灭干净，且
   #有外星人撞到了飞船，飞船将被摧毁。
   #与此同时，我们还 限制了可供玩家使用的飞船数，而有外星人抵达屏幕底端时，飞船也将被摧毁。
   #玩家用光了飞船后，游戏便结束。

    #7.6.1　检测外星人和飞船碰撞
#我们首先检查外星人和飞船之间的碰撞，以便外星人撞上飞船时我们能够作出合适的响应。
#我们在更新每个外星人的位置后立即检测外星人和飞船之间的碰撞。

#1）# 检测外星人和飞船之间的碰撞
     #方法spritecollideany() 接受两个实参：一个精灵和一个编组
     #它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组。
     #它遍历编组aliens ，并返回它找到的第一个与飞船发生了碰撞的外星人。
     #如果没有发生碰撞，spritecollideany() 将返回None
   
#2）有外星人撞到飞船时，需要执行的任务很多：需要删除余下的所有外星人和子弹，让飞船重新居中，以及创建一群新的外星人。
   #编写完成这些任 务的代码前，需要确定检测外星人和飞船碰撞的方法是否可行。
   #而为确定这一点，最简单的方式是编写一条print 语句。） 

#3）现在，我们需要将ship 传递给update_aliens() ：
   #现在如果你运行这个游戏，则每当有外星人撞到飞船时，终端窗口都将显示“Ship hit!!!”。

   #7.6.2 响应外星人和飞船碰撞  
#现在需要确定外星人与飞船发生碰撞时,
#我们不销毁ship 实例并创建一个新的ship 实例，
#而是通过跟踪游戏的统计信息来记录飞船被撞了多少次（跟踪统计信息 还有助于记分）。

#1)下面来编写一个用于跟踪游戏统计信息的新类——GameStats ，并将其保存为文件game_stats.py.
 #在这个游戏运行期间，我们只创建一个GameStats 实例，但每当玩家开始新游戏时，需要重置一些统计信息。
 #同时在玩家开始新游戏 时也能调用reset_stats() 。
 # 当前只有一项统计信息——ships_left ，其值在游戏运行期间将不断变化。
 #一开始玩家拥有的飞船数存储在settings.py的ship_limit 中： 
#2) 飞船的设置
    #self.ship_speed_factor = 3.5
    #self.ship_limit = 3
#3)我们还需对alien_invasion.py做些修改，以创建一个GameStats 实例：  from settings import Settings
  #  stats = GameStats(ai_settings) 




#8 计分
#在本章中，我们将结束游戏《外星人入侵》的开发。
#我们将添加一个Play按钮，用于根据需要启动游戏以及在游戏结束后重启游戏。
#我们还将修改这个游戏，使其在玩 家的等级提高时加快节奏，并实现一个记分系统。
#阅读本章后，你将掌握足够多的知识，能够开始编写随玩家等级提高而加大难度以及显示得分的游戏。


   #8.1 添加Play按钮
#在本节中，我们将添加一个Play按钮，它在游戏开始前出现，并在游戏结束后再次出现，让玩家能够开始新游戏。

   #8.1.1 创建Button 类
#由于Pygame没有内置创建按钮的方法，我们创建一个Button 类，用于创建带标签的实心矩形。
#你可以在游戏中使用这些代码来创建任何按钮。
#下面是Button 类的第一部分， 请将这个类保存为文件button.py：

   #8.1.2 在屏幕上绘制按
#我们将使用Button 类来创建一个Play按钮。鉴于只需要一个Play按钮，我们直接在alien_invasion.py中创建它

  #8.1.3 开始游戏  
#为在玩家单击Play按钮时开始新游戏，需在game_functions.py中添加代码，以监视与这个按钮相关的鼠标事件 

  #8.1.4 重置游戏
#前面编写的代码只处理了玩家第一次单击Play按钮的情况，而没有处理游戏结束的情况，因为没有重置导致游戏结束的条件。
  
#为在玩家每次单击Play按钮时都重置游戏，需要重置统计信息、删除现有的外星人和子弹、创建一群新的外星人，并让飞船居中

  #8.1.5 将Play按钮切换到非活动状态
  
 #当前，Play按钮存在一个问题，那就是即便Play按钮不可见，玩家单击其原来所在的区域时，游戏依然会作出响应。
 #如果玩家不小心单击了Play按钮原来所处的区 域，游戏将重新开始！
 #为修复这个问题，可让游戏仅在game_active 为False 时才开始：  


  #8.1.6 隐藏光标
#为让玩家能够开始游戏，我们要让光标可见，但游戏开始后，光标只会添乱
#1)为修复这种问题，我们在游戏处于活动状态时让光标不可见：
#2)游戏结束后，我们将重新显示光标，让玩家能够单击Play按钮来开始新游戏

  #8.1.7 添加让玩家在按P时开始游戏的代码
#1)将check_play_button() 的一些代码提取出来，放到一个名为start_game() 的函数中

#2)并在check_play_button() 和check_keydown_events() 中调用这个函数。

#8.2 提高等级 
#当前，将整群外星人都消灭干净后，玩家将提高一个等级，但游戏的难度并没有变。
  
#下面来增加一点趣味性：每当玩家将屏幕上的外星人都消灭干净后，加快游戏的节奏，让游戏玩起来更难。

  #8.2.1　修改速度设置
  #1)我们首先重新组织Settings 类，将游戏设置划分成静态的和动态的两组
  
  #2)对于随着游戏进行而变化的设置，我们还确保它们在开始新游戏时被重置。
  #settings.py的方法__init__()中，速度不在设置在这里

  #3） def initialize_dynamic_settings(self): 
#这个方法设置了飞船、子弹和外星人的初始速度。随游戏的进行，
#我们将提高这些速度，而每当玩家开始新游戏时，都将重置这些速度。
#在这个方法中，我们还设置 了fleet_direction ，使得游戏刚开始时，
#外星人总是向右移动。每当玩家提高一个等级时，
#我们都使用increase_speed() 来提高飞船、子弹和外星人的速度：

  #4）为提高这些游戏元素的速度，我们将每个速度设置都乘以speedup_scale 的值。

  #5）在check_bullet_alien_collisions() 中，
  #我们在整群外星人都被消灭后调用increase_speed() 来加快游戏的节奏，再创建一群新的外星人.

  #8.2.2　重置速度
#每当玩家开始新游戏时，我们都需要将发生了变化的设置重置为初始值，否则新游戏开始时，速度设置将是前一次游戏增加了的值：
#在函数 start_game()中直接加上： ai_settings.initialize_dynamic_settings() 即可，速度恢复原状。

#8.3 计分
#下面来实现一个记分系统，以实时地跟踪玩家的得分，并显示最高得分、当前等级和余下的飞船数。
#得分是游戏的一项统计信息，因此我们在GameStats 中添加一个score 属性：
  ##为在每次开始游戏时都重置得分，self.sorce = 0
  #我们在reset_stats() 而不是__init__() 中初始化score 。

  #8.3.1 显示得分
#为在屏幕上显示得分，我们首先创建一个新类Scoreboard 
#就当前而言，这个类只显示当前得分，但后面我们也将使用它来显示最高得分、等级和余下的飞船数。
#它被保存为文件scoreboard.py.

  #8.3.2 创建记分牌
#为显示得分，我们在alien_invasion.py中创建一个Scoreboard 实例

  #8.3.3 在外星人被消灭时更新得分
#为在屏幕上实时地显示得分，每当有外星人被击中时，我们都更新stats.score 的值，再调用prep_score() 更新得分图像。
  #但在此之前，我们需要指定玩家每击落一个外星人都将得到多少个点：settings.py中 def initialize_dynamic_settings(self):
   # 记分        self.alien_points = 50

 #8.3.4 将消灭的每个外星人的点数都计入得分
#当前，我们的代码可能遗漏了一些被消灭的外星人。
#例如，如果在一次循环中有两颗子弹射中了外星人，或者因子弹更宽而同时击中了多个外星人，
#玩家将只能得到一个被消灭 的外星人的点数。
   
#为修复这种问题，我们来调整检测子弹和外星人碰撞的方式。
   #在game_functions.py下的def check_bullet_alien_collisions(ai_settings, screen,
   # stats, sb, ship,aliens, bullets): 中
##if collisions:
##    for aliens in collisions.values():
##                 stats.score += ai_settings.alien_points * len(aliens)
##                 sb.prep_score()
## 
#如果字典collisions 存在，我们就遍历其中的所有值。别忘了，每个值都是一个列表，包含被同一颗子弹击中的所有外星人。
#对于每个列表，都将一个外星人的点数乘以其中 包含的外星人数量，并将结果加入到当前得分中。
   #为测试这一点，请将子弹宽度改为300像素，并核实你得到了更宽的子弹击中的每个外星人的点数，再将子弹宽度恢复到正常值。

  #8.3.5 提高点数
#玩家每提高一个等级，游戏都变得更难，因此处于较高的等级时，外星人的点数应更高。
   #为实现这种功能，我们添加一些代码，以在游戏节奏加快时提高点数：
## 外星人点数的提高速度
##   class Settings():中的
##       def __init__(self):定义属性：
##           # 外星人点数的提高速度
##           self.score_scale = 1.5
##    在 def initialize_dynamic_settings(self):
##        #和改变速度一样，每次提高速度，得分就会增加
##        self.alien_points = int(self.alien_points * self.score_scale)
##        print(self.alien_points)#现在每当提高一个等级时，你都会在终端窗口看到新的点数值。

  #8.3.6 将得分圆整
#大多数街机风格的射击游戏都将得分显示为10的整数倍，下面让我们的记分系统遵循这个原则。
#我们还将设置得分的格式，在大数字中添加用逗号表示的千位分隔符。我们 在Scoreboard 中执行这种修改； 
        #rounded_score = int(round(self.stats.score, -1))
   
        #round() 将圆整到最近的10、100、1000等整数倍
        #在Python 2.7中，round() 总是返回一个小数值，我们要使用int() 来确保报告的得分为整数。
        #如果使用的是Python 3，可省略对int() 的调用
   
        #score_str = "{:,}".format(rounded_score)
        #使用了一个字符串格式设置指令，它让Python将数值转换为字符串时在其中插入逗号，
        #例如，输出1,000,000 而不是1000000

   #8.3.7　最高得分
#每个玩家都想超过游戏的最高得分记录。
#下面来跟踪并显示最高得分，给玩家提供要超越的目标。我们将最高得分存储在GameStats 中。

   #8.3.8 显示等级
#为在游戏中显示玩家的等级，首先需要在GameStats 中添加一个表示当前等级的属性。
#1)为确保每次开始新游戏时都重置等级，在reset_stats() 中初始化它：

#2)为让Scoreboard 能够在当前得分下方显示当前等级，我们在__init__() 中调用了一个新方法prep_level() ： 
#在 def show_score(self):这个方法中，添加了一行在屏幕上显示等级图像的代码
   
#3)我们在check_bullet_alien_collisions() 中提高等级，并更新等级图像： 

#4)为确保开始新游戏时,更新记分、等级图像，在按钮Play被单击时触发重置

#5)在check_events() 中，现在需要向check_play_button()传递sb ，让它能够访问记分牌对象：
#最后，更新alien_invasion.py中调用check_events() 的代码，也向它传递sb ：

#注意 注意 注意：在一些经典游戏中，得分带标签，如Score、High Score和Level。
   #我们没有显示这些标签，因为开始玩这款游戏后，每个数字的含义将一目了然。
   #要包含这些标签，只需在Scoreboard 中调用font.render() 前，将它们添加到得分字符串中即可。 

 #8.3.9 显示余下的飞船
#最后，我们来显示玩家还有多少艘飞船，但使用图形而不是数字；
#为此，我们在屏幕左上角绘制飞船图像来指出还余下多少艘飞船，就像众多经典的街机游戏那样。
#1）首先，需要让Ship 继承Sprite ，以便能够创建飞船编组： 
   #在这里，我们导入了Sprite ，让Ship 继承Sprite
   #并在__init__() 的开头就调用了super()
   
#2)接下来，需要修改Scoreboard ，在其中创建一个可供显示的飞船编组。
   #下面是其中的import 语句和方法__init__():
   #self.prep_ships()

   #鉴于要创建一个飞船编组，我们导入Group 和Ship 类。
   #调用prep_level() 后，我们调用了prep_ships()，新建的方法 。
## def prep_ships(self):
##        # """显示还余下多少艘飞船""" 
##        self.ships = Group() 
##        for ship_number in range(self.stats.ships_left):
##            ship = Ship(self.ai_settings, self.screen) 
##            ship.rect.x = 10 + ship_number * ship.rect.width 
##            ship.rect.y = 10 
##            self.ships.add(ship)
   #方法prep_ships() 创建一个空编组self.ships ，用于存储飞船实例。
   #为填充这个编组，根据玩家还有多少艘飞船，运行一个循环相应的次数
   #我们创建一艘新飞船，并设置其x 坐标，让整个飞船编组都位于屏幕左边，且每艘飞船的左边距都为10像素
   #我们还将y 坐标设置为离屏幕上边缘10像素，让所有飞船都与得分图像对齐。
   #。最后，我们将每艘新飞船都添加到编组ships 中

#3）为在屏幕上显示飞船，我们对编组调用了draw() 。Pygame将绘制每艘飞船。

#4）为在游戏开始时让玩家知道他有多少艘飞船，我们在开始新游戏时调用prep_ships() 
  #这是在game_functions.py的check_play_button() 中调用的start_game()函数中进行的：
   #接着重置计分图像，重置剩余飞船图像

#5）我们还在飞船被外星人撞到时调用prep_ships() ，从而在玩家损失一艘飞船时更新飞船图像：
   #首先，我们在update_aliens() 的定义中添加了形参sb
   #然后，我们向ship_hit()和check_aliens_bottom()都传递了sb ，让它们都能够访问记分牌对象。
   #接下来，我们更新了ship_hit() 的定义，使其包含形参sb
   #我们在将ships_left 的值减1后调用了prep_ships()
   #这样每次损失了飞船时，显示的 飞船数都是正确的

#6）在check_aliens_bottom() 中需要调用ship_hit() ，因此对这个函数进行更新，

############游戏名： 去 你 的 烦 恼 ################
   
import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

#from alien import Alien #由于我们不再在alien_invasion.py中直接创建外星人，因此无需在这个文件中导入Alien 类。

from settings import Settings

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
    #初始化游戏屏幕并创建一个屏幕对象


    pygame.init()

    
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(
        "Alien_Invasion")

    # 创建Play按钮 
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例 
    stats = GameStats(ai_settings)
    

    #设置背景颜色
    bg_color=(230,230,230)#RGB 0…255

     # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings) 
    sb = Scoreboard(ai_settings, screen, stats) 
    

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    
    #创建一个用于存储子弹的编组
    bullets = Group()#创建了一个Group 实例，并将其命名为bullets
    #while 循环外面创建的，这样就无需每次运行该循环时都创建一个新的子弹编组。  

    #c创建一个外星人编组 
    aliens = Group()     
##     #创建一个外星人 #from alien import Alien 
##    alien = Alien(ai_settings,screen)

     # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

  
  
    
    #开始游戏主循环
    while True:

##        #监视键盘和鼠标事件
##        for event in pygame.event.get():
##            if event.type==pygame.QUIT:
        
##                sys.exit()
##
##        #让最近绘制的屏幕可见
##        pygame.display.flip()
##
##        # 每次循环时都重绘屏幕
        
##        screen.fill(ai_settings.bg_color) 
##        ship.blitme()

##
##        # 让最近绘制的屏幕可见
        
##        pygame.display.flip()
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets) 
    
        if stats.game_active:
            ship.update()   #飞船Ship()对象中的update()方法
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets) 
            #print(len(bullets))#测试子弹是否删除
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button) 


run_game()






















