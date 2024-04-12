from pygame import *
import math
import font

window = display.set_mode((800, 500))
pic = image.load('free-icon-tennis-ball-5140646.png')
display.set_icon(pic)
display.set_caption('ping-pong')

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
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 430:
            self.speed_y *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.speed_x *= -1
        
label1 = font.Font(None, 15)
label2 = font.Font(None, 50)
n1 = label1.render('ИГРОК №1', True, (255, 255, 255))
n2 = label1.render('ИГРОК №2', True, (255, 255, 255))

player1 = Player(image_player, 0.7, 50, 150)
player2 = Player(image_player_l, 0.7, 650, 150)
ball = Ball(image_ball, 1, 365, 215)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    ball.reset()
    player1.reset()
    player2.reset()
    window.blit(n1, (10, 5))
    window.blit(n2, (700, 5))

    ball.move()
    player1.control_move()
    player2.control_move_l()


    display.update()
