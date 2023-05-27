from pygame import *
init()
mixer.init()

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,image_scale1,image_scale2,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(image_scale1, image_scale2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < width - 65:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 65:
            self.rect.y += self.speed
        
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 4:
            self.direction = 'right'
        if self.rect.x >= width - 80:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width =wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

#Сцена
width = 700
height = 500
window = display.set_mode((width,height))
display.set_caption('Maze')

#Уровни
level = 1
lvl = 1

#Спрайты
background = transform.scale(image.load('backGround2.jpg'), (width, height))
player = Player('hero.png',75,75, 5, height - 50, 3.75)
enemy = Enemy('capybara.png',95,100, 115, 125, 4)
goal = GameSprite('watermelons.png',155,125, 555, 15,0)

mixer.music.load('Music.ogg')
mixer.music.play()
money = mixer.Sound("Win.ogg")
kick = mixer.Sound("Boom.ogg")
music2 = mixer.Sound("Capybara.ogg")

font.init()
win = font.Font(None,70).render('You win!', True, (255,215,0))
lose = font.Font(None,70).render('You Lose!', True, (255,215,0))

game = True
finish = False
clock = time.Clock()
FPS = 120
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        enemy.update()
        player.reset()  
        enemy.reset()
        goal.reset()

        if level == 1:
            w1 = Wall(154,205,50,400,160,10,450)
            w2 = Wall(154,205,50,250,10,10,400)
            w3 = Wall(154,205,50,100,160,10,450)
            w4 = Wall(154,205,50,550,10,10,400)
            w5 = Wall(0,0,0,0,0,0,0)
            w6 = Wall(0,0,0,0,0,0,0)
            w7 = Wall(0,0,0,0,0,0,0)
            level = 0
        elif level == 2:
            player = Player('hero.png',75,75, 5, height - 50, 3.15)
            enemy = Enemy('capybara.png',95,100, 115, 125, 3.05)
            w1 = Wall(154,205,50,0,255,420,10)
            w2 = Wall(154,205,50,225,390,10, 125)
            w3 = Wall(154,205,50,100,265,10,140)
            w4 = Wall(154,205,50,550,120,10,420)
            w5 = Wall(154,205,50,0,120,220,10)
            w6 = Wall(154,205,50,310,120,245,10)
            w7 = Wall(0,0,0,0,0,0,0)
            level = 0
            lvl = 2
        elif level == 3:
            player = Player('hero.png',95,95, 5, height - 50, 1.5)
            enemy = Enemy('cyborg.png',75,75, 115, 125, 2.75)
            w1 = Wall(154,205,50,400,160,10,450)
            w2 = Wall(154,205,50,250,10,10,400)
            w3 = Wall(154,205,50,100,160,10,450)
            w4 = Wall(154,205,50,550,10,10,400)
            w5 = Wall(0,0,0,0,0,0,0)
            w6 = Wall(0,0,0,0,0,0,0)
            w7 = Wall(0,0,0,0,0,0,0)
            level = 0
            lvl = 3

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        if sprite.collide_rect(player,goal):
            if lvl != 2 and lvl == 1:
                level = 2
            if lvl != 3 and lvl == 2:
                level = 3
            if lvl != 4 and lvl == 3:
                player = Player('hero.png',115,115, 150, 150, 0)
                enemy = Enemy('cyborg.png',0,0, 0, 0, 0)
                background = transform.scale(image.load('CapybaraLose.jpg'), (width, height))
                level = 4
                window.blit(win, (200,200))
                mixer.music.pause()
                music2.play()
                w1 = Wall(0,0,0,0,0,0,0)
                w2 = Wall(0,0,0,0,0,0,0)
                w3 = Wall(0,0,0,0,0,0,0)
                w4 = Wall(0,0,0,0,0,0,0)
                w5 = Wall(0,0,0,0,0,0,0)
                w5 = Wall(0,0,0,0,0,0,0)
                w6 = Wall(0,0,0,0,0,0,0)
                w7 = Wall(0,0,0,0,0,0,0)
                player = Player('hero.png',0,0, 0, 0, 0)

        if sprite.collide_rect(player, enemy): #sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            window.blit(lose, (200,200))
            finish = True
            mixer.music.pause()
            kick.play()

    display.update()
    clock.tick(FPS)