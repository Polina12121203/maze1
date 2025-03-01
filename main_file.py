from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Лабіринт')
bg = transform.scale(image.load("background.jpg"), (700, 500))
mixer.init()
mixer.music.load('Monsters-P.I.ogg')
mixer.music.play()
#kick = mixer.Sound("kick.ogg")
#kick.play()
game = True

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
hero1 = GameSprite("enemy.png", 100, 100, 60)
hero2 = GameSprite("chest.png", 200, 200, 60)

while game:
    window.blit(bg, (0, 0))
    hero1.reset()
    hero2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()