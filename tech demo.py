import pygame


pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('tech demo')

#object (circle)
circleimg = pygame.image.load('circle.png')
circleX = 400
circleY = 300
deltaCircleX = 0
deltaCircleY = 0


def circle(x,y):
    screen.blit(circleimg,(x,y))



#game loop
running = True
while running:


    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deltaCircleX = -0.1
            elif event.key == pygame.K_RIGHT:
                deltaCircleX = 0.1
            elif event.key == pygame.K_UP:
                deltaCircleY = -0.1
            elif event.key == pygame.K_DOWN:
                deltaCircleY = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                deltaCircleX = 0
                deltaCircleY = 0

    circleX += deltaCircleX
    circleY += deltaCircleY
    circle(circleX,circleY)
    pygame.display.update()