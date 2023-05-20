from pygame import *
font.init 
window=display.set_mode((700,500))
display.set_caption('Ping-pong')
background=transform.scale(image.load('images.jpg'),(700,500))
font1=font.Font(None,45)
font2=font.Font(None,45)
win=font1.render('YOU LOSE',True,255,215,0)
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
ball=GameSprite('png-clipart-football-football.png',10,10,20,100,5)
rocket1=Player('d7300adb552de6eL.png',10,10,20,100,5)
rocket2=Player('d7300adb552de6eLR.png',100,100,20,100,5)

game=True
finish = False
while game:
    if finish != True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if ball.rect.x<0:
            window.blit(win,(200,200))
            finish=True
        if ball.rect.y<0 or ball.rect.y >500:
            speed_y  *= -1
        if sprite.collide_rect(rocket1,ball):
            speed_x *=-1
        if sprite.collide_rect(rocket2,ball):
            speed_x *=-1  
        window.blit(background,(0,0))
        rocket1.update_l()
        rocket2.update_r()
        rocket1.reset()
        rocket2.reset()
        ball.reset()
        
    for e in event.get():
        if e.type==QUIT:
            game=False
           
                
                    
    display.update()
    time.delay(10)
    
