from pygame import *
import os
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
FPS = 50
display.set_caption("Shooter")

clock = time.Clock()

#path1 = os.path.join(os.path.abspath(__file__+"/.."),"media")
# print(path1)
path1 = os.path.join(os.getcwd(),"media")
background = os.path.join(path1, "galaxy.jpg")
# print(background)
background = image.load(background)
background = transform.scale(background, (win_width, win_height))

class GameSprite:
    def __init__(self, x, y, width, height, speed, image):
        self.rect = Rect(x, y, width, height)
        self.speed = speed
        image = transform.scale(image, (width, height))
        self.image = image
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        if key.get_pressed()[K_d] and self.rect.x <= win_width-self.rect.width:
            self.rect.x += self.speed
        if key.get_pressed()[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed 
    def __init__(self, x, y, width, height, speed, image):
        super().__init__(x, y, width, height, speed, image)
        self.bullets = []

    def fire(self):
            b = Bullet(self.rect.centerx, self.rect.y, 10, 50, 2, Bullet_img)
            self.bullets.append(b)


class Bullet(GameSprite):
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y <= -50:
            rocket.bullets.remove(self)

class Enemy(GameSprite):
    def move(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -100
            self.rect.x = randint(0, 650)

enemy_img = os.path.join(path1, "ufo.png")
enemy_img = image.load(enemy_img)
enemies = []
for i in range(5):
    enemy = Enemy(randint(0, 650), randint(-120, -50), 60, 50, randint(1, 5), enemy_img)
    enemies.append(enemy)

player_img = os.path.join(path1, "rocket.png")
player_img = image.load(player_img)
enemy_img = os.path.join(path1, "ufo.png")
enemy_img = image.load(enemy_img)
Bullet_img = os.path.join(path1, "bullet.png")
Bullet_img = image.load(Bullet_img)
rocket = Player(300, 420, 50, 65, 3, player_img)

game = True
while game:

    for ev in event.get():
        if ev.type == QUIT:
            game = False 
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                rocket.fire()

    window.blit(background, (0,0))
    rocket.draw()
    rocket.move()
    for bullet in rocket.bullets:
        bullet.draw()
        bullet.move()

    for ufo in enemies:
        ufo.draw()
        ufo.move()

        
        
    
    display.update()
    clock.tick()
