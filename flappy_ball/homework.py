import pgzrun
import random

TITLE = "Flappy Balls"
WIDTH = 1500
HEIGHT = 700

# Ball 1 attributes
ball1_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ball1_gravity = (random.randint(500,2000))

class FlappyBall1:
    def __init__(self, current_x, current_y):
        self.x = current_x
        self.y = current_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
        self.color = ball1_color

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)

# Ball 2 attributes
ball2_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ball2_gravity = 500.0

class FlappyBall2:
    def __init__(self, current_x, current_y):
        self.x = current_x
        self.y = current_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
        self.color = ball2_color

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)

# Creating the objects
ball1 = FlappyBall1(50, 100)
ball2 = FlappyBall2(WIDTH - 50, 100)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()

def update(dt):
    # Ball 1 update
    uy = ball1.vy
    ball1.vy += ball1_gravity * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt

    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = -ball1.vy * 0.9
    ball1.x += ball1.vx * dt

    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius + 10:
        ball1.vx = -ball1.vx

    # Ball 2 update
    uy = ball2.vy
    ball2.vy += ball2_gravity * dt
    ball2.y += (uy + ball2.vy) * 0.5 * dt

    if ball2.y > HEIGHT - ball2.radius:
        ball2.y = HEIGHT - ball2.radius
        ball2.vy = -ball2.vy * 0.9
    ball2.x += ball2.vx * dt

    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius + 10:
        ball2.vx = -ball2.vx

pgzrun.go()



