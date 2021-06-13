from pygame import *
from random import randint
img_back = "mirage.png"
img_hero = "defus.png"
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
mixer.init()
mixer.music.load('mainmenu.mp3')
mixer.music.play()

font.init()
font1 = font.SysFont("Arial", 80)
font2 = font.SysFont("Arial", 36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 170:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 170:
            self.rect.y += self.speed
player1 =  Player(img_hero, 1, 100, 60, 200, 5)
player2 =  Player(img_hero, 640, 100, 60, 200, 5)
class Enemy(GameSprite):
    pass



finish = False

run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.blit(background,(0,0))
        player1.update_l()
        player2.update_r()
        player1.reset()
        player2.reset()
        display.update()