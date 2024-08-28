import pgzrun
import random

TITLE = "Flappy ball"
WIDTH = 1500
HEIGHT = 700


R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)

rand_color = (R,G,B)
gravity = 500.0
class Flappy_ball:
    def __init__(self,current_x,current_y):
        self.x = current_x
        self.y = current_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x , self.y)  
        screen.draw.filled_circle(pos,self.radius , rand_color)


#creating the object

ball = Flappy_ball(50,100)      

def draw():
    screen.clear()
    ball.draw()

def update(dt):
    uy =  ball.vy
    ball.vy += gravity * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9
    ball.x += ball.vx *dt
    if ball.x > WIDTH-ball.radius or ball.x < ball.radius + 10 :
        
        ball.vx = -ball.vx

pgzrun.go()

