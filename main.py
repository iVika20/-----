from pygame import *

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

    def reset(self):
        window.blit(self.image, (self.pos_x, self.pos_y))
    

class Player(GameSprite):
    def control_move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.pos_y > 0: 
            self.pos_y -= self.speed
        if keys[K_DOWN] and self.pos_y < 300:
            self.pos_y += self.speed
    
    def control_move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.pos_y > 0: 
            self.pos_y -= self.speed
        if keys[K_s] and self.pos_y < 300:
            self.pos_y += self.speed
        

class Ball(GameSprite):
    def move(self):
        None


player1 = Player(image_player, 0.7, 50, 150)
player2 = Player(image_player_l, 0.7, 650, 150)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    window.blit(image_ball,  (365, 215))
    player1.reset()
    player2.reset()

    player1.control_move()
    player2.control_move_l()


    display.update()
