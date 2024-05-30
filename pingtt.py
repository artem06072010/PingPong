from pygame import *
from random import *
from time import time as tm 

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('PingPonk')

#задай фон сцены
background = transform.scale(image.load('stol.png'),(700, 500))

#создай 2 спрайта и размести их на сцене
#sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))

font.init()
font1 = font.SysFont('Arial', 70)
font2 = font.SysFont('Arial', 30)

win = font1.render('YOU WIN!', True, (155, 215, 0))


#mixer.music.play()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), ( w , h ))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if key_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 10
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if key_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 10

speed_x = 2
speed_y = 2

boll = GameSprite("boll.png", 350, 250, 30, 30, 2 )
player_l = Player("raketka.png", 5, 200, 60, 90 ,  4)
player_r = Player("raketka.png", 625, 200, 60, 90, 4)




#обработай событие «клик по кнопке "Закрыть окно"»


clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for i in event.get():
        if i.type  == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player_l.update_l()
        player_l.reset()
        player_r.update_r()
        player_r.reset()
        boll.reset()
    clock.tick(FPS)
    display.update()

