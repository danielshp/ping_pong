from pygame import *
from random import randint
img_back = "mirage.png"
img_hero = "defus.png"
img_ball = "c4.png"
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
player1 =  Player(img_hero, 1, 100, 60, 150, 5)
player2 =  Player(img_hero, 640, 100, 60, 150, 5)
speed_x = 3
speed_y = 3

ball = GameSprite(img_ball, 200 , 200, 30, 80, 5)



clock = time.Clock()
finish = False
FPS = 60
font.init()
points1 = 0
points2 = 0
font = font.Font(None, 35)
lose1 = font.render("Player1 Lose!", True, (180,0,0))
lose2 = font.render("Player2 Lose!", True, (180,0,0))

run = True 

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player1.update_l()
        player2.update_r()
        win1 = font.render("Player1 points: " + str(points1), True, (180,0,0))
        win2 = font.render("Player2 points: " + str(points2), True, (180,0,0))
        if sprite.collide_rect( player1, ball) or sprite.collide_rect( player2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y  > win_height-115 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            points2 = points2 + 1
            game_over = True
            ball.rect.x = 350
            ball.rect.y = 200 
        if ball.rect.x > win_width:
            points1 = points1 + 1
            game_over = True
            ball.rect.x = 350
            ball.rect.y = 200  
        if points1 == 3 :
            window.blit( lose2, (300,200))
        if points2 == 3:
            window.blit( lose1, (300,200))
        window.blit( win1, (0,20))
        window.blit( win2, (500,20))
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
time.delay(50)
        