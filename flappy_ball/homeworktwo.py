import pgzrun
import random

TITLE = "Flappy Balls"
WIDTH = 1500
HEIGHT = 700

# Ball 1 attributes
ball1_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ball1_gravity = (random.randint(500, 2000))

class FlappyBall1:
    def __init__(self, current_x, current_y):
        self.x = current_x
        self.y = current_y
        self.horizontal_speed = 200
        self.vertical_speed = 0
        self.radius = 40
        self.color = ball1_color

    def draw(self):
        position = (self.x, self.y)
        screen.draw.filled_circle(position, self.radius, self.color)

# Ball 1 attributes
ball1_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ball1_gravity_acceleration = 500.0

# Create ball 2 using the FlappyBall1 class and update its attributes
ball_two = FlappyBall1(WIDTH - 50, 100)
ball_two.color = ball2_color
ball_two.gravity_acceleration = ball2_gravity_acceleration

def draw():
    screen.clear()
    ball_one.draw()
    ball_two.draw()

def update(dt):
    # Ball 1 update
    previous_vertical_speed = ball_one.vertical_speed
    ball_one.vertical_speed += ball1_gravity * dt
    ball_one.y += (previous_vertical_speed + ball_one.vertical_speed) * 0.5 * dt

    if ball_one.y > HEIGHT - ball_one.radius:
        ball_one.y = HEIGHT - ball_one.radius
        ball_one.vertical_speed = -ball_one.vertical_speed * 0.9
    ball_one.x += ball_one.horizontal_speed * dt

    if ball_one.x > WIDTH - ball_one.radius or ball_one.x < ball_one.radius + 10:
        ball_one.horizontal_speed = -ball_one.horizontal_speed

    # Ball 2 update
    previous_vertical_speed = ball_two.vertical_speed
    ball_two.vertical_speed += ball_two.gravity_acceleration * dt
    ball_two.y += (previous_vertical_speed + ball_two.vertical_speed) * 0.5 * dt

    if ball_two.y > HEIGHT - ball_two.radius:
        ball_two.y = HEIGHT - ball_two.radius
        ball_two.vertical_speed = -ball_two.vertical_speed * 0.9
    ball_two.x += ball_two.horizontal_speed * dt

    if ball_two.x > WIDTH - ball_two.radius or ball_two.x < ball_two.radius + 10:
        ball_two.horizontal_speed = -ball_two.horizontal_speed

pgzrun.go()