from pygame import *
from random import randint
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
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    pass

win_width = 700
win_height = 500
display.set_caption("Ping_Pong")
window = display.set_mode((win_width, win_height))


finish = False

run = True 
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        display.update()
