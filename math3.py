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
    height_screen=600
    score=0
    color=['#DC143C','#f97101','#4fff4d','#1b981b','#7de8e4',"#6495ED",'#3506e0','#410a5c','#fb6af1','#8A2BE2']
    pygame.init()
    screen = pygame.display.set_mode((width_screen,height_screen))


    #title and icon
    pygame.display.set_caption("phần mềm học toán")
    icon=pygame.image.load('img/calculator.png')
    pygame.display.set_icon(icon)


    #class
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






    class Button_rect:
        def __init__(self,text,width,height,pos,elevation,effect):
            
            gui_font = pygame.font.Font(None,text[1])
            #Core attributes 
            self.pressed = False
            self.elevation = elevation
            self.dynamic_elecation = elevation
            self.original_y_pos = pos[1]

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
            screen.fill(now_color)
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
                        return True
            else:
                self.dynamic_elecation = self.elevation
                self.top_color = '#475F77'



    #board
    board_button_img=pygame.image.load('img/board.png')
    board_button_img = pygame.transform.scale(board_button_img, (300,200))
    board1_buttonX=30
    board1_buttonY=270
    board1_button=Button(board1_buttonX,board1_buttonY,board_button_img)
     
    board2_buttonX=500
    board2_buttonY=270
    board2_button=Button(board2_buttonX,board2_buttonY,board_button_img)

    board3_buttonX=30
    board3_buttonY=420
    board3_button=Button(board3_buttonX,board3_buttonY,board_button_img)

    board4_buttonX=500
    board4_buttonY=420
    board4_button=Button(board4_buttonX,board4_buttonY,board_button_img)


    forward_button_img=pygame.image.load('img/play-again.png')
    forward_buttonX=755
    forward_buttonY=0
    forward_button_img = pygame.transform.scale(forward_button_img, (40,40))
    forward_button=Button(forward_buttonX,forward_buttonY,forward_button_img)

    cat_img=pygame.image.load('img/cat (4).png')
    cat_img = pygame.transform.scale(cat_img, (100,100))

    #game_apple

    game_score=0
    john_X=380
    john_speed=8

    red_apple=pygame.image.load('img_game/john and apple/garden/red-apple.png')
    red_apple=pygame.transform.scale(red_apple,(32,32))
    green_apple=pygame.image.load('img_game/john and apple/garden/green-apple.png')
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
    heart_bar_img=pygame.transform.scale(heart_bar_img,(63,63))
    heart_bar_x=0
    heart_bar_y=-3

    john_right=pygame.image.load("img_game/john and apple/john/R/john_run_right-png/john_run_right (4).png").convert_alpha()
    john_right=pygame.transform.scale(john_right,(150,150))
    john_left=pygame.image.load("img_game/john and apple/john/L/john_run_left-png/john_run_left (4).png")
    john_left=pygame.transform.scale(john_left,(150,150))
    john_center=pygame.image.load("img_game/john and apple/john/john_center.png").convert_alpha()
    john_costume=1
    wait_walk=0
    time_walk=5
    set=0
    



    #start
    sec=5
    a=0
    b=0
    real=[]
    start_button_img=pygame.image.load('img/start-button (4).png')
    start_buttonX=350
    start_buttonY=400
    # start_button=Button(start_buttonX,start_buttonY,start_button_img)
    start_button=Button_rect(('Start',35),100,100,(start_buttonX,start_buttonY),8,50)




    #game_loop
    hide=0
    score=0
    highscore=score
    running=True
    now_color='#3d8f58'
    screen.fill(now_color)
    board_index=0
    clock=pygame.time.Clock()
    while running:
        clock.tick(60)
        #loop
        if(hide==0):
            if start_button.draw():
                hide=1
                ti.sleep(0.25)

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
            screen.fill(now_color)
            pygame.draw.rect(screen,"white",(0,0,len_timebar,5))
            ti.sleep(0.1)
        elif sec<=0:
            hide=1



        if hide==2:
            #font
            font = pygame.font.SysFont('consolas', 70)
            textSurface = font.render(str(a)+"+"+str(b)+"=",True,"white")
            screen.blit(textSurface, (300, 100))
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
                screen.blit(textSurface1, (150, 345))
            


            #button2
            if board2_button.draw():
                hide=3
                board_index=2
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[1]),True,"black")
                screen.blit(textSurface1, (620, 345))
            


            #button3
            if board3_button.draw():
                hide=3
                board_index=3
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[2]),True,"black")
                screen.blit(textSurface1, (150, 495))
            


            #button4
            if board4_button.draw():
                hide=3
                board_index=4
            else:
                # font1 = pygame.font.SysFont('consolas', 60)
                textSurface1 = font1.render(str(real[3]),True,"black")
                screen.blit(textSurface1, (620, 495))

        
        
        elif (hide==3):
            if(real[board_index-1]==answer):
                score+=1
                hide=1
            elif(score<10):
                game_score=0
                hide=1
            else:
                game_score=0
                hide=4
        
        elif hide==4:
            screen.fill("white")
            #character
            screen.blit(bg_back,(0,0))
            screen.blit(bg_center,(5,0))

            if(heart_point>=1):
                screen.blit(heart_bar_img,(0,0))
            if(heart_point>=2):
                screen.blit(heart_bar_img,(20,0))
            if(heart_point==3):
                screen.blit(heart_bar_img,(40,0))


            font1 = pygame.font.SysFont('consolas', 30)
            textSurface1 = font1.render(str(game_score),True,"black")
            screen.blit(textSurface1, (3,15))

            if(highscore<score):
                        highscore=score
            if forward_button.draw():
                    score=0
                    hide=1

            else:
                if(john_costume==4):
                        john_costume=1
                else:
                    wait_walk+=1
                    if wait_walk>time_walk:
                        john_costume+=1
                        wait_walk=0
                if event.type==pygame.KEYDOWN:
                    if(event.key==pygame.K_RIGHT):
                        john_right=pygame.image.load("img_game/john and apple/john/R/john_run_right-png/john_run_right ("+str(john_costume)+").png").convert_alpha()
                        john_right=pygame.transform.scale(john_right,(150,150))
                        john_X+=john_speed
                        screen.blit(john_right,(john_X,335))
                        set=1
                    if(event.key==pygame.K_LEFT):
                        john_left=pygame.image.load("img_game/john and apple/john/L/john_run_left-png/john_run_left ("+str(john_costume)+").png").convert_alpha()
                        john_left=pygame.transform.scale(john_left,(150,150))
                        john_X-=john_speed
                        screen.blit(john_left,(john_X,335))
                        set=2
                    else:
                        set=0
                else:
                    if(set==1):
                        john_right=pygame.image.load("img_game/john and apple/john/R/john_run_right-png/john_run_right (2).png").convert_alpha()
                        john_right=pygame.transform.scale(john_right,(150,150))
                        screen.blit(john_right,(john_X,335))
                    elif(set==2):
                        john_left=pygame.image.load("img_game/john and apple/john/L/john_run_left-png/john_run_left (2).png").convert_alpha()
                        john_left=pygame.transform.scale(john_left,(150,150))
                        screen.blit(john_left,(john_X,335))
                    else:
                        screen.blit(john_center,(john_X,335))
                
                if(red_apple_y<415):
                    if collision(red_apple,(red_apple_x,red_apple_y),john_center,(john_X,335))==False:
                        red_apple_change+=0.125
                        red_apple_y+=red_apple_change
                        pos_apple=Enemy(red_apple,red_apple_x,red_apple_y)
                        pos_apple.draw()
                    else:
                        game_score+=1
                        red_apple_change=0
                        red_apple_y=0
                        red_apple_x=randint(0,760)
                else:
                    if(heart_point<=0):
                        hide=1
                        
                    else:
                        heart_point-=1
                    red_apple_change=0
                    red_apple_y=0
                    red_apple_x=randint(0,760)
                # font1 = pygame.font.SysFont('consolas', 80)
                # textSurface1 = font1.render('score:'+str(score),True,"white")
                # screen.blit(textSurface1, (150, 100))
                # textSurface1 = font1.render('highscore:'+str(highscore),True,"white")
                # screen.blit(textSurface1, (150, 180))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        pygame.display.flip()


run()