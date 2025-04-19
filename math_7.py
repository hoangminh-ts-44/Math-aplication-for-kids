# phần mềm tính nhẩm nhanh Thalassa Math trong python #
import pygame,pygame_widgets
from sys import exit
from pygame_widgets.slider import Slider
from colorsys import hsv_to_rgb
from random import randint,shuffle,uniform
from datetime import datetime
from json import dump,load
from math import sin
from variable import *
from data import *
def main():
    #create screen, images and variable
    pygame.init()
    width_screen, height_screen = 1000, 800
    screen = pygame.display.set_mode((width_screen,height_screen),pygame.RESIZABLE)
    icon=pygame.image.load('resources/img/calculator.png').convert_alpha()

    #title and icon
    pygame.display.set_caption('Phần mềm toán học : Thalassa Math')
    pygame.display.set_icon(icon)

    #class
    class Background():
        def __init__(self,img):
            self.x = width_screen/2
            self.y = 0
            self.img = img
            self.width = self.img.get_width()
            self.height = self.img.get_height()

        def draw(self): screen.blit(self.img, (int(self.x), int(self.y)))

        def update(self,player):
            x_camera = player.x - (width_screen/2 - player.width/2)
            if x_camera < 0: x_camera = 0
            if x_camera + width_screen > self.width: x_camera = self.width - width_screen
            self.x = -x_camera

    lock = pygame.image.load('resources/img/lock.png').convert_alpha()
    head_shark = pygame.image.load('resources/img/shark (2).png').convert_alpha()
    class Map:
        def __init__(self,pos,img,bg,character,index):
            self.pos=pos
            self.index=index
            self.img=img
            self.rect=self.img.get_rect()
            self.rect.center=self.pos
            self.clicked=False
            self.food=[]
            self.bg=bg
            self.game_score=0
            self.charater=character
            self.action=False
            self.x_speed=4
            self.x=5

        def restart(self):
            self.action=False
            self.x_speed=4
            self.x=5
        def create(self,food_set):
            self.food.clear()
            self.food_set=food_set
            for i in range(len(self.food_set)):
                if self.food_set[i][0]==0:
                    for _ in range(min(self.food_set[i][2],self.spam)):
                        for _ in range(self.food_set[i][3]):
                            rannum1_y=randint(self.food_set[i][5][0],self.food_set[i][5][1])
                            rannum1_x=randint(self.food_set[i][4][0],self.food_set[i][4][1])
                            self.append(Food(self.food_set[i][1][0],self.food_set[i][1][1],(rannum1_x,rannum1_y),self.food_set[i][6],self.food_set[i][7],self.food_set[i][8]))

        def append(self,insert): self.food.append([insert,True])

        def draw(self,pos,time,food_set,spam):
            self.spam=spam
            self.food_set=food_set
            if self.food_set[len(fish_list)]!=1 and self.index==len(fish_list):
                font1 = pygame.font.SysFont('consolas', 40)
                textSurface1 = font1.render('Welcome to SHARK game',True,WHITE)
                screen.blit(textSurface1, (width_screen/2-textSurface1.get_width()/2,height_screen/8))
                screen.blit(head_shark,(width_screen/4*3.4-40,height_screen/8-30))
                if self.x>width_screen-60: self.x=5
                self.x+=self.x_speed
                for i in range(1,5):screen.blit(shark1_img_title,(self.x,height_screen-(50+i*45)))

            if self.food_set[self.index]!=1:
                self.time=time
                if not self.action:
                    self.rect.center=pos
                    pos=pygame.mouse.get_pos()

                    #check mouse
                    if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0]==1 and not self.clicked:
                            self.clicked=True
                            self.action=True
                            self.create(fish_list)

                    if pygame.mouse.get_pressed()[0]==0 : self.clicked=False

                    #draw button
                    screen.blit(self.img,(self.rect.x,self.rect.y))
                    self.game_score=0
                    return -1

                elif self.action: return self.play()
            else:
                my_surface = pygame.Surface((width_screen, height_screen))
                my_surface = my_surface.convert_alpha()
                my_surface.fill(pygame.Color(0, 100, 255,50))
                screen.blit(self.img,(width_screen/2-self.rect.width/2,height_screen/2-self.rect.height/2))
                pygame.draw.rect(my_surface,BLACK,(0,0,width_screen, height_screen))
                screen.blit(lock,(width_screen/4*3.25-40,height_screen/8+40))
                my_surface.set_alpha(200)
                screen.blit(my_surface,(0,0))
                font1 = pygame.font.SysFont('consolas', 80)
                textSurface1 = font1.render('Lock',True,WHITE)
                screen.blit(textSurface1, (width_screen/2-85,height_screen/2))
                return -1

        def play(self):
            screen.fill((75, 155, 255))
            self.bg.draw()
            self.bg.update(self.charater)
            i=0
            while i<len(self.food):
                if not self.food[i][0].action and self.food[i][1]:self.game_score += self.food[i][0].print_point(); self.food[i][1]=False
                if self.food[i][0].update(self.bg,self.charater)==False:self.food.pop(i)
                i+=1
            self.charater.update(self.bg)

            font1 = pygame.font.SysFont('consolas', 30)
            textSurface1 = font1.render(str(self.game_score),True,BLACK)
            screen.blit(textSurface1, (5,0))
            text= font1.render('Time: '+ str(round(self.time)),True,BLACK)
            screen.blit(text,(5,30))

            return self.game_score

    class Fish:
        def __init__(self,pos,img_right,img_left,speed):
            self.img_right=img_right
            self.img_left=img_left
            self.mouse_fish_pos=(0,0)
            self.rect=self.img_right.get_rect()
            self.width=self.rect[2]
            self.height=self.rect[3]
            self.rect.center=(0,0)
            self.dx,self.dy=(0,0)
            self.x=pos[0]
            self.y=pos[1]
            self.speed=self.local_sp=speed
        def update(self,bg):
            if food1[16]==0:
                if pygame.mouse.get_pressed()[0]==1:self.speed=self.local_sp*2
                else:self.speed=self.local_sp

            mx,my=pygame.mouse.get_pos()
            self.rect.midleft=(self.x,self.y)
            if self.x+bg.x<=mx: self.x+=self.speed
            if self.x+bg.x>=mx: self.x-=self.speed

            if self.x <= 0: self.x = 0

            if self.x + self.width >= bg.width: self.x = bg.width - self.width

            # moving y
            if self.y<my-self.speed: self.y+=self.speed
            elif self.y>my+self.speed: self.y-=self.speed

            self.mouse_fish_pos=(mx,my)
            if self.x+bg.x <= self.mouse_fish_pos[0]:
                screen.blit(self.img_right,(int(self.x+bg.x), int(self.y+bg.y)))
            elif self.x+bg.x >= self.mouse_fish_pos[0]:
                screen.blit(self.img_left,(int(self.x+bg.x), int(self.y+bg.y)))


    class Food:
        def __init__(self,img_right,img_left,pos,speed,point,sound):
            self.img_right=img_right
            self.img_left=img_left
            self.rect=self.img_right.get_rect()
            self.height=self.rect[3]
            self.width=self.rect[2]
            self.x,self.y=pos
            self.y_local=self.y
            self.speedx,self.speedy=speed,speed*1.25
            self.action=True
            self.point=point
            self.sound=sound
            self.text=font3.render(''.join(['+',str(point)]),True,'WHITE')
            self.alpha=255
        def update(self,bg,player):
            if self.action:
                self.x+=self.speedx
                if self.x < 0: self.speedx=-self.speedx
                if self.x + self.width > bg.width: self.speedx=-self.speedx
                if rect_distance((self.x+bg.x,self.y,self.width,self.height),(player.x+bg.x,player.y,player.width,player.height))<=80 and (self.y > 20 and self.y + self.height < bg.height-self.height):
                    if self.y>player.y: self.y+=abs(self.speedy)
                    else: self.y-=abs(self.speedy)
                elif rect_distance((self.x+bg.x,self.y,self.width,self.height),(player.x+bg.x,player.y,player.width,player.height))>=85:
                    if self.y!=self.y_local:
                        if self.y>self.y_local: self.y-=abs(self.speedy)
                        else: self.y+=abs(self.speedy)

                if collision(self.img_right,(self.x+bg.x,self.y),self.point,player.img_right,(int(player.x+bg.x), int(player.y)),max_game_score):
                    self.action=False
                    if sound_effect_play:pygame.mixer.Sound.play(self.sound)

                if self.speedx > 0: screen.blit(self.img_right,(int(self.x+bg.x), int(self.y)))
                elif self.speedx <= 0: screen.blit(self.img_left,(int(self.x+bg.x), int(self.y)))
            else:
                if self.alpha>20:self.text_food(bg.x)
                else:return False

        def text_food(self,x):
            self.alpha -= 10
            self.y -= 2
            self.text.set_alpha(self.alpha)
            screen.blit(self.text, (self.x+x, self.y))
        def print_point(self): return self.point

    def collision(surface1, pos1, score1, surface2, pos2, score2):
        mask1 = pygame.mask.from_surface(surface1)
        mask2 = pygame.mask.from_surface(surface2)
        rect1= surface1.get_rect()
        rect2= surface2.get_rect()
        x = pos2[0] - pos1[0]
        y = pos2[1] - pos1[1]
        if mask1.overlap(mask2, (x, y)) != None and (score1<score2 or rect1<rect2): return True
        return False

    class Button:
        def __init__(self,x,y,image):
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.topleft=(x,y)
            self.clicked=False
        def draw(self,pos):
            self.rect.topleft=pos
            pos=pygame.mouse.get_pos()
            #check mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and not self.clicked:self.clicked=True
                if self.clicked:
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked=False
                        return True
            #draw button
            screen.blit(self.image,(self.rect.x,self.rect.y))

    class Button_pause:
        def __init__(self,width,height,x,y):
            self.x=x
            self.y=y
            self.pos=[(x,y),(x,y+height),(x+(width/8*7),y+height/2)]
            self.rect=pygame.Rect((x,y),(width,height))
            self.clicked = False
            self.action = False
        def load(self,width,height,x,y):
            self.x = x
            self.y = y
            self.pos = [(x, y), (x, y + height), (x + (width / 8 * 7), y + height / 2)]
            self.rect = pygame.Rect((x, y), (width, height))
        def draw(self):
            pygame.draw.polygon(screen, (255, 255, 255), self.pos)
            pos = pygame.mouse.get_pos()
            # check mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.action = True if not self.action else False

                if pygame.mouse.get_pressed()[0] == 0: self.clicked = False

            return self.action



    class Button_img3D:
        def __init__(self,x,y,image):
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.center=(x,y)
            self.effect=5
            self.clicked=False
        def draw(self,pos):
            action=False
            self.rect.center=pos
            pos=pygame.mouse.get_pos()
            # check mouse
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: self.clicked = True
                if self.clicked:
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                        return True

            # draw button
            if not self.clicked:
                screen.blit(self.image,(self.rect.x,self.rect.y))
                screen.blit(self.image,(self.rect.x,self.rect.y-self.effect))
            else: screen.blit(self.image,(self.rect.x,self.rect.y))
            return action


    class Button_switch:
        def __init__(self,set_point,pos):
            self.clicked=False
            self.button_rect= pygame.Rect(pos,(80,40))
            self.action=set_point
            self.pos=pos
        def draw(self,suf,pos):
            self.button_rect.topleft=pos
            self.pos=pos
            mouse_pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]==1 and not self.clicked:
                    self.clicked=True
                    if self.action:self.action=False
                    else:self.action=True

                elif pygame.mouse.get_pressed()[0]==0 :self.clicked=False

            if self.action:
                pygame.draw.rect(suf,GREEN, self.button_rect ,border_radius = 75)
                pygame.draw.rect(suf,BLACK, self.button_rect ,2, border_radius = 75)
                pygame.draw.circle(suf,WHITE,(self.pos[0]+20,self.pos[1]+20),14)
                pygame.draw.circle(suf,BLACK,(self.pos[0]+20,self.pos[1]+20),15,1)

            else:
                pygame.draw.rect(suf,LIGHTGRAY, self.button_rect ,border_radius = 75)
                pygame.draw.rect(suf,BLACK, self.button_rect ,2, border_radius = 75)
                pygame.draw.circle(suf,WHITE,(self.pos[0]+60,self.pos[1]+20),14)
                pygame.draw.circle(suf,BLACK,(self.pos[0]+60,self.pos[1]+20),15,1)

        def answer(self): return self.action
        def restart(self,action): self.action=action

    class Button_rect:
        def __init__(self,text,width,height,pos,elevation,effect):
            gui_font = pygame.font.SysFont('Consolas',text[1])
            self.pressed = False
            self.elevation = elevation
            self.dynamic_elecation = elevation
            self.original_y_pos = pos[1]
            self.pos=pos
            self.width=width
            self.height=height

            # top rectangle
            self.top_rect = pygame.Rect(pos,(width,height))
            self.top_color = pygame.Color(71, 95, 119)

            # bottom rectangle
            self.bottom_rect = pygame.Rect(pos,(width,height))
            self.bottom_color = pygame.Color(53, 75, 94)
            #text
            self.text_surf = gui_font.render(text[0],True,WHITE)
            self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
            #effect
            self.effect=effect
        def draw(self,pos):
            # top rectangle
            self.original_y_pos = pos[1]
            self.top_rect = pygame.Rect(pos,(self.width,self.height))

            # bottom rectangle
            self.bottom_rect = pygame.Rect(pos,(self.width,self.height))
            # elevation logic
            self.top_rect.y = self.original_y_pos - self.dynamic_elecation
            self.text_rect.center = self.top_rect.center

            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

            self.rect=pygame.Rect((pos[0],pos[1]-self.dynamic_elecation),(self.width,self.height+self.dynamic_elecation))

            pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = self.effect)
            pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = self.effect)
            screen.blit(self.text_surf, self.text_rect)

            if self.check_click(): return True

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.top_rect.collidepoint(mouse_pos):
                self.top_color = pygame.Color(96, 128, 159)
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elecation = 0
                    self.pressed = True
                else:
                    self.dynamic_elecation = self.elevation
                    if self.pressed:
                        self.pressed=False
                        return True
            else:
                self.dynamic_elecation = self.elevation
                self.top_color = pygame.Color(71, 95, 119)

    class Buy_button:
        def __init__(self, level, width, height, pos, elevation, effect, coin, type='gem',type_button=1):
            self.text_list = ('Sold', 'Buy')
            self.level = level
            self.type_button=type_button
            # Core attributes
            self.pressed = False
            self.elevation = elevation
            self.dynamic_elecation = elevation
            self.original_y_pos = pos[1]
            self.pos = pos
            self.width = width
            self.height = height
            self.coin = coin
            self.type = type
            # top rectangle
            self.top_rect = pygame.Rect(pos, (width, height))
            self.top_color = pygame.Color(191, 191, 191)

            # bottom rectangle
            self.bottom_rect = pygame.Rect(pos, (width, height))
            self.bottom_color = pygame.Color(179, 179, 179)
            # effect
            self.effect = effect
            self.gui_font = pygame.font.Font(None, 35)

        def draw(self, money, pos, note=None):
            self.pos = pos
            self.note = note
            # top rectangle
            self.original_y_pos = pos[1]
            self.top_rect = pygame.Rect(pos, (self.width, self.height))

            # bottom rectangle
            self.bottom_rect = pygame.Rect(pos, (self.width, self.height))

            self.money = money
            # text
            self.text_surf = self.gui_font.render(self.text_list[self.level], True, BLACK)
            self.text_coin = self.gui_font.render(str(self.coin) + ' ' + self.type, True, BLACK)

            self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
            # elevation logic
            self.top_rect.y = self.original_y_pos - self.dynamic_elecation
            self.text_rect.center = self.top_rect.center

            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
            self.rect = pygame.Rect((self.pos[0], self.pos[1] - self.dynamic_elecation),(self.width, self.height + self.dynamic_elecation))

            pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=self.effect)
            pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=self.effect)
            screen.blit(self.text_surf, self.text_rect)
            screen.blit(self.text_coin, (self.pos[0] + 20, self.top_rect.y + self.height + 30))

            if self.check_click() == 0: return self.coin
            return 0

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.bottom_rect.collidepoint(mouse_pos):
                self.top_color = pygame.Color(217, 217, 217)
                text = font6.render(self.note, True, BLACK)
                screen.blit(text, (5, 175))
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elecation = 0
                    self.pressed = True
                else:
                    self.dynamic_elecation = self.elevation
                    if self.pressed == True:
                        self.pressed = False
                        if self.level == 1:
                            if self.money >= self.coin:
                                self.level = 0
                            else:
                                self.level = 1
                            return self.level
            else:
                self.dynamic_elecation = self.elevation
                self.top_color = pygame.Color(191, 191, 191)

        def answer(self):
            return self.level
        def restart(self):
            if self.type_button==0:self.level = 1

    class Buy_item:
        def __init__(self, grid):
            self.list_buy = {'Fish': [], 'Map': [], 'Other': []}
            self.list_grid = [[0, 1.5], [0, 1.5], [0, 1.5]]
            self.list_action = []
            self.shop = 'Map'
            self.x, self.y = 0, 2
            self.grid = grid + 1
            self.button_fish = Button_rect(('Fish', 30), 200, 50, (0, 120), 5, 0)
            self.button_map = Button_rect(('Map', 30), 200, 50, (width_screen / 3, 120), 5, 0)
            self.button_other = Button_rect(('Other', 30), 200, 50, (width_screen / 1.5, 120), 5, 0)
            self.font = pygame.font.Font(None, 12)

        def add(self, img, action, money, category='Other', type_money='gem',type_button=1, note=None):
            self.category = category
            self.type_money = type_money
            self.type_button=type_button
            if self.category == 'Fish':
                self.x, self.y = self.list_grid[0]
                if self.y < self.grid:
                    if self.x == self.grid - 1:
                        self.x = 0
                        self.y += 2
                    self.x += 1
                self.list_grid[0] = self.x, self.y
            elif self.category == 'Map':
                self.x, self.y = self.list_grid[1]
                if self.y < self.grid:
                    if self.x == self.grid - 1:
                        self.x = 0
                        self.y += 2
                    self.x += 1
                self.list_grid[1] = self.x, self.y
            elif self.category == 'Other':
                self.x, self.y = self.list_grid[2]
                if self.y < self.grid:
                    if self.x == self.grid - 1:
                        self.x = 0
                        self.y += 2
                    self.x += 1
                self.list_grid[2] = self.x, self.y
            self.note = note
            self.img = img
            self.rect = img.get_rect()
            self.money = money
            self.rect.center = (width_screen / self.grid * self.x, height_screen / self.grid * self.y)
            # action= 0:unlock ; 1:lock
            self.action = action
            self.button_buy(self.rect.center)

        def button_buy(self, rect):
            self.list_buy[self.category].append((Buy_button(self.action, 120, 80, rect, 8, 20, self.money,self.type_money,self.type_button), (self.x, self.y), self.img,self.type_money, self.note))
        def restart(self,name,index):
            self.list_buy[name][index][0].restart()
        def draw(self, score, gem):
            self.gem = gem
            self.list_action.clear()
            pygame.draw.rect(screen, pygame.Color(145, 200, 230), (0, 120, width_screen, 50))
            if self.button_fish.draw((0, 120)):
                self.shop = 'Fish'
            elif self.button_map.draw((width_screen / 2 - 100, 120)):
                self.shop = 'Map'
            elif self.button_other.draw((width_screen - 200, 120)):
                self.shop = 'Other'
            for i in self.list_buy[self.shop]:
                screen.blit(i[2], (width_screen / self.grid * i[1][0] - 46, height_screen / self.grid * i[1][1]))
                if i[3] == 'gem':
                    self.gem -= i[0].draw(gem, (width_screen / self.grid * i[1][0] - 55, height_screen / self.grid * i[1][1] + 110), i[4])
            self.list_action = [j[0].answer() for i in self.list_buy for j in self.list_buy[i]]

            return (self.gem, self.list_action)

    def draw_menu_setting(color, rect):
        screen.fill(pygame.Color(61, 143, 88))
        pygame.draw.rect(screen, color, rect,border_radius=30)
        font1 = pygame.font.SysFont('consolas', 38, bold=True)
        sound_text= font1.render('Sound:',True,(0,255,220))
        sound_effect_text= font1.render('Sound Effect:',True,(0,255,220))
        vol_text= font1.render('Volume:',True,(0,255,220))
        screen.blit(sound_text, (width_screen/8-40,height_screen/8-20))
        screen.blit(sound_effect_text, (width_screen/8-40,height_screen/4-20))
        screen.blit(vol_text, (width_screen/8-40,height_screen/8*3-20))

        sound_buttonX,sound_buttonY=(width_screen/4*1.5),(height_screen/8-20)
        sound_effect_buttonX, sound_effect_buttonY = (width_screen / 4 * 2), (height_screen / 8*2 - 20)
        sound_bar_x, sound_bar_y = int(width_screen / 4*1.5), int(height_screen / 8 * 2.9)
        sound_bar.setX(sound_bar_x)
        sound_bar.setY(sound_bar_y)

        sound_button.draw(screen,(sound_buttonX,sound_buttonY))
        sound_effect_button.draw(screen,(sound_effect_buttonX,sound_effect_buttonY))
        pygame_widgets.update(events)

    def rect_distance(rect1, rect2):
        if rect1[0] > rect2[0]+rect2[2]:
            distance=rect1[0] - (rect2[0]+rect2[2])
            return distance
        elif rect2[0] > rect1[0]+rect1[2] :
            distance=rect2[0] - (rect1[0]+rect1[2])
            return distance
        if rect2[1] > rect1[1]+rect1[3] :
            distance=rect2[1] - (rect1[1]+rect1[3])
            return distance
        elif rect1[1]>rect2[1]+rect2[3] :
            distance=rect1[1]-(rect2[1]+rect2[3])
            return distance
        return False

    class Time:
        def __init__(self,sec,count_time_bar):
            self.sec=sec
            self.count_time_bar=count_time_bar
        def count_time(self):
            if self.sec>0:
                self.sec-=timiner
                len_timebar=int(width_screen*(self.sec/local_sec))
                if food1[15]==0:
                    self.count_time_bar+=change_time
                    color_time_bar=hsv_to_rgb(self.count_time_bar,0.75,1)
                    pygame.draw.rect(screen,(color_time_bar[0]*255,color_time_bar[1]*255,color_time_bar[2]*255),(0,0,len_timebar,10),border_top_right_radius=5,border_bottom_right_radius=5)
                else:pygame.draw.rect(screen,WHITE,(0,0,len_timebar,10))
            elif self.sec<=0: return 1

    class Dot:
        def __init__(self, pos):
            self.gravity = uniform(4, 7)
            self.y = pos[1]+15
            self.x = pos[0]+15
            self.speed = uniform(2, 7)
        def draw(self):
            self.x -= self.speed
            self.y -= self.gravity
            screen.blit(spakle_img, (self.x, self.y))
            if self.y > height_screen: return True
    spakle_img=pygame.image.load('resources/effect/sparkle.png')
    #board
    board_button_img=pygame.image.load('resources/img/board1.png').convert_alpha()
    board1_button_img = pygame.image.load('resources/img/board2.png').convert_alpha()
    board1_buttonX,board1_buttonY=(width_screen/4-70),((height_screen/8)*5-60)
    board1_button=Button(board1_buttonX,board1_buttonY,board_button_img)

    board2_buttonX,board2_buttonY=(width_screen/4*3-70),((height_screen/8)*5-60)
    board2_button=Button(board2_buttonX,board2_buttonY,board_button_img)

    board3_buttonX,board3_buttonY=(width_screen/4-70),((height_screen/8)*7-60)
    board3_button=Button(board3_buttonX,board3_buttonY,board_button_img)

    board4_buttonX,board4_buttonY=(width_screen/4*3-70),((height_screen/8)*7-60)
    board4_button=Button(board4_buttonX,board4_buttonY,board_button_img)

    board5_button = Button(board1_buttonX, board1_buttonY, board1_button_img)

    board6_button = Button(board2_buttonX, board2_buttonY, board1_button_img)

    board7_button = Button(board3_buttonX, board3_buttonY, board1_button_img)

    board8_button = Button(board4_buttonX, board4_buttonY, board1_button_img)

    #game fish
    map_img=(pygame.image.load('resources/img_game/big fish eat small fish/map/map1 (1).png').convert_alpha(),
             pygame.image.load('resources/img_game/big fish eat small fish/map/map2 (1).png').convert_alpha(),
             pygame.image.load('resources/img_game/big fish eat small fish/map/map3 (1).png').convert_alpha(),
             pygame.image.load('resources/img_game/big fish eat small fish/map/map4 (1).png').convert_alpha(),
             pygame.image.load('resources/img_game/big fish eat small fish/map/map5 (1).png').convert_alpha(),
             pygame.image.load('resources/img_game/big fish eat small fish/map/map6 (1).png').convert_alpha(),
             pygame.image.load('resources/img_game/big fish eat small fish/map/map7 (1).png').convert_alpha()
             )
    map_buy_img=(pygame.image.load('resources/img_game/big fish eat small fish/map/map1 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/map/map2 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/map/map3 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/map/map4 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/map/map5 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/map/map6 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/map/map7 (2).png').convert_alpha()
                 )
    shark_img=(Fish((100,200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark1 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark1 (2).png').convert_alpha(),7.5),
           Fish((100,200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark2 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark2 (2).png').convert_alpha(), 6),
           Fish((100, 200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark3 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark3 (2).png').convert_alpha(), 5),
           Fish((100, 200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark4 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark4 (2).png').convert_alpha(),4.5),
           Fish((100, 200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark5 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark5 (2).png').convert_alpha(),5.5),
           Fish((100, 200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark6 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark6 (2).png').convert_alpha(), 6),
           Fish((100, 200),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark7 (1).png').convert_alpha(),pygame.image.load('resources/img_game/big fish eat small fish/shark/shark7 (2).png').convert_alpha(),5.5),
    )


    whale_img = [pygame.image.load('resources/img_game/big fish eat small fish/fish1/whale (1).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/whale (2).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/whale (3).png').convert_alpha()]

    fish1_img = [pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish1 (1).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish1 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish1 (3).png').convert_alpha()]

    fish2_img=[pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish2 (1).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish2 (2).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish2 (3).png').convert_alpha()]

    fish3_img=[pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish3 (1).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish3 (2).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish3 (3).png').convert_alpha()]

    fish4_img = [pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish4 (1).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish4 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish4 (3).png').convert_alpha()]

    fish5_img=[pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish5 (1).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish5 (2).png').convert_alpha(),
               pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish5 (3).png').convert_alpha()]

    fish6_img = [pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish6 (1).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish6 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish6 (3).png').convert_alpha()]

    fish7_img = [pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish7 (1).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish7 (2).png').convert_alpha(),
                 pygame.image.load('resources/img_game/big fish eat small fish/fish1/fish7 (3).png').convert_alpha()]

    sea_bg_img=(
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg4.jpg').convert_alpha()),
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg5.jpg').convert_alpha()),
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg6.jpg').convert_alpha()),
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg7.jpg').convert_alpha()),
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg8.jpg').convert_alpha()),
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg9.jpg').convert_alpha()),
        Background(pygame.image.load('resources/img_game/big fish eat small fish/sea_bg10.jpg').convert_alpha())
    )

    sound_buttonX, sound_buttonY = (width_screen / 2), (height_screen / 8 - 20)
    sound_effect_buttonX, sound_effect_buttonY = (width_screen / 4 * 1.5), (height_screen / 8 * 1.75 - 20)
    sound_button = Button_switch(True, (sound_buttonX, sound_buttonY))
    sound_effect_button = Button_switch(True, (sound_effect_buttonX, sound_effect_buttonY))
    try:
        with open('his.txt') as text_file:
            if len(open('his.txt').read())>0:
                history=text_file.readline().split()
                gem=int(text_file.readline())
                vol=float(text_file.readline())
                food1=text_file.readline().split()
                sound_button.restart(bool(int(food1[0])));sound_effect_button.restart(bool(int(food1[1])))
                food1=list(map(int,text_file.readline().split()))
                date_his=int(text_file.readline())
                streak = int(text_file.readline())
                total_answer=load(text_file)
            else:
                history=(0,0)
                gem=0
                vol=0.5
                food1=[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
                date_his=int(datetime.now().strftime('%d'))
                streak=1
                total_answer = [[0, 0, 0, 0] for _ in range(13)]
    except :
        open('his.txt','w+')
        history=(0,0)
        gem=0
        vol=0.5
        food1=[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
        date_his = int(datetime.now().strftime('%d'))
        streak = 1
        total_answer = [[0, 0, 0, 0] for _ in range(13)]
    date_now=datetime.now().strftime('%d')
    bite1_sound=pygame.mixer.Sound('resources/sounds/bite (1).ogg')
    bite2_sound = pygame.mixer.Sound('resources/sounds/bite (2).ogg')
    bite3_sound = pygame.mixer.Sound('resources/sounds/bite (3).ogg')

    fish_list=([food1[0],fish1_img,randint(1,5),randint(2,5),(10,2000-100),(150,height_screen-100),1,1,bite3_sound],
        [food1[1],fish2_img,randint(1,5),randint(1,3),(100,2000-100),(150,height_screen-100),2,1,bite3_sound],
        [food1[2],fish3_img,randint(5,10),1,(30,2000-50),(20,height_screen-20),3,2,bite3_sound],
        [food1[3],fish4_img, randint(1, 4), randint(1, 3), (100, 2000 - 100), (150, height_screen - 100), 4,3,bite2_sound],
        [food1[4],fish5_img,randint(5,10),1,(30,2000-50),(20,height_screen-20),3,3,bite2_sound],
        [food1[5],fish6_img, randint(2, 6), 1, (30, 2000 - 50), (20, height_screen - 20), 5, 10,bite2_sound],
        [food1[6],fish7_img,randint(2,4),1,(280,2000-160),(20,height_screen-20),randint(2,5),10,bite1_sound],
        [food1[7],whale_img,randint(1,2),1,(280,780),(0,300),randint(1,3),20,bite1_sound])
    map_pos=(width_screen/2,height_screen/2)
    list_map=(Map(map_pos,map_img[0],sea_bg_img[0],shark_img[0],8),
              Map(map_pos,map_img[1],sea_bg_img[1],shark_img[1],9),
              Map(map_pos,map_img[2],sea_bg_img[2],shark_img[2],10),
              Map(map_pos,map_img[3],sea_bg_img[3],shark_img[3],11),
              Map(map_pos,map_img[4],sea_bg_img[4],shark_img[4],12),
              Map(map_pos,map_img[5],sea_bg_img[5],shark_img[5],13),
              Map(map_pos, map_img[6], sea_bg_img[6],shark_img[6], 14)
              )

    # effect
    rainbow_effect_img=pygame.image.load('resources/effect/rainbow.png').convert_alpha()
    speed_effect_img=pygame.image.load('resources/effect/speed.png').convert_alpha()
    pet_effect_img=pygame.image.load('resources/effect/pet.png').convert_alpha()
    double_effect_img=pygame.image.load('resources/effect/star.png').convert_alpha()
    freeze_effect_img=pygame.image.load('resources/effect/snowflake.png').convert_alpha()
    wand_effect_img=pygame.image.load('resources/img/magic-wand.png').convert_alpha()

    right_arrow_buttonX,right_arrow_buttonY=width_screen/4,height_screen/2
    right_arrow_button=Button_img3D(right_arrow_buttonX,right_arrow_buttonY,pygame.image.load('resources/img/arrow-right.png').convert_alpha())

    left_arrow_buttonX,left_arrow_buttonY=width_screen/4*3,right_arrow_buttonY
    left_arrow_button=Button_img3D(left_arrow_buttonX,left_arrow_buttonY,pygame.image.load('resources/img/arrow-left.png').convert_alpha())

    left_forward_buttonX, left_forward_buttonY = width_screen / 4, height_screen / 4*3
    left_forward_button = Button_img3D(left_forward_buttonX, left_forward_buttonY,pygame.image.load('resources/img/forward (1).png').convert_alpha())

    right_forward_buttonX, right_forward_buttonY = width_screen / 4 * 3, right_arrow_buttonY
    right_forward_button = Button_img3D(right_forward_buttonX, right_forward_buttonY,pygame.image.load('resources/img/forward (2).png').convert_alpha())

    forward_num=0
    # shop
    buy_menu=Buy_item(5)
    buy_menu.add(fish1_img[2],food1[0],0,'Fish')
    buy_menu.add(fish2_img[2],food1[1],1,'Fish')
    buy_menu.add(fish3_img[2],food1[2],2,'Fish')
    buy_menu.add(fish4_img[2],food1[3],3,'Fish')
    buy_menu.add(fish5_img[2],food1[4],5,'Fish')
    buy_menu.add(fish6_img[2],food1[5],10,'Fish')
    buy_menu.add(fish7_img[2],food1[6],10,'Fish')
    buy_menu.add(whale_img[2],food1[7],15,'Fish')
    buy_menu.add(map_buy_img[0],food1[8],0,'Map')
    buy_menu.add(map_buy_img[1],food1[9],10,'Map')
    buy_menu.add(map_buy_img[2],food1[10],15,'Map')
    buy_menu.add(map_buy_img[3],food1[11],20,'Map')
    buy_menu.add(map_buy_img[4],food1[12],25,'Map')
    buy_menu.add(map_buy_img[5],food1[13],30,'Map')
    buy_menu.add(map_buy_img[6],food1[14],35,'Map')
    buy_menu.add(rainbow_effect_img,food1[15],5,note='Thanh thời gian cầu vồng')
    buy_menu.add(speed_effect_img,food1[16],10,note='Gấp đôi tốc độ của cá mập khi nhấn chuột trái')
    buy_menu.add(pet_effect_img,food1[17],20,note='+5 xu khi trả lời đúng có pet bơi qua màn hình học tập')
    buy_menu.add(double_effect_img, food1[18], 10,type_button=0, note='Nhân đôi số điểm cho câu trả lời đúng trong 1 lần học')
    buy_menu.add(freeze_effect_img, food1[19], 5,type_button=0, note='Đóng băng thời gian 1 câu hỏi')
    buy_menu.add(wand_effect_img, food1[20], 20,'Other','gem',0,'Hiệu ứng đũa phép cho con trỏ chuột')

    #start
    sec,sec_game,a,b,real=5,15,0,0,[]
    start_buttonX,start_buttonY=(width_screen/2-50),(height_screen/4*3-50)
    start_button=Button_rect(('Start',27),100,100,(start_buttonX,start_buttonY),10,50)

    forward_buttonX,forward_buttonY=(width_screen/2-80),(height_screen/8*4.5-50)
    forward_button=Button_rect(('Play again',27),160,80,(forward_buttonX,forward_buttonY),10,25)

    goto_buttonX, goto_buttonY = (width_screen / 2 - 80), (height_screen / 8 * 3 - 50)
    goto_button = Button_rect(('Go to Menu', 25), 160, 50, (goto_buttonX, goto_buttonY), 10, 20)

    #setting
    setting_button_img=pygame.image.load('resources/img/settings.png').convert_alpha()
    setting_buttonX,setting_buttonY=(width_screen/4*2.75-50),(height_screen/4*3-50)
    setting_button=Button(setting_buttonX,setting_buttonY,setting_button_img)

    # shopping
    shopping_button_img=pygame.image.load('resources/img/store.png').convert_alpha()
    shopping_buttonX,shopping_buttonY=(width_screen/2-50),(height_screen/4*3.5-50)
    shopping_button=Button(shopping_buttonX,shopping_buttonY,shopping_button_img)

    #sound
    tick_sound=pygame.mixer.Sound('resources/sounds/tick.ogg')
    failed_sound=pygame.mixer.Sound('resources/sounds/failed.ogg')

    soundtrack='sounds/spring.ogg'
    happy_holiday='sounds/happy-holiday.ogg'
    japan_music='sounds/japan_music.ogg'
    funny_story='sounds/funny-story.ogg'
    music_name=soundtrack
    pygame.mixer.music.load('resources/'+soundtrack)
    pygame.mixer.music.play(-1)
    sound_list,sound_index=(soundtrack,japan_music,happy_holiday,funny_story),0
    sound_bar_x,sound_bar_y=int(width_screen/4*1.5),int(height_screen/8*1.75)
    sound_bar=Slider(screen, sound_bar_x,sound_bar_y,200, 20, min=1, max=100, step=2,colour=pygame.Color(0, 139, 139),handleColour=pygame.Color(65,225,210))
    sound_bar.setValue(vol*100)
    pygame.mixer.music.set_volume(vol)

    #review
    review_button=Button_rect(('Ôn Tập Tổng Hợp',20),200,50,(width_screen/4*3,height_screen/2-100),3,10)
    review_list=[]
    review_answer=0
    review_correct_answer=0
    review_flag=False

    #exit
    exit_buttonX,exit_buttonY=(width_screen/8*7-40),(height_screen/8*7-40)
    exit_button=Button_rect(('OK',35),80,80,(exit_buttonX,exit_buttonY),8,25)

    #close game
    close_button_img=pygame.image.load('resources/img/close (1).png').convert_alpha()
    close_buttonX,close_buttonY=(width_screen/16*15),(height_screen/16*0.75)
    close_button=Button_img3D(close_buttonX,close_buttonY,close_button_img)

    # play game
    play_game_button_img=pygame.image.load('resources/img/gamepad.png').convert_alpha()
    play_game_buttonY,play_game_buttonX=(height_screen/4*3-50),(width_screen/4*1.25-50)
    play_game_button=Button(play_game_buttonX,play_game_buttonY,play_game_button_img)

    #pause
    pause=pygame.image.load('resources/img/multimedia.png').convert_alpha()
    paused_buttonX,paused_buttonY=(width_screen/16*15.5-10),(height_screen/16*0.65)
    paused_button=Button_pause(20,20,paused_buttonX,paused_buttonY)

    # blog
    text_img=pygame.image.load('resources/img/text.png').convert_alpha()
    blog_button_img=pygame.image.load('resources/img/blog.png').convert_alpha()
    blog_buttonY,blog_buttonX=(height_screen/4*3-50),(width_screen/4*1.25-50)
    blog_button=Button(blog_buttonX,blog_buttonY,blog_button_img)
    #statistical
    statistical_button_img=pygame.image.load('resources/img/robot.png').convert_alpha()
    statistical_button=Button(width_screen-30,height_screen-30,statistical_button_img)

    easy_img=(pygame.image.load('resources/img/think.png').convert_alpha(),
              pygame.image.load('resources/img/shells.png').convert_alpha(),
              pygame.image.load('resources/img/reef.png').convert_alpha(),
              pygame.image.load('resources/img/turtle.png').convert_alpha(),
              pygame.image.load('resources/img/bubbles.png').convert_alpha())

    medium_img=(pygame.image.load('resources/img/seaweed (3).png').convert_alpha(),
                pygame.image.load('resources/img/think (1).png').convert_alpha(),
                pygame.image.load('resources/img/jellyfish.png').convert_alpha(),
                pygame.image.load('resources/img/jellyfish (1).png').convert_alpha(),
                pygame.image.load('resources/img/jellyfish (2).png').convert_alpha())

    difficult_img=(pygame.image.load('resources/img/teenager.png').convert_alpha(),
                   pygame.image.load('resources/img/seaweed (4).png').convert_alpha(),
                   pygame.image.load('resources/img/crab.png').convert_alpha(),
                   pygame.image.load('resources/img/starfish (2).png').convert_alpha(),
                   pygame.image.load('resources/img/sea-snail.png').convert_alpha())

    hard_img=(pygame.image.load('resources/img/scholar.png').convert_alpha(),
              pygame.image.load('resources/img/jellyfish (3).png').convert_alpha(),
              pygame.image.load('resources/img/graduation-hat.png').convert_alpha(),
              pygame.image.load('resources/img/beach.png').convert_alpha(),
              pygame.image.load('resources/img/clownfish.png').convert_alpha(),
              pygame.image.load('resources/img/coral.png').convert_alpha())

    intro_img=(pygame.image.load('resources/img/shark.png').convert_alpha(),
               pygame.image.load('resources/img/fish.png').convert_alpha(),
               pygame.image.load('resources/img/starfish.png').convert_alpha(),
               pygame.image.load('resources/img/starfish (1).png').convert_alpha(),
               pygame.image.load('resources/img/maths.png').convert_alpha(),
               pygame.image.load('resources/img/seaweed.png').convert_alpha())

    menu_img=(pygame.image.load('resources/img/sea.png').convert_alpha(),
              pygame.image.load('resources/img/seaweed (2).png').convert_alpha(),
              pygame.image.load('resources/img/coral (1).png').convert_alpha(),
              pygame.image.load('resources/img/stingray.png').convert_alpha(),
              pygame.image.load('resources/img/blowfish.png').convert_alpha())

    shark=(pygame.image.load('resources/img/baby_shark.png').convert_alpha(),
           pygame.image.load('resources/img/teenager_shark.png').convert_alpha(),
           pygame.image.load('resources/img/crazy_shark.png').convert_alpha(),
           pygame.image.load('resources/img/men_shark.png').convert_alpha(),
           pygame.image.load('resources/img/old_shark.png').convert_alpha())

    statics_img=(pygame.image.load('resources/img/robot (1).png').convert_alpha(),
           pygame.image.load('resources/img/bionic-eye.png').convert_alpha(),
           pygame.image.load('resources/img/robot-arm.png').convert_alpha(),
           pygame.image.load('resources/img/packages.png').convert_alpha(),
           pygame.image.load('resources/img/idea.png').convert_alpha(),
           pygame.image.load('resources/img/robot (2).png').convert_alpha(),
           pygame.image.load('resources/img/drone.png').convert_alpha(),
           pygame.image.load('resources/img/fish (1).png').convert_alpha())

    mouse_img=(pygame.image.load('resources/mouse/1.png').convert_alpha(),
         pygame.image.load('resources/mouse/2.png').convert_alpha(),
         pygame.image.load('resources/mouse/3.png').convert_alpha(),
         pygame.image.load('resources/mouse/4.png').convert_alpha(),
         pygame.image.load('resources/mouse/5.png').convert_alpha(),
         pygame.image.load('resources/mouse/6.png').convert_alpha(),
         pygame.image.load('resources/mouse/magic-wand.png').convert_alpha())
    mouse_set=0

    menu_button=tuple(Button_rect((str(i),25),50,50,(0,0),5,25) for i in range(1,14))

    opinion_img=[pygame.image.load('resources/opinion/'+str(i)+'.png').convert_alpha() for i in range(1,8)]
    fire_img=[pygame.image.load('resources/streak/fire ('+str(i)+').png').convert_alpha() for i in range(1,61)]
    count_img=[pygame.image.load('resources/count_number/' + str(i) + '.png').convert_alpha() for i in range(16)]
    fire_count=0

    ruby_img=pygame.image.load('resources/img/ruby.png').convert_alpha()
    shark1_img_title=pygame.image.load('resources/img/shark (3).png').convert_alpha()


    #font
    font = pygame.font.Font('resources/Dosis.ttf', 60)
    font1 = pygame.font.SysFont('Roboto Slab', 60, bold=True)
    font2 = pygame.font.Font('resources/BagelFatOne.ttf', 60)
    font3 = pygame.font.SysFont('consolas', 20)
    font4 = pygame.font.Font('resources/HARLOW.ttf', 80)
    font5 = pygame.font.SysFont('consolas', 80)
    font6 = pygame.font.SysFont('consolas', 15)
    largeText = pygame.font.SysFont('Open sans', 120)
    TextSurf = largeText.render('Pause', True, WHITE)
    textSurface1 = font1.render(' Thalassa Math ', True, WHITE)

    bubbleY=[height_screen+randint(5,20) for _ in range(4)]
    petY=height_screen+randint(5,20)
    speedX=2
    dot_list=[]
    streak_difference=int(date_now)-date_his
    if streak_difference>1:streak=1;total_answer=[[0,0,0,0] for _ in range(13)]
    elif streak_difference==1:streak+=1;total_answer=[[0,0,0,0] for _ in range(13)]

    #game_loop
    pygame.mouse.set_visible(0)
    hide,set_mode,set_cal,max_game_score,score,ran_map,board_index,spam_num,timing,double,new_score,bad_score=0,0,0,0,0,0,0,3,30,0,0,0
    highscore,total_score=map(int,history)
    running,now_color,level,int_level,length_level,clock,timiner=1,pygame.Color(61, 143, 88),'1',1,len(diction[0])-1,pygame.time.Clock(),1/timing
    screen.fill(now_color)
    while running:
        #loop
        size_screen=pygame.display.get_window_size()
        width_screen=max(size_screen[0],850)
        height_screen=max(size_screen[1],750)
        events=pygame.event.get()
        #set variable and size
        setting_buttonX,setting_buttonY=(width_screen/4*2.75-50),(height_screen/4*3-50)
        sound_play=sound_button.answer()
        sound_effect_play = sound_effect_button.answer()

        if not sound_play and pygame.mixer.music.get_busy():pygame.mixer.music.pause()
        elif sound_play and not pygame.mixer.get_busy() and hide!=7:pygame.mixer.music.unpause()

        if(hide==0):
            screen.fill(DEEPFORESTGREEN)
            screen.blit(intro_img[0],(width_screen/8,height_screen/8))
            screen.blit(intro_img[1],(width_screen/4*2.5-50,height_screen/8))
            screen.blit(intro_img[2],(width_screen/40,height_screen/4*0.15))
            screen.blit(intro_img[3],(width_screen/4*3.5,height_screen/4*2.5))
            screen.blit(intro_img[4],(width_screen/8-40,height_screen/2))
            k=width_screen//100
            for i in range(k): screen.blit(intro_img[5],(width_screen/k*i+15,height_screen-80))

            screen.blit(textSurface1,(width_screen/2-225,height_screen/2))

            start_buttonX,start_buttonY=(width_screen/2-50),(height_screen/4*3-50)
            blog_buttonY,blog_buttonX=(height_screen/4*3-50),(width_screen/4*1.25-50)
            if start_button.draw((start_buttonX,start_buttonY)):hide=11
            if setting_button.draw((setting_buttonX,setting_buttonY)):set_mode,hide=0,6
            if blog_button.draw((blog_buttonX,blog_buttonY)):set_mode,hide=0,10

        elif(hide==1):
            # set answer
            ques = diction[int_level-1][randint(0, length_level)]
            if level=='1':
                ran_num=ques[1]
                real = [ran_num, ran_num+ 1, ran_num + randint(2, 3),ran_num + randint(4, 5)]
                local_sec=6
            elif level=='2':
                ran_num=ques[1]
                real=[ran_num,ran_num-1,ran_num+randint(4,6),ran_num+randint(2,3)]
                set_cal=1 if set_cal==0 else 0
                local_sec=5
            elif level=='3':
                ran_num=ques[1]
                real=[ran_num,ran_num+1,ran_num+randint(2,3),ran_num+randint(4,5)]
                local_sec=10
            elif level=='4':
                ran_num = ques[1]
                real=[ran_num,ran_num-1,ran_num+randint(1,3),ran_num+randint(4,5)]
                local_sec=10
            elif level=='5':
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec=8
            elif level=='6':
                ran_num = ques[1]
                real = [ran_num, ran_num + 1, ran_num + randint(2, 3), ran_num + randint(4, 5)]
                local_sec = 12
            elif level=='7':
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec=15
            elif level=='8':
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec = 10
            elif level=='9':
                ques = ques[randint(0, len(ques) - 1)]
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec = 10
            elif level=='10':
                ques = ques[randint(0, len(ques) - 1)]
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec = 12
            elif level == '11':
                ques = ques[randint(0, len(ques) - 1)]
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec = 15
            elif level == '12':
                ques = ques[randint(0, len(ques) - 1)]
                ran_num = ques[1]
                real = [ran_num, ran_num - 1, ran_num + randint(1, 3), ran_num + randint(4, 5)]
                local_sec = 18
            elif level == '13':
                ran_num = ques[1]
                answer=ran_num
                real=['+','-','x',':']
                local_sec = 10
            if level!='13':answer=real[0]
            shuffle(real)
            text = ques[0]
            ##
            game_score, ran_map, sec_game, sec = 0,0,10,local_sec
            count_time_bar,change_time=0,1/(local_sec*65)
            time_bar=Time(sec,count_time_bar)
            max_game_score=0
            now_color=color[randint(0,len(color)-1)]
            speedY=change_time*975*(60/timing) if randint(0,5)==0 else 0
            petY = height_screen + randint(60, 80)
            frequence = 0.025
            angle = 0
            hide=13 if review_flag else 2

        if hide==2:
            if food1[19]==1:
                screen.fill(now_color)
                if time_bar.count_time(): hide=3
            else:screen.fill(ICE)

            paused_buttonX, paused_buttonY = (width_screen / 16 * 15 - 10), (height_screen / 16 * 0.75 - 10)
            paused_button.load(20, 20, paused_buttonX, paused_buttonY)

            #font
            textSurface = font.render(text,True,WHITE)

            screen.blit(textSurface, ((width_screen-textSurface.get_width())/2, height_screen/7))
            if level=='1':screen.blit(count_img[ran_num],(width_screen / 2 - 150, height_screen*0.25))
            textSurface = font3.render(str(score),False,WHITE)
            screen.blit(textSurface, (10, 15))

            x_top_board,y_top_board=(width_screen/4-97.5),((height_screen/8)*5-70)
            x_bottom_board, y_bottom_board=(width_screen/4*3-97.5),((height_screen/8)*7-70)
            board1_buttonX,board1_buttonY=x_top_board,y_top_board
            board2_buttonX,board2_buttonY=x_bottom_board, y_top_board
            board3_buttonX,board3_buttonY=x_top_board,y_bottom_board
            board4_buttonX,board4_buttonY=x_bottom_board, y_bottom_board
            x=len(real)
            #button1
            if x>0:
                textSurface1 = font2.render(str(real[0]), True, BLACK)
                if board1_button.draw((board1_buttonX,board1_buttonY)):hide,board_index=3,1
                else:screen.blit(textSurface1, ((width_screen/4-(textSurface1.get_width()/2)-8), (y_top_board+(textSurface1.get_height()/4)-8)))

            #button2
            if x > 1:
                textSurface2 = font2.render(str(real[1]), True, BLACK)
                if board2_button.draw((board2_buttonX,board2_buttonY)):hide,board_index=3,2
                else:screen.blit(textSurface2, ((width_screen/4*3-(textSurface2.get_width()/2)-8), (y_top_board+(textSurface2.get_height()/4)-8)))

            #button3
            if x > 2:
                textSurface3 = font2.render(str(real[2]), True, BLACK)
                if board3_button.draw((board3_buttonX,board3_buttonY)):hide,board_index=3,3
                else:screen.blit(textSurface3, ((width_screen/4-(textSurface3.get_width()/2)-8), (y_bottom_board+(textSurface3.get_height()/4)-8)))

            #button4
            if x > 3:
                textSurface4 = font2.render(str(real[3]), True, BLACK)
                if board4_button.draw((board4_buttonX,board4_buttonY)):hide,board_index=3,4
                else:screen.blit(textSurface4, ((width_screen/4*3-(textSurface4.get_width()/2)-8), (y_bottom_board+(textSurface4.get_height()/4)-8)))

            if paused_button.draw(): hide=7

            if level in ('1','2','3','4'):
                screen.blit(easy_img[0],(width_screen/8-50,height_screen/8-80))
                screen.blit(easy_img[1],(width_screen/8-40,height_screen/4*1.5-40))

                if bubbleY[0]<6: bubbleY[0]=height_screen+randint(5,25)
                else: bubbleY[0]-=1.25

                if bubbleY[1]<6: bubbleY[1]=height_screen+randint(5,25)
                else:bubbleY[1]-=1.5

                if bubbleY[2]<6: bubbleY[2]=height_screen+randint(5,25)
                else: bubbleY[2]-=1

                if bubbleY[3]<6: bubbleY[3]=height_screen+randint(5,25)
                else: bubbleY[3]-=0.85

                screen.blit(easy_img[2],((width_screen/5*0.35-40,height_screen-80)))
                screen.blit(easy_img[3],((width_screen/6*5-60,height_screen/4*1.5-60)))
                for i in range(4): screen.blit(easy_img[4],(width_screen/5*(i+1),bubbleY[i]))

            elif level in ('5','6','7','8'):
                screen.blit(medium_img[0],(width_screen/8*7-60,height_screen/4*0.75-75))
                screen.blit(medium_img[1],(width_screen/8-60,height_screen/4*0.65-75))

                if bubbleY[0]<6: bubbleY[0]=height_screen+randint(5,25)
                else: bubbleY[0]-=1
                screen.blit(medium_img[2],(width_screen/4*0.75+25,bubbleY[0]))

                if bubbleY[1]<6: bubbleY[1]=height_screen+randint(5,25)
                else: bubbleY[1]-=1.25
                screen.blit(medium_img[3],(width_screen/4*2.75+25,bubbleY[1]))

                if bubbleY[2]>height_screen: bubbleY[2]=randint(5,25)
                else: bubbleY[2]+=1.5
                screen.blit(medium_img[4],(width_screen/2,bubbleY[2]))

            elif level in ('9','10','11','12'):
                screen.blit(difficult_img[0],(width_screen/8-60,height_screen/4*0.65-75))
                for i in range(width_screen//100+1): screen.blit(difficult_img[1],(width_screen/(width_screen//100)*i+8.5,height_screen-80))

                if bubbleY[3]>width_screen-90:speedX=-2
                elif bubbleY[3]<5:speedX=2

                bubbleY[3]+=speedX
                screen.blit(difficult_img[2],(bubbleY[3],height_screen-70))
                screen.blit(difficult_img[3],(width_screen/4*3-40,height_screen/2*0.75))
                screen.blit(difficult_img[3],(width_screen/4*0.75-40,height_screen/4*1.5))
                screen.blit(difficult_img[4],(width_screen/4*2.15,height_screen/4*1.25))

            elif level in '13':
                screen.blit(hard_img[0],(width_screen/8-60,height_screen/4*0.65-75))
                screen.blit(hard_img[1],(width_screen/2-40,height_screen/4*2.5+40))
                screen.blit(hard_img[2],(width_screen/8*7-60,height_screen/4*0.65-75))
                if bubbleY[3]>width_screen-90:bubbleY[3]=5
                bubbleY[3]+=abs(speedX)
                for i in range((width_screen//100)+1): screen.blit(hard_img[3],(width_screen/(width_screen/100)*i,height_screen-60))
                screen.blit(hard_img[4],(bubbleY[3],height_screen/4*1.5-40))
                screen.blit(hard_img[5],(width_screen-75,height_screen/4*1.5-40))

            if food1[17]==0:
                if petY < -100:petY = height_screen + randint(60, 80)
                else:petY -= speedY
                screen.blit(pet_effect_img, (width_screen / 2, petY))

        elif hide==3:
            if food1[19]==0:
                food1[19] = 1
                buy_menu.restart('Other', 4)
            if(real[board_index-1] == answer and not time_bar.count_time()):
                if sound_effect_play:pygame.mixer.Sound.play(tick_sound)
                t=10
                if int(streak)%7==0 and streak!='0':t*=2
                if (petY > -20 or petY<height_screen) and speedY != 0:t+=5
                if food1[18] == 0: t *= 2; double = 1
                score+=t
                if len(review_list) == 1 and review_flag:hide=14;total_score+=score
                else: hide=1
                if review_flag:review_correct_answer+=1
                else:total_answer[int(level) - 1][1] += 1
            else:
                if sound_effect_play: pygame.mixer.Sound.play(failed_sound)
                if not review_flag:
                    total_score+=score
                    if double == 1:food1[18] = 1; buy_menu.restart('Other', 3)
                    double = 0
                    if score>0:gem+=1
                    if(highscore<score):highscore,new_score=score,1; gem+=1
                if not review_flag:hide=5
                else:
                    if len(review_list) > 1:hide=1
                    else:hide=14; total_score+=score
            if not review_flag:
                total_answer[int(level)-1][0]+=1
                for i in total_answer:i[2] = 200 / i[0] * i[1] if i[0] > 0 else 0;i[3] = i[0] / i[1] if i[1] > 0 else 0
            elif len(review_list) != 1: review_list.pop(0); review_answer+=1;level=review_list[0]

        elif hide==4:
            screen.fill(DARKSTEELBLUE)
            # time game
            if sec_game>0 and game_score>-1: sec_game-=timiner
            elif sec_game<0  and game_score>-1:
                total_score+=game_score
                list_map[ran_map].restart()
                hide=8

            game_score=list_map[ran_map].draw((width_screen/2,height_screen/2),sec_game,food1,spam_num)
            max_game_score=max(game_score,max_game_score)

            if game_score==-1:
                mouse_set=4
                right_arrow_buttonX,right_arrow_buttonY=(width_screen/4*3.5),(height_screen/2)
                if right_arrow_button.draw((right_arrow_buttonX,right_arrow_buttonY)):
                    if ran_map<len(list_map)-1:ran_map+=1
                    else:ran_map=0
                left_arrow_buttonX,left_arrow_buttonY=(width_screen/8),right_arrow_buttonY
                if left_arrow_button.draw((left_arrow_buttonX,left_arrow_buttonY)):
                    if ran_map>0:ran_map-=1
                    else:ran_map=len(list_map)-1
            else: mouse_set=5

            close_buttonX,close_buttonY=(width_screen/16*15.5),(height_screen/16*0.75)
            if close_button.draw((close_buttonX,close_buttonY)):
                if game_score>0:total_score+=game_score
                list_map[ran_map].restart()
                hide=8

        elif hide==5:
            screen.fill(DARKSTEELBLUE)
            if bad_score>2:screen.blit(opinion_img[6], (50, height_screen - 350))
            elif new_score==1: screen.blit(opinion_img[0], (20, height_screen - 300))
            elif score==0:screen.blit(opinion_img[5],(width_screen-250,height_screen-300))
            elif score<=20:screen.blit(opinion_img[4],(0,height_screen-250))
            elif score<=highscore/2:screen.blit(opinion_img[3],(0,height_screen-300))
            elif score<=highscore-10:screen.blit(opinion_img[2],(0,height_screen-250))
            elif score <= highscore:screen.blit(opinion_img[1],(width_screen-280,height_screen-300))

            textSurface1 = font3.render(str(total_score),False,WHITE)
            screen.blit(textSurface1,(5,5))
            textSurface1 = font3.render('gem:' + str(gem), False, WHITE)
            screen.blit(textSurface1, (5, 30))
            screen.blit(ruby_img,(textSurface1.get_width()+10,25))

            textSurface1 = font4.render('Score:'+str(score),True,WHITE)
            screen.blit(textSurface1, ((width_screen-textSurface1.get_width())/2, 80))
            textSurface1 = font4.render('Highscore:'+str(highscore),True,WHITE)
            screen.blit(textSurface1, ((width_screen-textSurface1.get_width())/2, 160))

            forward_buttonX,forward_buttonY=(width_screen/2-80),(height_screen/8*4.5-40)
            if forward_button.draw((forward_buttonX,forward_buttonY)): new_score,score,hide,bad_score=0,0,1,0 if bad_score>=2 and score>=20 else bad_score
            goto_buttonX, goto_buttonY = (width_screen / 2 - 80), (height_screen / 8 * 3.5 - 25)
            if goto_button.draw((goto_buttonX, goto_buttonY)): new_score,score, hide,bad_score = 0,0, 11,0 if bad_score>2 and score>=20 else bad_score
            if(score>=10 and bad_score<=2):
                setting_buttonX=(width_screen/4*2.5-50)
                play_game_buttonY=(height_screen/4*3-50)
                play_game_buttonX=(width_screen/4*1.5-50)
                if play_game_button.draw((play_game_buttonX,play_game_buttonY)):
                    if score <= 20: bad_score += 1
                    score,ran_map,hide=0,0,4
                shopping_buttonX,shopping_buttonY=(width_screen/2-50),(height_screen/4*3.5-50)
                if shopping_button.draw((shopping_buttonX,shopping_buttonY)):set_mode,hide=5,9
            if setting_button.draw((setting_buttonX,setting_buttonY)):set_mode,hide=5,6
        elif hide==6:
            screen.fill(now_color)
            draw_menu_setting(pygame.Color(105,160,125), (10, 10, width_screen-20, height_screen-20))
            vol=sound_bar.getValue()/100
            pygame.mixer.music.set_volume(vol)

            position_shark=(width_screen/2-180,height_screen/8*6-150)

            if level in ('1','2','3'): screen.blit(shark[0],position_shark)
            elif level in ('5','6','7'): screen.blit(shark[2],position_shark)
            elif level in ('9','10','11'): screen.blit(shark[1],position_shark)
            elif level in '13': screen.blit(shark[4],position_shark)
            elif level in ('4','8','12'): screen.blit(shark[3],position_shark)
            exit_buttonX,exit_buttonY=(width_screen/8*7-40),(height_screen/8*7-40)
            if exit_button.draw((exit_buttonX,exit_buttonY)):
                hide=set_mode
                if music_name!=sound_list[sound_index]:
                    music_name=sound_list[sound_index]
                    pygame.mixer.music.load('resources/'+sound_list[sound_index])
                    if sound_play: pygame.mixer.music.play(-1)
        elif hide==7:
            pygame.mixer.music.pause()
            screen.fill(DARKSLATEGRAY)
            screen.blit(TextSurf, (width_screen/2-160,0))
            paused_buttonX, paused_buttonY = (width_screen / 16 * 15 - 10), (height_screen / 16 * 0.75 - 10)
            paused_button.load(20, 20, paused_buttonX, paused_buttonY)
            if not paused_button.draw():
                if sound_play: pygame.mixer.music.unpause()
                hide=set_mode
            screen.blit(pause,(width_screen/2-150,height_screen/2-150))

        elif hide==8:
            screen.fill(TEAL)
            textSurface1 = font3.render(str(total_score),False,WHITE)
            screen.blit(textSurface1,(5,5))
            forward_buttonX,forward_buttonY=(width_screen/2-80),(height_screen/8*4.5-40)
            if forward_button.draw((forward_buttonX,forward_buttonY)):new_score,score,hide=0,0,1
            goto_buttonX, goto_buttonY = (width_screen / 2 - 80), (height_screen*0.4)
            if goto_button.draw((goto_buttonX, goto_buttonY)): score, hide = 0, 11
            if setting_button.draw((setting_buttonX,setting_buttonY)):new_score,set_mode,hide=0,8,6
            shopping_buttonX,shopping_buttonY=(width_screen/4*1.25-50),(height_screen/4*3-50)
            if shopping_button.draw((shopping_buttonX,shopping_buttonY)):set_mode,hide=8,9
        elif hide==9:
            screen.fill(SAND)
            textSurface1 = font5.render('SHOP',True,WHITE)
            textRect1=textSurface.get_rect()
            textRect1.center=((width_screen-textSurface1.get_width())/2,25)
            textSurface2 = font3.render(str(total_score),False,BLACK)
            screen.blit(textSurface1,textRect1.center)
            screen.blit(textSurface2,(5,5))
            food2=buy_menu.draw(total_score,gem)
            food1=food2[1]
            for i in range(len(fish_list)):fish_list[i][0]=food2[1][i]
            gem=food2[0]
            exit_buttonX,exit_buttonY=(width_screen/8*7.5-40),(height_screen/8*7.5-40)
            if exit_button.draw((exit_buttonX,exit_buttonY)): hide=set_mode

        elif hide==10:
            screen.fill(now_color)
            screen.blit(text_img,(0,0))
            exit_buttonX,exit_buttonY=(width_screen/8*7-40),(height_screen/8*7-40)
            if exit_button.draw((exit_buttonX,exit_buttonY)): hide=set_mode
        elif hide==11:
            screen.fill(LIGHTBLUE)
            score=0
            textSurface1=font1.render('Menu',True,WHITE)
            row,col=width_screen//150,height_screen//150
            screen.blit(textSurface1,(width_screen/2-textSurface1.get_width()/2,height_screen/12-11))
            menu_y,menu_x=1,0
            for i in range(len(menu_button)):
                menu_x+=1;x=i+1
                if menu_button[i].draw((width_screen/row*menu_x-25,height_screen/col*menu_y+25)):
                    int_level,level,hide,set_mode,length_level=x,str(x),1,2,len(diction[x-1])-1
                    if level in ('1', '2', '3'):sound_index, mouse_set = 0, 0
                    elif level in ('5', '6', '7'):sound_index, mouse_set = 2, 2
                    elif level in ('9', '10', '11'):sound_index, mouse_set = 1, 1
                    elif level in ('4', '8', '12','13'):sound_index, mouse_set = 3, 3
                    if music_name != sound_list[sound_index]:
                        music_name = sound_list[sound_index]
                        pygame.mixer.music.load('resources/' + sound_list[sound_index])
                        if sound_play: pygame.mixer.music.play(-1)
                if x%(row-1)==0:menu_x,menu_y=0,menu_y+1
            for i in range(width_screen//95+1):screen.blit(menu_img[0],(width_screen/(width_screen/95)*i,height_screen-85))

            textSurface1 = font3.render(str(total_score), False, WHITE)
            screen.blit(textSurface1, (5, 5))
            textSurface1 = font3.render('gem:' + str(gem), False, WHITE)
            screen.blit(textSurface1, (5, 30))
            screen.blit(ruby_img, (textSurface1.get_width() + 10, 25))

            screen.blit(menu_img[1], (width_screen/8*7,height_screen/8))
            screen.blit(menu_img[2], (0, height_screen / 3))
            screen.blit(menu_img[3], (width_screen/10*3-50, height_screen / 10*3))
            screen.blit(menu_img[4], (width_screen / 10*8.5, height_screen / 10 * 7))
        elif hide==12:
            screen.fill(LIGHTGRAY)
            for i in range(forward_num*5,min(forward_num*5+5,len(total_answer))):
                if total_answer[i][3] >= 1 and total_answer[i][3] < 1.1:st_color = pygame.Color(10, 200, 10);text='Xuất sắc'
                elif total_answer[i][3] >= 1.1 and total_answer[i][3] < 1.3:st_color = pygame.Color(130, 250, 30);text='Tốt,tiếp tục phát huy'
                elif total_answer[i][3] >= 1.3 and total_answer[i][3] < 2:st_color = pygame.Color(250, 250, 30);text='Cần ôn tập thêm'
                elif total_answer[i][3] >= 2 and total_answer[i][3] < 4:st_color = pygame.Color(230, 80, 15);text='Chưa nắm vững'
                else:st_color = pygame.Color(242, 15, 12);text='Chưa ôn tập'
                hs=height_screen/8*(i%5+1)-10
                textSurface=font3.render(' '.join(('Level:',str(i+1))),True,DARKSLATEGRAY)
                screen.blit(textSurface,(width_screen/16,hs))
                textSurface=font3.render(text,True,DARKSLATEGRAY)
                screen.blit(textSurface,(width_screen/1.5,hs))
                pygame.draw.rect(screen,DARKGRAY,(width_screen/4+total_answer[i][2],hs,200-total_answer[i][2],20),border_radius=10)
                pygame.draw.rect(screen,st_color,(width_screen/4,hs,total_answer[i][2],20),border_radius=10)
            if review_button.draw((width_screen/2-75,height_screen/4*3-35)):
                review_list=[str(randint(1,13)) for _ in range(21)]
                hide,level,review_flag,review_answer,review_correct_answer,score=1,review_list[0],True,0,0,0
            exit_buttonX, exit_buttonY = (width_screen / 8), (height_screen / 8 * 7 - 40)
            if exit_button.draw((exit_buttonX, exit_buttonY)): hide = set_mode
            left_forward_buttonX, left_forward_buttonY = width_screen / 3, height_screen / 8 * 7
            right_forward_buttonX, right_forward_buttonY = width_screen / 1.5, left_forward_buttonY
            if left_forward_button.draw((left_forward_buttonX,left_forward_buttonY)):
                forward_num -= 1
                if forward_num<0:forward_num=0
            if right_forward_button.draw((right_forward_buttonX,right_forward_buttonY)):
                forward_num += 1
                if forward_num>2:forward_num=2
        elif hide==13:
            if food1[19]==1:
                screen.fill(DARKIRON)
                if time_bar.count_time(): hide=3
            else:screen.fill(ICE)

            paused_buttonX, paused_buttonY = (width_screen / 16 * 15 - 10), (height_screen / 16 * 0.75 - 10)
            paused_button.load(20, 20, paused_buttonX, paused_buttonY)

            #font
            textSurface = font.render(text,True,WHITE)

            screen.blit(textSurface, ((width_screen-textSurface.get_width())/2, height_screen/7))
            if level=='1':screen.blit((pygame.image.load('resources/count_number/' + str(ran_num) + '.png').convert_alpha()),(width_screen / 2 - 150, height_screen*0.25))
            textSurface = font3.render(str(score),False,WHITE)
            screen.blit(textSurface, (5, 15))

            x_top_board,y_top_board=(width_screen/4-97.5),((height_screen/8)*5-70)
            x_bottom_board, y_bottom_board=(width_screen/4*3-97.5),((height_screen/8)*7-70)
            board1_buttonX,board1_buttonY=x_top_board,y_top_board
            board2_buttonX,board2_buttonY=x_bottom_board, y_top_board
            board3_buttonX,board3_buttonY=x_top_board,y_bottom_board
            board4_buttonX,board4_buttonY=x_bottom_board, y_bottom_board
            x=len(real)
            #button5
            if x>0:
                textSurface1 = font2.render(str(real[0]), True, BLACK)
                if board5_button.draw((board1_buttonX,board1_buttonY)):hide,board_index=3,1
                else:screen.blit(textSurface1, ((width_screen/4-(textSurface1.get_width()/2)-8), (height_screen/8*4.5-8)))

            #button6
            if x > 1:
                textSurface2 = font2.render(str(real[1]), True, BLACK)
                if board6_button.draw((board2_buttonX,board2_buttonY)):hide,board_index=3,2
                else:screen.blit(textSurface2, ((width_screen/4*3-(textSurface2.get_width()/2)-8), (height_screen/8*4.5-8)))

            #button7
            if x > 2:
                textSurface3 = font2.render(str(real[2]), True, BLACK)
                if board7_button.draw((board3_buttonX,board3_buttonY)):hide,board_index=3,3
                else:screen.blit(textSurface3, ((width_screen/4-(textSurface3.get_width()/2)-8), (height_screen/8*6.5-8)))

            #button8
            if x > 3:
                textSurface4 = font2.render(str(real[3]), True, BLACK)
                if board8_button.draw((board4_buttonX,board4_buttonY)):hide,board_index=3,4
                else:screen.blit(textSurface4, ((width_screen/4*3-(textSurface4.get_width()/2)-8), (height_screen/8*6.5-8)))

            if paused_button.draw(): hide=7

            screen.blit(statics_img[1], (width_screen/8*6.5, 50))
            screen.blit(statics_img[2], (10, height_screen - 180))
            screen.blit(statics_img[3], (width_screen-150, height_screen - 120))
            screen.blit(statics_img[4], (0, height_screen/2-80))

            if bubbleY[0] > width_screen - 100:speedX = -2
            elif bubbleY[0] < 5:speedX = 2
            bubbleY[0] += speedX
            screen.blit(statics_img[0], (bubbleY[0], height_screen - 100))

            if food1[17]==0:
                if petY < -100:petY = height_screen + randint(60, 80)
                else:petY -= speedY
                screen.blit(pet_effect_img, (width_screen / 2, petY))

        elif hide==14:
            screen.fill(WHITESMOKE)
            review_flag,set_mode=False,2
            textSurface=font4.render('Correct answer: '+str(review_correct_answer),True,BLACK)
            screen.blit(textSurface,(width_screen/2-textSurface.get_width()/2,height_screen/5))
            screen.blit(statics_img[5], (5, height_screen-240))
            x=width_screen//2+sin(angle)*(width_screen/3)
            angle+=frequence
            screen.blit(statics_img[6], (x, 10))
            bubbleY[1]+=4
            if bubbleY[1]>width_screen:bubbleY[1]=0
            screen.blit(statics_img[7], (bubbleY[1], height_screen/2))

            exit_buttonX, exit_buttonY = (width_screen / 8 * 7 - 40), (height_screen / 8 * 7 - 40)
            if exit_button.draw((exit_buttonX, exit_buttonY)): hide = 11

        for event in events:
            if event.type==pygame.QUIT:
                if type(streak)!='str':streak = str(streak)
                if double == 1: food1[18] = 1;buy_menu.restart('Other', 3)
                with open('his.txt','w') as text_file:
                    text_file.write(' '.join((str(highscore),str(total_score),'\n')))
                    text_file.write(str(gem)+'\n')
                    text_file.write(str(vol)+'\n')
                    text_file.write(' '.join(('1' if sound_play else '0','1' if sound_effect_play else '0','\n')))
                    text_file.write(' '.join([str(i) for i in food1]))
                    text_file.write('\n'+date_now+'\n')
                    text_file.write(streak+'\n')
                    dump(total_answer,text_file)
                running=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    open('his.txt', 'w').write('')
                    highscore, total_score = (0, 0)
                    gem, score = 0, 0
                    sound_button.restart(True);sound_effect_button.restart(True)
                    food1 = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                    vol = 0.5

        if hide in (5, 8, 11):
            streak = str(streak)
            a = 11 * len(streak)
            fireX, fireY = width_screen / 8 * 7 - a, height_screen / 16 - 22
            pygame.draw.rect(screen, PERU, (fireX, height_screen / 16 - 25, 80 + a, 50), border_radius=25)
            screen.blit(fire_img[int(fire_count)], (fireX + 10, fireY))
            textSurface = font3.render(streak, True,BLANCHEDALMOND if int(streak)%7==0 else WHITE if int(streak) < 365 else GOLD)
            screen.blit(textSurface, (fireX + 56, height_screen / 16 - 8))
            fire_count += 1
            if fire_count == 60: fire_count = 0
            if statistical_button.draw((width_screen - 65, height_screen / 8 * 3 - 30)):set_mode=hide; hide = 12

        pos = list([i - 12 for i in pygame.mouse.get_pos()]) + [80, 80]
        for i in dot_list:
            if i.draw(): dot_list.remove(i)
        if (pos[1] < height_screen - 30 and pos[1] > 0) and (pos[0] < width_screen - 30 and pos[0] > 0):
            if food1[20] == 0:
                mouse_set = 6
                if randint(1, 50) == 48:
                    sparkle_pos = pos[0:2]
                    for _ in range(randint(5, 20)): dot_list.append(Dot(sparkle_pos))
            else:
                if len(dot_list) > 0: dot_list.clear()
            screen.blit(mouse_img[mouse_set], pos)
        pygame.display.update()
        clock.tick(timing)

if __name__=='__main__':
    main()
    pygame.quit();exit()

