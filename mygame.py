import pygame
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
g =350

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
            is_green = not is_green

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -=3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if pressed[pygame.K_w]: b -= 3
    if pressed[pygame.K_s]: b += 3
    if pressed[pygame.K_a]: a -= 3
    if pressed[pygame.K_d]: a += 3

    screen.fill(hotpink)
    if is_green: color2 = (255, 255, 0)
    else: color2 = (0, 255, 0)
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    if ((t == x and g == y)):
        color3 = hotpink
    elif ((t == a and g == b)):
        color3 = hotpink

    screen.fill(hotpink)
    pygame.draw.rect(screen, color3, pygame.Rect(t, g, 60, 60))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.draw.rect(screen, color2, pygame.Rect(a, b, 60, 60))




    pygame.display.flip()
    clock.tick(60)
