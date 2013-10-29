
import sys, pygame, os
pygame.init()
 
size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = os.path.join("jpgs", "basketball.jpg")
ball_image = pygame.transform.scale(pygame.image.load(ball), (50, 50))
ballrect = ball_image.get_rect()

while 1:
                        for event in pygame.event.get():
                                                if event.type == pygame.QUIT: sys.exit()

                        ballrect = ballrect.move(speed)
                        if ballrect.left < 0 or ballrect.right > width:
                                                speed[0] = -speed[0]
                        if ballrect.top < 0 or ballrect.bottom > height:
                                                speed[1] = -speed[1]

screen.fill(black)
screen.blit(ball, ballrect)
pygame.display.flip()
