from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лабіринт')
bg = transform.scale(image.load("background.jpg"), (700, 500))
mixer.init()
mixer.music.load('Monsters-P.I.ogg')
mixer.music.play()
#kick = mixer.Sound("kick.ogg")
#kick.play()
game = True
clock = time.Clock()
fps = 60

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
            

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width-80:
            self.direction = "left"
        if self.direction== "right":
            self.rect.x += self.speed
        if self.direction== "left":
            self.rect.x -= self.speed
hero1 = Player("enemy.png", 100, 100, 10)
hero2 = Enemy("chest.png", 200, 200, 5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg, (0, 0))
        hero1.update()   
        hero2.update()     
        hero1.reset()
        hero2.reset()

        
    display.update()
    clock.tick(fps)