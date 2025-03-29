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
font.init()
font = font.Font(None, 70)
win = font.render(
    'YOU WIN!', True, (155, 215, 200)
)
lose = font.render(
    'YOU LOSE!', True, (255, 0, 0)
)
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
        if keys[K_a] and self.rect.x > 5 or keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80 or keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5 or keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80 or keys[K_DOWN] and self.rect.y < win_height - 80:
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


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

hero1 = Player("enemy.png", 0, 0, 3)
hero2 = Enemy("chest.png", 530, 200, 0)
enemy = Enemy("enem.png", 470, 150, 2)
wall1 = Wall(205,255,55,300,70,3,350)
wall2 = Wall(205,255,55,150,70,500,3)
wall3 = Wall(205,255,55,650,70,3,500)
wall4 = Wall(205,255,55,500,170,3,450)

wall5 = Wall(205,255,55,225,370,3,300)
wall6 = Wall(205,255,55,150,370,75,3)
wall7 = Wall(205,255,55,50,70,3,300)
wall8 = Wall(205,255,55,150,0,3,300)
wall9 = Wall(205,255,55,50,370,100,3)






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
        enemy.update()     
        enemy.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall9.draw_wall()
        wall8.draw_wall()
        wall7.draw_wall()
        
        if sprite.collide_rect(hero1, enemy) or sprite.collide_rect(hero1, wall1) or sprite.collide_rect(hero1, wall2)or sprite.collide_rect(hero1, wall3) or sprite.collide_rect(hero1, wall4) or sprite.collide_rect(hero1, wall5) or sprite.collide_rect(hero1, wall6) or sprite.collide_rect(hero1, wall7) or sprite.collide_rect(hero1, wall8) or sprite.collide_rect(hero1, wall9):
            finish = True
            window.blit(lose, (200, 200))
        if sprite.collide_rect(hero1, hero2):
            finish = True
            window.blit(win, (200, 200))
            


    display.update()
    clock.tick(fps)