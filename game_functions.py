import sys

import pygame

from bullet import Bullet

from alien import Alien

from random import randint

from time import sleep 

def check_keydown_events(event, ai_settings, screen, stats, sb,
                         play_button, ship, aliens, bullets): 
    #响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_p:
        #p键启动游戏
        start_game(ai_settings, screen, stats, sb,
                   play_button, ship, aliens, bullets)
        
         
def check_keyup_events(event,ship):
    #响应松开                 
    if event.key == pygame.K_RIGHT:
         ship.moving_right=False
    elif event.key == pygame.K_LEFT:
         ship.moving_left=False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        
def check_events(ai_settings, screen, stats, sb, play_button,
                 ship, aliens,bullets):
    #'''响应按键和鼠标'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,
                                 play_button, ship, aliens,bullets)
                

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            check_play_button(ai_settings, screen, stats,
                              sb, play_button,ship, aliens, bullets, mouse_x, mouse_y)
        else:
            #print(event.type)
            #显示按不同键得到的信息，其实就是pygame模块对键盘的一些设置
            pass


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):  
    #"""在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 
    if (button_clicked and not stats.game_active): 
        if play_button.rect.collidepoint(mouse_x, mouse_y):  
            start_game(ai_settings, screen, stats, sb, play_button, ship, aliens,bullets)
        

        
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button): 
#'''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    
    #在飞船和外星人后面绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme() #单个外星人时
    aliens.draw(screen)
#对编组调用draw() 时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect 决定。
#在这里，aliens.draw(screen) 在屏幕上绘制编组中的每个外星人。


    # 显示得分
    sb.show_score()
    
     # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #"""更新子弹的位置，并删除已消失的子弹"""

    # 更新子弹的位置
    bullets.update()#子弹Bullet()对象中的update()方法，将为编组bullets 中的每颗子弹调用bullet.update()。

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人,并且射击完左右外星人之后，自动生产一波
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets)
 

##    # 检查是否有子弹击中了外星人
##    # 如果是这样，就删除相应的子弹和外星人
##    # 两个实参True 告诉Pygame删除发生碰撞的子弹和外星人。
##    # 要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，
##    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
##    # 可将第一个布尔实参设置 为False ，并让第二个布尔实参为True 。
##    # 这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。）
##    if len(aliens) == 0:
##        #删除现有的子弹，并生产新的一波外星人
##        bullets.empty()
##        create_fleet(ai_settings,screen,ship,aliens)

    
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets): 
    # """响应子弹和外星人的碰撞"""
     collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
     if collisions:
         for aliens in collisions.values():
             stats.score += ai_settings.alien_points * len(aliens)
             sb.prep_score()
    #check_bullet_alien_collisions() 中，每当有外星人被消灭，都需要在更新得分后调用check_high_score()       
         check_high_score(stats, sb)
   
         
     if len(aliens) == 0:
         # 删除现有的所有子弹，并创建一个新的外星人群
         bullets.empty()
         
         #通过修改速度设置ship_speed_factor 、alien_speed_factor
         #和bullet_speed_factor 的值，足以加快整个游戏的节奏！ 
         ai_settings.increase_speed()

          # 提高等级 
         stats.level += 1 
         sb.prep_level()
         
         create_fleet(ai_settings, screen, ship, aliens)

       
def fire_bullet(ai_settings,screen,ship,bullets):
    #如果还没有到达限制的数量，就发射一颗子弹
    
    #创建一颗子弹，并将其加入编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
     #"""计算屏幕可容纳多少行外星人""" 
    available_space_y = (ai_settings.screen_height-
                         (3 * alien_height) - ship_height)
    #number_rows = int(available_space_y / (2 * alien_height))
    number_rows = randint(1,3) #随机产生
    return number_rows
 #这里使用了int() ，因为我们不想创建 不完整的外星人行



def get_number_aliens_x(ai_settings, alien_width):
    #计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度 
    available_space_x = ai_settings.screen_width - 2 * alien_width
    #number_aliens_x = int(available_space_x / (2 * alien_width))
    #函数int() 将小数部分丢弃，相当于向下圆整
    #（这大有裨益，因为我们宁愿每行都多出一点点空间，也不希望每行的外星人之间过于拥挤）。
    number_aliens_x = randint(1,5) #随机产生
    return number_aliens_x 



def create_alien(ai_settings, screen, aliens, alien_number, row_number): 
    #创建一个外星人群，并放在当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width 
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
    aliens.add(alien)
    
     
def create_fleet(ai_settings, screen, ship, aliens):  
    #创建外星人群
    alien = Alien(ai_settings, screen) 
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width) 
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # 创建外星人群
    for row_number in range(number_rows): 
        for alien_number in range(number_aliens_x):  
             # 每次循环，创建一个外星人并将其加入当前行 
           create_alien(ai_settings, screen, aliens, alien_number, row_number)



def check_fleet_edges(ai_settings,aliens):
    #有外星人到达屏幕边缘时采取相应的措施
    for alien in aliens.sprites():
        if alien.check_edges():#满足切换方向
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    #将整群外星人下移，并改变它们的方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    #"""响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
         
         # 将ships_left减1
        stats.ships_left -= 1

        # 更新剩余飞船的记分牌 
        sb.prep_ships()
         
        # 清空外星人列表和子弹列表 
        aliens.empty()
        bullets.empty()
        
        # 创建一群新的外星人，并将飞船放到屏幕底端中央 
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #暂停一会儿
        sleep(0.5)
         
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)#将重新显示光标




def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    #"""检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites(): 
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break 




def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets): 
    #检查是否有外星人群位于屏幕边缘，并更新所有外星人的位置
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
     # 检测外星人和飞船之间的碰撞
     #方法spritecollideany() 接受两个实参：一个精灵和一个编组
     #它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组。
     #它遍历编组aliens ，并返回它找到的第一个与飞船发生了碰撞的外星人。 
    if pygame.sprite.spritecollideany(ship, aliens): 
        print("Ship hit!!!")
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def  start_game(ai_settings, screen, stats, sb, play_button, ship, aliens,bullets):
    #启动游戏

    # 重置游戏设置
    ai_settings.initialize_dynamic_settings() 

    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息 
    stats.reset_stats()
    stats.game_active = True

     # 重置记分牌图像 
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    #重置剩余飞船图像
    sb.prep_ships()

    # 清空外星人列表和子弹列表 
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并让飞船居中
    ship.center_ship()
    create_fleet(ai_settings, screen, ship, aliens)
        

def check_high_score(stats,sb):
     # """检查是否诞生了新的最高得分""" 
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    
  






    
