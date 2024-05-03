from pygame import *
import math
font.init()

window = display.set_mode((800, 500))
pic = image.load('free-icon-tennis-ball-5140646.png')
display.set_icon(pic)
display.set_caption('ping-pong')

mode = 3
background = transform.scale(image.load('tennis_court_background.jpg'), (800,500))
image_player = transform.scale(image.load('free-icon-flying-saucer-11617509.png'), (200, 100))
image_player = transform.rotate(image_player, 90)
image_player_l = transform.rotate(image_player, 180)
image_ball = transform.scale(image.load('free-icon-tennis-ball-5140646.png'), (70, 70))


class GameSprite(sprite.Sprite):
    def __init__(self, image, speed, x, y):
        super().__init__()
        self.image = image
        self.speed = speed
        self.pos_x = x
        self.pos_y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def reset(self):
        window.blit(self.image, self.rect.topleft)
    

class Player(GameSprite):
    def control_move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.pos_y > 0: 
            self.pos_y -= self.speed
        if keys[K_DOWN] and self.pos_y < 300:
            self.pos_y += self.speed
        self.rect.topleft = (self.pos_x, self.pos_y)
    
    def control_move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.pos_y > 0: 
            self.pos_y -= self.speed
        if keys[K_s] and self.pos_y < 300:
            self.pos_y += self.speed
        self.rect.topleft = (self.pos_x, self.pos_y)

class Ball(GameSprite):
    speed_x = 1
    speed_y = 1
    def move(self):
        global mode
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 430:
            self.speed_y *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.speed_x *= -1
        if self.rect.x > 800:
            mode = 1
        if self.rect.x < 0:
            mode = 2

        
label1 = font.Font(None, 20)
label2 = font.Font(None, 50)
label3 = font.Font(None, 30)
n1 = label1.render('ИГРОК 1', True, (255, 255, 255))
n2 = label1.render('ИГРОК 2', True, (255, 255, 255))
lab1 = label2.render('Победил ИГРОК 1', True, (240, 30, 200))
lab2 = label2.render('Победил ИГРОК 2', True, (240, 30, 200))
lab3 = label3.render('Управление ИГРОКОМ 1:', True, (255, 255, 255))
lab4 = label3.render('для перемещения вверх нажмите клавишу "W"', True, (255, 255, 255))
lab5 = label3.render('для перемещения вниз нажмите клавижу "S"', True, (255, 255, 255))
lab6 = label3.render('Управление ИГРОКОМ 2:', True, (255, 255, 255))
lab7 = label3.render('для перемещения вверх нажмите стрелку вверх', True, (255, 255, 255))
lab8 = label3.render('для перемещения вниз нажмите стрелку вниз', True, (255, 255, 255))
lab9 = label3.render('Чтобы НАЧАТЬ ИГРУ нажмите "O"', True, (255, 255, 255))


player1 = Player(image_player, 0.7, 50, 150)
player2 = Player(image_player_l, 0.7, 650, 150)
ball = Ball(image_ball, 1, 365, 215)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if mode == 3: 
        window.blit(lab3, (50, 50))
        window.blit(lab4, (50, 90))
        window.blit(lab5, (50, 130))
        window.blit(lab6, (250, 190))
        window.blit(lab7, (250, 230))
        window.blit(lab8, (250, 270)) 
        window.blit(lab9, (150, 350)) 
        keys = key.get_pressed()
        if keys[K_o]: mode = 0                 

    if mode == 0:
        window.blit(background, (0, 0))
        ball.reset()
        player1.reset()
        player2.reset()
        window.blit(n1, (10, 5))
        window.blit(n2, (700, 5))
        
        ball.move()
        player1.control_move_l()
        player2.control_move()
    if mode == 1:
        window.blit(lab1, (250, 200))
    if mode == 2:
        window.blit(lab2, (250, 200))

    display.update()
