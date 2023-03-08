import sys, pygame
pygame.init()

size = width, height = 2000, 1000
speed = [1, 1]
black = 255, 255, 255
acc = 1.5

screen = pygame.display.set_mode(size)

ball = pygame.image.load("maxsmol.JPG")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0] * acc
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1] * acc

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()