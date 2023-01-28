# phần mềm tính nhẩm nhanh trong python #
# pygame có luồng
from threading import Thread
import pygame
import time as ti
from random import *

def run():

    #create screen, images and variable
    #
    #create screen
    width_screen=800
    height_screen=800
    score=0
    color=['#DC143C','#f97101','#4fff4d','#1b981b','#7de8e4',"#6495ED",'#3506e0','#410a5c','#fb6af1','#8A2BE2']
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width_screen,height_screen))

    #title and icon
    pygame.display.set_caption("phần mềm học toán")
    icon=pygame.image.load('img/calculator.png')
    pygame.display.set_icon(icon)


    #class

    class Background():
        def __init__(self):
            self.x = 0
            self.y = height_screen-600
            self.speed = 5
            self.img = bg_center
            self.width = self.img.get_width()
            self.height = self.img.get_height()
        def draw(self):
            screen.blit(self.img, (int(self.x), int(self.y)))
            screen.blit(self.img, (int(self.x + self.width), int(self.y)))
            screen.blit(self.img, (int(self.x - self.width), int(self.y)))
            
        def update(self):
            if event.type==pygame.KEYDOWN:
                if(event.key==pygame.K_RIGHT):
                    self.x -= self.speed
                elif(event.key==pygame.K_LEFT):
                    self.x += self.speed
            
            if self.x < -self.width:
                self.x = -self.width
            if self.x > self.width:
                self.x = self.width

        def answer(self):
            return self.x
    
    
    class Apple_trees():
        def __init__(self,amount,img_appletrees,img_trees,pos):
            self.amount_apple=amount
            self.img_appletrees=img_appletrees
            self.img_trees=img_trees
            self.rect=self.img_appletrees.get_rect()
            self.clicked=False
            self.pos=pos
            self.x=pos[0]
            self.y=pos[1]
            self.speed=5
        def update(self,amount):
            self.amount_apple=amount
        def draw(self):
            action=False
            pos=pygame.mouse.get_pos()
            #check mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked==False and self.amount_apple!=0:
                    self.clicked=True
                    action=True
                    self.amount_apple-=1

            if pygame.mouse.get_pressed()[0]==0 :
                self.clicked=False
            
            if event.type==pygame.KEYDOWN:
                if(event.key==pygame.K_RIGHT):
                    if self.x>-800+self.pos[0]:
                        self.x -= self.speed
                elif(event.key==pygame.K_LEFT):
                    if self.x<800+self.pos[0] :
                        self.x += self.speed
            
            
            if self.amount_apple>0:
                screen.blit(self.img_appletrees,(self.x,self.y))
            else:
                screen.blit(self.img_trees,(self.x,self.y))
              
            return self.amount_apple 
                        
                
    class Player():
        def __init__(self,x,speed):
            self.x=x
            self.speed=speed
            self.x_change=self.speed
            self.john_costume=1
            self.wait_walk=0
            self.time_walk=4
            self.set=2
        def update(self):
            if(self.john_costume==4):
                self.john_costume=1
            else:
                self.wait_walk+=1
                if self.wait_walk>self.time_walk:
                    self.john_costume+=1
                    self.wait_walk=0
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT):
                self.x_change=self.speed
                if(event.key==pygame.K_RIGHT):
                    self.set=1
                elif(event.key==pygame.K_LEFT):
                    self.set=2
                
                if self.set==1:
                    # self.x+=self.x_change
                    john_right=pygame.image.load("img_game/john and apple/john/R/john_run_right-png/john_run_right ("+str(self.john_costume)+").png").convert_alpha()
                    john_right=pygame.transform.scale(john_right,(150,150))
                    screen.blit(john_right,(self.x,335))
                if self.set==2:
                    # self.x-=self.x_change
                    john_left=pygame.image.load("img_game/john and apple/john/L/john_run_left-png/john_run_left ("+str(self.john_costume)+").png").convert_alpha()
                    john_left=pygame.transform.scale(john_left,(150,150))
                    screen.blit(john_left,(self.x,335))
                
            else:
                if self.set==1:
                    john_right=pygame.image.load("img_game/john and apple/john/R/john_run_right-png/john_run_right (4).png").convert_alpha()
                    john_right=pygame.transform.scale(john_right,(150,150))
                    screen.blit(john_right,(self.x,335))
                elif self.set==2:
                    john_left=pygame.image.load("img_game/john and apple/john/L/john_run_left-png/john_run_left (4).png").convert_alpha()
                    john_left=pygame.transform.scale(john_left,(150,150))
                    screen.blit(john_left,(self.x,335))
        
        def answer(self):
            return (self.x,335)
            
    class Enemy():
        def __init__(self,image,x,y):
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.topleft=(x,y)
        def draw(self):
            #draw apple
            screen.blit(self.image,(self.rect.x,self.rect.y))

    def collision(surface1, pos1, surface2, pos2):
        mask1 = pygame.mask.from_surface(surface1)
        mask2 = pygame.mask.from_surface(surface2)
        x = pos2[0] - pos1[0]
        y = pos2[1] - pos1[1]
        if mask1.overlap(mask2, (x, y)) != None:
            return True
        return False


    class Button():
        def __init__(self,x,y,image):
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.topleft=(x,y)
            self.clicked=False
        def draw(self):
            action=False
            pos=pygame.mouse.get_pos()
            #check mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                    self.clicked=True
                    action=True

            if pygame.mouse.get_pressed()[0]==0 :
                self.clicked=False
            #draw button
            screen.blit(self.image,(self.rect.x,self.rect.y))

            return action



    class Button_pause:
        def __init__(self,width,height,x,y):
            self.pos=[(x,y),(x,y+height),(x+(width-width/8),y+height/2)]
            self.rect=pygame.Rect((x,y),(width,height))
        def draw(self):
            pygame.draw.polygon(screen,(255,255,255),self.pos)
            action=False
            pos=pygame.mouse.get_pos()
            #check mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                    self.clicked=True
                    action=True
                    

            if pygame.mouse.get_pressed()[0]==0 :
                self.clicked=False
            
            return action
    
    
    class Button_set_level:
        def __init__(self,level,width,height,pos,elevation,effect):
            self.text_list=['Easy','Medium','Difficult']
            self.level=level
            #Core attributes 
            self.pressed = False
            self.elevation = elevation
            self.dynamic_elecation = elevation
            self.original_y_pos = pos[1]
            self.pos=pos
            self.width=width
            self.height=height

            # top rectangle 
            self.top_rect = pygame.Rect(pos,(width,height))
            self.top_color = '#bfbfbf'

            # bottom rectangle 
            self.bottom_rect = pygame.Rect(pos,(width,height))
            self.bottom_color = '#b3b3b3'
            #effect
            self.effect=effect
        def draw(self):
            #text
            gui_font = pygame.font.Font(None,20)
            self.text_surf = gui_font.render(self.text_list[self.level],True,'#000000')
            self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
            # elevation logic 
            self.top_rect.y = self.original_y_pos - self.dynamic_elecation
            self.text_rect.center = self.top_rect.center

            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
            self.rect=pygame.Rect((self.pos[0],self.pos[1]-self.dynamic_elecation),(self.width,self.height+self.dynamic_elecation))
            pygame.draw.rect(screen,now_color,self.rect,border_radius = self.effect)
            pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = self.effect)
            pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = self.effect)
            screen.blit(self.text_surf, self.text_rect)

            if self.check_click():
                return True

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.top_rect.collidepoint(mouse_pos):
                self.top_color = '#d9d9d9'
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elecation = 0
                    self.pressed = True
                else:
                    self.dynamic_elecation = self.elevation
                    if self.pressed == True:
                        self.pressed=False
                        if self.level!=len(self.text_list)-1:
                            self.level+=1
                        else:
                            self.level=0
                        return True
            else:
                self.dynamic_elecation = self.elevation
                self.top_color = '#bfbfbf'


    class Button_switch:
        def __init__(self,set_point,pos):
            self.clicked=False
            self.button_rect = pygame.Rect(pos,(80,40))
            self.action=set_point
            self.pos=pos
        def draw(self,suf):
            mouse_pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                    self.clicked=True
                    if self.action:
                        self.action=False
                    else:
                        self.action=True

                elif pygame.mouse.get_pressed()[0]==0 :
                    self.clicked=False
            
            if self.action==True:
                pygame.draw.rect(suf,(0,255,40), self.button_rect ,border_radius = 75)
                pygame.draw.rect(suf,(0,0,0), self.button_rect ,2, border_radius = 75)
                pygame.draw.circle(suf,(255,255,255),(self.pos[0]+20,self.pos[1]+20),15)
                pygame.draw.circle(suf,(0,0,0),(self.pos[0]+20,self.pos[1]+20),16,1)
                
                
            elif self.action==False:
                pygame.draw.rect(suf,(210,210,210), self.button_rect ,border_radius = 75)
                pygame.draw.rect(suf,(0,0,0), self.button_rect ,2, border_radius = 75)
                pygame.draw.circle(suf,(255,255,255),(self.pos[0]+60,self.pos[1]+20),15)
                pygame.draw.circle(suf,(0,0,0),(self.pos[0]+60,self.pos[1]+20),16,1)
        def answer(self):
            return self.action



    class Button_rect:
        def __init__(self,text,width,height,pos,elevation,effect):
            
            gui_font = pygame.font.Font(None,text[1])
            #Core attributes 
            self.pressed = False
            self.elevation = elevation
            self.dynamic_elecation = elevation
            self.original_y_pos = pos[1]
            self.pos=pos
            self.width=width
            self.height=height
            

            # top rectangle 
            self.top_rect = pygame.Rect(pos,(width,height))
            self.top_color = '#475F77'

            # bottom rectangle 
            self.bottom_rect = pygame.Rect(pos,(width,height))
            self.bottom_color = '#354B5E'
            #text
            self.text_surf = gui_font.render(text[0],True,'#FFFFFF')
            self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
            #effect
            self.effect=effect
        def draw(self):
            # elevation logic 
            self.top_rect.y = self.original_y_pos - self.dynamic_elecation
            self.text_rect.center = self.top_rect.center

            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
            # screen.fill(now_color)
            self.rect=pygame.Rect((self.pos[0],self.pos[1]-self.dynamic_elecation),(self.width,self.height+self.dynamic_elecation))
            pygame.draw.rect(screen,now_color,self.rect,border_radius = self.effect)
            pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = self.effect)
            pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = self.effect)
            screen.blit(self.text_surf, self.text_rect)

            if self.check_click():
                return True

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.top_rect.collidepoint(mouse_pos):
                self.top_color = '#60809f'
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elecation = 0
                    self.pressed = True
                else:
                    self.dynamic_elecation = self.elevation
                    if self.pressed == True:
                        self.pressed=False
                        return True
            else:
                self.dynamic_elecation = self.elevation
                self.top_color = '#475F77'

        
            
    


    def draw_menu_setting(surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        screen.fill(now_color)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect(),border_radius=30)
        font1 = pygame.font.SysFont('consolas', 38, bold=True)
        sound_text= font1.render("Sound:",True,(0,255,220))
        level_text= font1.render("Level:",True,(0,255,220))
        shape_surf.blit(sound_text, (width_screen/8-40,height_screen/8-20))
        shape_surf.blit(level_text, (width_screen/8-40,height_screen/8*2-20))
        sound_button.draw(shape_surf)
        level_button.draw()
        shape_surf.set_alpha(180)
        surface.blit(shape_surf, rect)

    #board
    board_button_img=pygame.image.load('img/board.png')
    board_button_img = pygame.transform.scale(board_button_img, (300,200))
    board1_buttonX=(width_screen/4-150)
    board1_buttonY=((height_screen/8)*5-100)
    board1_button=Button(board1_buttonX,board1_buttonY,board_button_img)
     
    board2_buttonX=(width_screen/4*3-150)
    board2_buttonY=((height_screen/8)*5-100)
    board2_button=Button(board2_buttonX,board2_buttonY,board_button_img)

    board3_buttonX=(width_screen/4-150)
    board3_buttonY=((height_screen/8)*7-100)
    board3_button=Button(board3_buttonX,board3_buttonY,board_button_img)

    board4_buttonX=(width_screen/4*3-150)
    board4_buttonY=((height_screen/8)*7-100)
    board4_button=Button(board4_buttonX,board4_buttonY,board_button_img)


    # forward_button_img=pygame.image.load('img/play-again.png')
    # forward_button_img = pygame.transform.scale(forward_button_img, (40,40))
    forward_buttonX=(width_screen/2-80)
    forward_buttonY=(height_screen/8*4.5-50)
    forward_button=Button_rect(('Play again',40),160,100,(forward_buttonX,forward_buttonY),10,25)


    cat_img=pygame.image.load('img/cat (4).png')
    cat_img = pygame.transform.scale(cat_img, (100,100))



    #game_apple

    game_score=0
    john_X=380
    john_speed=10

    apple_trees_img=pygame.image.load('img_game/john and apple/garden/apple-trees.png')
    apple_trees_img=pygame.transform.scale(apple_trees_img,(500,500))
    trees_img=pygame.image.load('img_game/john and apple/garden/trees.png')
    trees_img=pygame.transform.scale(trees_img,(500,500))
    
    apple_trees_list=[Apple_trees(6,apple_trees_img,trees_img,(10,height_screen-560))]
    
    red_apple=pygame.image.load('img_game/john and apple/garden/red-apple.png')
    red_apple=pygame.transform.scale(red_apple,(32,32))
    red_apple_button=Button((width_screen/2-73),(height_screen/4*3-72),pygame.transform.scale(red_apple,(145,145)))
    green_apple=pygame.image.load('img_game/john and apple/garden/green-apple.png')
    red_apple_worm=pygame.image.load('img_game/john and apple/garden/red-apple-worm.png')
    red_apple_y=0
    red_apple_x=randint(0,760)
    red_apple_change=0
    green_apple=pygame.transform.scale(green_apple,(32,32))

    bg_back=pygame.image.load('img_game/john and apple/garden/background_garden_apple_back.png')
    bg_center=pygame.image.load('img_game/john and apple/garden/background_garden_apple_center.png')
    bg_center=pygame.transform.scale(bg_center,(800,600))

    # heart_bar_img=pygame.image.load('img_game/john and apple/garden/heart bar/heart-'+str(heart_point)+".png")
    # heart_bar_img=pygame.transform.scale(heart_bar_img,(163,163))
    heart_bar_img=pygame.image.load('img_game/john and apple/garden/heart bar/heart.png').convert_alpha()
    heart_bar_img=pygame.transform.scale(heart_bar_img,(38,38))

    john_right=pygame.image.load("img_game/john and apple/john/R/john_run_right-png/john_run_right (4).png").convert_alpha()
    john_right=pygame.transform.scale(john_right,(150,150))
    john_left=pygame.image.load("img_game/john and apple/john/L/john_run_left-png/john_run_left (4).png").convert_alpha()
    john_left=pygame.transform.scale(john_left,(150,150))
    john_center=pygame.image.load("img_game/john and apple/john/john_center.png").convert_alpha()
    
    john_player=Player(john_X,john_speed)




    #start
    sec=5
    a=0
    b=0
    real=[]
    set_apple_list=[green_apple,red_apple,red_apple_worm]
    set_apple=choice(set_apple_list)
    start_buttonX=(width_screen/2-50)
    start_buttonY=(height_screen/4*3-50)
    start_button=Button_rect(('Start',35),100,100,(start_buttonX,start_buttonY),10,50)
    #setting
    setting_button_img=pygame.image.load('img/settings.png')
    setting_button_img=pygame.transform.scale(setting_button_img,(100,100))
    setting_buttonX=(width_screen/4*2.75-50)
    setting_buttonY=(height_screen/4*3-50)
    setting_button=Button(setting_buttonX,setting_buttonY,setting_button_img)
    #sound
    tick_sound=pygame.mixer.Sound('sounds/tick.wav')
    soundtrack='sounds/spring.wav'
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.play(-1)
    sound_buttonX=(width_screen/4)
    sound_buttonY=(height_screen/8-20)
    sound_button=Button_switch(True,(sound_buttonX,sound_buttonY))
    
    #level
    level_buttonX=(width_screen/4+15)
    level_buttonY=(height_screen/8*2-10)
    level_button=Button_set_level(0,60,40,(level_buttonX,level_buttonY),6,8)
    
    #exit
    exit_buttonX=(width_screen/8*7-40)
    exit_buttonY=(height_screen/8*7-40)
    exit_button=Button_rect(('Exit',35),80,80,(exit_buttonX,exit_buttonY),8,25)

    #pause
    paused_buttonX=(width_screen/16*15.5-10)
    paused_buttonY=(height_screen/16*0.7-10)
    paused_button=Button_pause(20,20,paused_buttonX,paused_buttonY)
    

    #game_loop
    hide=0
    total_score=0
    score=0
    highscore=score
    running=True
    now_color='#3d8f58'
    screen.fill(now_color)
    board_index=0
    clock=pygame.time.Clock()
    while running:
        # clock.tick(60)
        #loop
        if(hide==0):
            screen.fill(now_color)
            if start_button.draw():
                hide=1
                ti.sleep(0.25)
            if setting_button.draw():
                hide=6
                
                
        elif(hide==1):
            local_sec=5
            sec=local_sec
            heart_point=3
            now_color=color[randint(0,len(color)-1)]
            a=randint(1,5)
            b=randint(1,5)
            real=[a+b,a+b+1,a+b-randint(1,2),a+b+randint(2,3)]
            answer=real[0]
            shuffle(real)
            screen.fill(now_color)
            hide=2


        if sec>0 and hide==2:
            sec-=0.1
            len_timebar=int(width_screen*(sec/local_sec))
            pygame.draw.rect(screen,now_color,(0,0,width_screen,5))
            pygame.draw.rect(screen,"white",(0,0,len_timebar,5))
            ti.sleep(0.1)
        elif sec<=0 and hide==2:
            hide=1

        sound_play=sound_button.answer()
        if sound_play==False:
            pygame.mixer.music.pause()
        elif sound_play and hide!=7:
            pygame.mixer.music.unpause()
            
            

        if hide==2:
            pygame.draw.rect(screen,now_color,(0,5,width_screen,height_screen-5))
            #font
            font = pygame.font.SysFont('consolas', 70)
            textSurface = font.render(str(a)+"+"+str(b)+"=",True,"white")
            screen.blit(textSurface, (width_screen/2-70, height_screen/8))
            font = pygame.font.SysFont('consolas', 25)
            textSurface = font.render(str(score),True,"white")
            screen.blit(textSurface, (5, 10))
            font1 = pygame.font.SysFont('consolas', 60)
            #button1
            if board1_button.draw():
                hide=3
                board_index=1
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[0]),True,"black")
                screen.blit(textSurface1, ((width_screen/4-30), (height_screen/8*5-24)))
            


            #button2
            if board2_button.draw():
                hide=3
                board_index=2
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[1]),True,"black")
                screen.blit(textSurface1, ((width_screen/4*3-30), (height_screen/8*5-24)))



            #button3
            if board3_button.draw():
                hide=3
                board_index=3
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[2]),True,"black")
                screen.blit(textSurface1, ((width_screen/4-30), (height_screen/8*7-24)))


            #button4
            if board4_button.draw():
                hide=3
                board_index=4
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[3]),True,"black")
                screen.blit(textSurface1, ((width_screen/4*3-30), (height_screen/8*7-24)))

            if paused_button.draw():
                hide=7
        
        elif (hide==3):
            if(real[board_index-1]==answer):
                pygame.mixer.music.pause()
                pygame.mixer.Sound.play(tick_sound)
                score+=10
                hide=1
            else:
                
                total_score+=score
                if(highscore<score):
                    highscore=score
                    hide=5
                else:
                    hide=5
        
        
        elif hide==4:
            screen.fill((180, 255, 255))
            #character
            # screen.blit(bg_back,(0,0))
            # screen.blit(bg_center,(0,height_screen-600))

            # if(heart_point>=1):
            #     screen.blit(heart_bar_img,(width_screen-120,0))
            # if(heart_point>=2):
            #     screen.blit(heart_bar_img,(width_screen-80,0))
            # if(heart_point==3):
            #     screen.blit(heart_bar_img,(width_screen-40,0))


            font1 = pygame.font.SysFont('consolas', 30)
            textSurface1 = font1.render(str(game_score),True,"black")
            screen.blit(textSurface1, (5,0))

            bg.draw()
            bg.update()
            john_player.update()
            set_back=0
            for i in apple_trees_list:
                if i.draw()==0:
                    set_back+=1
            

            # if(red_apple_y<415):
            #     if collision(red_apple,(red_apple_x,red_apple_y),john_center,john_player.answer())==False:
            #         red_apple_change+=0.2
            #         red_apple_y+=red_apple_change
            #         pos_apple=Enemy(set_apple,red_apple_x,red_apple_y)
            #         pos_apple.draw()
            #     else:
            #         set_apple_list=[green_apple,red_apple,red_apple_worm]
            #         set_apple=choice(set_apple_list)
            #         game_score+=1
            #         red_apple_change=0
            #         red_apple_y=0
            #         red_apple_x=randint(0,width_screen)
            # else:
            #     if(heart_point<=0):
            #         hide=1
                    
            #     else:
            #         heart_point-=1
            #     red_apple_change=0
            #     red_apple_y=0
            #     red_apple_x=randint(0,width_screen)


        elif hide==5:
            now_color="#225b6c"
            screen.fill(now_color)
            font1 = pygame.font.SysFont('consolas', 20)
            textSurface1 = font1.render(str(total_score),True,"white")
            screen.blit(textSurface1,(0,0))
            font1 = pygame.font.SysFont('consolas', 80)
            textSurface1 = font1.render('score:'+str(score),True,"white")
            screen.blit(textSurface1, (width_screen/4-40, 100))
            textSurface1 = font1.render('highscore:'+str(highscore),True,"white")
            screen.blit(textSurface1, (width_screen/4-40, 180))
            
            if forward_button.draw():
                score=0
                hide=1
            if(score>=10):
                # draw apple button
                if red_apple_button.draw():
                    score=0
                    set=2
                    bg=Background()
                    for i in apple_trees_list:
                        i.update(randint(2,12))
                    hide=4
         
        elif hide==6:
            draw_menu_setting(screen, (190, 190, 190, 120), (10, 10, width_screen-20, height_screen-20))
            if exit_button.draw():
                hide=0
        
        elif hide==7:
            pygame.mixer.music.pause()
            screen.fill(now_color)
            largeText = pygame.font.SysFont("comicsansms",120)
            TextSurf = largeText.render("Pause",True,(0,0,0))
            screen.blit(TextSurf, (width_screen/2-180,height_screen/2-120))
            if paused_button.draw():
                if sound_play:
                    pygame.mixer.music.unpause()
                hide=2

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        pygame.display.flip()

run()
