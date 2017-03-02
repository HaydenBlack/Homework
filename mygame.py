import pygame
import random
color4 = (0, 0, 0)
#Naming the Variables
xcoordinant = random.randrange(0, 700)
ycoordinant = random.randrange(0, 700)
rangeY = (0, 700)
hotpink = (255,20,147)
color3 = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((700, 700))
done = False
is_blue = True
is_green = True
x = 30
y = 30
a = 30
b = 30
t = 350
g = 350

clock = pygame.time.Clock()
#Changing the color
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
            is_green = not is_green
#Controls
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 1
    if pressed[pygame.K_DOWN]: y += 1
    if pressed[pygame.K_LEFT]: x -= 1
    if pressed[pygame.K_RIGHT]: x += 1

    if pressed[pygame.K_w]: b -= 1
    if pressed[pygame.K_s]: b += 1
    if pressed[pygame.K_a]: a -= 1
    if pressed[pygame.K_d]: a += 1
#Colors
    screen.fill(hotpink)
    if is_green: color2 = (255, 255, 0)
    else: color2 = (0, 255, 0)
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    if ((t == x and g == y)):
        for i in range(1):
            pygame.draw.rect(screen,(0, 0, 0), pygame.Rect(xcoordinant, ycoordinant, 60, 60))
        color3 = hotpink
        #random.randint(rangeX and rangeY)
    elif ((t == a and g == b)):
        for j in range(1):
            pygame.draw.rect(screen,(0, 0, 0), pygame.Rect(xcoordinant, ycoordinant, 60, 60))
        color3 = hotpink
        #random.randint(rangeX and rangeY)
#The rectangles traits
    screen.fill(hotpink)
    pygame.draw.rect(screen, color3, pygame.Rect(t, g, 60, 60))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.draw.rect(screen, color2, pygame.Rect(a, b, 60, 60))
    if ((t == x and g == y)):
        for k in range(1):
            pygame.draw.rect(screen, color4, pygame.Rect(xcoordinant, ycoordinant, 60, 60))
            color4 = (0, 0, 0)

    elif ((t == a and g == b)):
        for i in range(1):
            pygame.draw.rect(screen, color4, pygame.Rect(xcoordinant, ycoordinant, 60, 60))
        color4 = (0, 0, 0)



    pygame.display.flip()
    clock.tick(60)
