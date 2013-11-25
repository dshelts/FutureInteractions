##########################
#Developer: Andrew Shelton

#Notes:
##Right side of the screen is 1st Player
##Left side is 2nd Player

##########################
####Includes##########
import pygame, sys, time, random, os, Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pygame.locals import *
####END INCLUDES######

#GLOBALS#

pygame.init()
size = width, height = 640, 480#screen size
screen = pygame.display.set_mode(size)#access to screen
pygame.display.set_caption('Leap Pong')#Header caption
white = [255, 255, 255]#White hex
black = [0, 0, 0]#Black hex
clock = pygame.time.Clock()#game clock

#END GLOBALS#

########## LEAP LOOP ##########################
class LeapListener(Leap.LeapListener):
	def on_init(self, controller):
		self.storage = {}
		print "Initialized"

	def on_connect(self, controller):
		print "Connected"
		#Gestures here
	def on_disconnect(self, controller):
		print "Disconnected"
	def on_exit(self, controller):
		print "Exited"

	def on_frame(self, controller):
		frame = controller.frame()
		interactionBox = frame.interaction_box

		if len(frame.fingers == 1):
			self.storage['noFingers']=False
			self.storage['onePlayer']=True

			pointerFinger = frame.fingers.leftmost
			stabilizedPosition = pointerFinger.stabilized_tip_position
			normalizedPosition = interactionBox.normalize_point(stabilizedPosition)#normalizes the position in x,y,z space
		
			#self.storage['x1'] = normalizedPosition.x
			self.storage['yRight'] = normalizedPosition.y #player 1 y direction only

		if len(frame.fingers >=2):
			self.storage['noFingers']=False
			self.storage['onePlayer']=False

			#Player one right most finger
			rightMost = frame.fingers.rightmost
			stabilizedPosition = rightMost.stabilized_tip_position
			normalizedPosition = interactionBox.normalize_point(stabilizedPosition)
			self.storage['yRight'] = normalizedPosition.y#player 1 right side
			#end Player one

			#Player two left most finger
			leftMost= frame.fingers.leftmost
			stabilizedPosition = leftMost.stabilized_tip_position
			normalizedPosition = interactionBox.normalize_point(stabilizedPosition)
			self.storage['yLeft'] = normalizedPosition.y#player 2 left side	
		#end Player two

		else:
			self.storage['noFingers'] = True
			self.storage['fingers'] = []
		### on frame ###


############ LEAP END LOOP #####################



################# Sound ########################
# class dummysound():
# 	def play(self):
# 		pass

# try:
# 	phase = pygame.mixer.Sound('cool_phase.ogg')
# except pygame.error:
# 	phase = dummysound()
# 	print 'Error: can\'t load phase.ogg'
# try:
# 	spap = pygame.mixer.Sound('spap.ogg')
# except pygame.error:
# 	spap = dummysound()
# 	print 'Error: can\'t load spap.ogg'
# try:
# 	die = pygame.mixer.Sound('die.ogg')
# except:
# 	die = dummysound()
# 	print 'Error: can\'t load die.ogg'
#######################End Sound#################


# def menu():
# 	global screen, black, white, clock, Menu
# 	titlemenu = Menu([20, 65], wordcolor=[255, 0, 0], selectedcolor=[255, 255, 0], data=['1-Player game', '2-Player game', 'Quit'])
# 	screen.fill(black)
# 	font = pygame.font.Font(None, 32)
# 	screen.blit(font.render('Up-Down over the right side of the Leap for Player 1', True, white, black), [0, 0])
# 	screen.blit(font.render('Up-Down over the left side of the Leap for Player 2. Solo: Up-Down', True, white, black), [0, 32])
# 	pygame.display.flip()
# 	while not titlemenu.selected:
# 		titlemenu.update(screen, pygame.event.poll())
# 		clock.tick(30)
# 		pygame.display.flip()
# 	if titlemenu.selected == '1-Player game':
# 		newGame()
# 	elif titlemenu.selected == '2-Player game':
# 		newGame(True)
# 	else:
# 		pygame.quit()
# 		sys.exit()

#############Pong Game Loop#############
def newGame(twoplayer=False):
	global white, black
	class Paddle():
		def __init__(self, LeapInput):
			global screen
			self.area = [screen.get_width(), screen.get_height()]
			self.pos = [20, self.area[1]/2]
			self.rect = Rect((self.pos), (10, 40))
			self.speed = 5
			self.score = 0
			self.LeapInput = LeapInput

		def update(self):#EDITS HERE TO MOVE LIKE HAND
			global screen, white
			keys = pygame.key.get_pressed()
			if keys[self.upkey]:
				if self.rect.top > 20:
					self.rect.top -= self.speed
			elif keys[self.downkey]:
				if self.rect.bottom < self.area[1]-20:
					self.rect.bottom += self.speed
			pygame.draw.rect(screen, white, self.rect)
			return
	
	class Enemy():
		def __init__(self):
			global screen
			self.area = [screen.get_width(), screen.get_height()]
			self.pos = [self.area[0]-30, self.area[1]/2]
			self.rect = Rect((self.pos), (10, 40))
			self.speed = 5
			self.score = 0
		def update(self, ball):
			global screen, white
			if ball.rect.centery < self.rect.centery:
				if self.rect.top > 20:
					self.rect.centery -= self.speed
			if ball.rect.centery > self.rect.centery:
				if self.rect.bottom < self.area[1]-20:
					self.rect.centery += self.speed
			pygame.draw.rect(screen, white, self.rect)
			return

	class Ball():
		def __init__(self):
			global screen
			self.pos = [screen.get_width()/2, screen.get_height()/2]
			self.center = self.pos
			self.rect = Rect((self.pos), (15, 15))
			self.speed = [random.randint(-2, 2), random.randint(-2, 2)]
			while self.speed[0] == 0:
				self.speed[0] = random.randint(-2, 2)
			while self.speed[1] == 0:
				self.speed[1] = random.randint(-2, 2)
			self.area = [screen.get_width(), screen.get_height()]
			self.paddlecols = 0
		def update(self, paddle, enemy):
			global screen, white, phase, spap, die
			if self.rect.top <= 0 or self.rect.bottom >= self.area[1]:
				phase.play()
				self.speed[1] = -self.speed[1]
				if self.speed[1] < 0:
					self.speed[1] -= 1
				elif self.speed[1] > 0:
					self.speed[1] += 1
			if self.rect.right >= self.area[0]:
				die.play()
				paddle.score += 1
				self.rect.center = self.center
				self.speed[0] = 0
				self.speed[1] = 0
				while self.speed[0] == 0:
					self.speed[0] = random.randint(-2, 2)
				while self.speed[1] == 0:
					self.speed[1] = random.randint(-2, 2)
			elif self.rect.left <= 0:
				die.play()
				enemy.score += 1
				self.rect.center = self.center
				self.speed[0] = 0
				self.speed[1] = 0
				while self.speed[0] == 0:
					self.speed[0] = random.randint(-2, 2)
				while self.speed[1] == 0:
					self.speed[1] = random.randint(-2, 2)
			if self.rect.colliderect(paddle.rect) or self.rect.colliderect(enemy.rect):
				self.paddlecols += 1
				if self.paddlecols > 1:
					if self.rect.colliderect(paddle.rect):
						self.rect.right += 7
					elif self.rect.colliderect(enemy.rect):
						self.rect.left -= 7
				else:
					spap.play()
					self.speed[0] = -self.speed[0]
					if self.speed[0] < 0:
						self.speed[0] -= 1
					elif self.speed[0] > 0:
						self.speed[0] += 1
			else:
				self.paddlecols = 0
			if self.speed[0] > 6:
				self.speed[0] = 6
			elif self.speed[0] < -6:
				self.speed[0] = -6
			self.rect = self.rect.move(self.speed)
			pygame.draw.rect(screen, white, self.rect)
			return
	ball = Ball()
	paddle = Paddle(pygame.K_UP, pygame.K_DOWN)
	paddle_two = Paddle(pygame.K_w, pygame.K_s)
	paddle_two.pos = [screen.get_width()-30, screen.get_height()/2]
	paddle_two.rect.center = paddle_two.pos
	enemy = Enemy()
	gameLoop(paddle, enemy, ball, twoplayer, paddle_two)
	startOver()







