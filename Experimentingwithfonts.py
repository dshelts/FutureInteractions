import os, sys, pygame
pygame.init()

def main():
    size = width, height = 500, 500
    
    black = 0, 0, 0
    red = 250, 0, 0
    screen = pygame.display.set_mode(size)
    
    font = pygame.font.Font('font.ttf', 42)
    
    stuff = "hello world"
    
    
    msgobject = font.render(stuff, False, red)
    
    msgrect = msgobject.get_rect()
    
    
    screen.blit(msgobject, msgrect)
    
    pygame.display.update()
    
main()