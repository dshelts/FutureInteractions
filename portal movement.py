import sys, pygame
pygame.init()

def main():

	size = width, height = 500, 500
	speed = [1, 1]
	black = 0,0,0

	screen = pygame.display.set_mode(size)
	
	oportal = pygame.image.load("C:\Users\Mejia_000\Documents\GitHub\Surgeon-Sim\jpgs\Oportal.jpg")
	oportalrect = oportal.get_rect()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			
			oportalrect = oportalrect.move(speed)
			if oportalrect.left <0 or oportalrect.right > width :
				speed[0] = -speed[0]
				if oportalrect.top < 0 or oportalrect.bottom > height:
					speed[1] = -speed[1]

					screen.fill(black)
					screen.blit(oportal, oportalrect)
					pygame.display.flip()
	print "Press Enter to quit..."
	sys.stdin.readline()	
	
if __name__ == "__main__":	
	main()