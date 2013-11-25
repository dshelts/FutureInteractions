#Pong implementation

import Leap, sys, pygame, os
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pygame.locals import *
from pongClasses import *
pygame.init()

ball_image  = os.path.join("jpgs","pongBall.jpg")
PongBall = pygame.transform.scale(pygame.image.load(ball_image),(50,50))

paddle_image = os.path.join("jpgs","pongPaddle.jpg")
LeftPaddle = pygame.transform.scale(pygame.image.load(paddle_image),(50,100))
RightPaddle = pygame.transform.scale(pygame.image.load(paddle_image),(50,100))

available_resolutions = pygame.display.list_modes()
BLACK = (0,0,0)
WIDTH = available_resolutions[0][0]
HEIGHT = available_resolutions[0][1]
SCREEN_SCALAR = .9
WIDTH, HEIGHT = int(WIDTH*SCREEN_SCALAR), int(HEIGHT*SCREEN_SCALAR)
SIZE = WIDTH, HEIGHT

class LeapListener(Leap.Listener):
	def on_init(self, controller):
		self.storage = {}
		print "Initialized"

	def on_connect(self, controller):
		print "Connected"
		#Gestures
		#controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		#controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
		#controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
		#controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

	def on_disconnect(self, controller):
		print "Disconnected"
	def on_exit(self, controller):
		print "Exited"
	def on_frame(self, controller):
		frame = controller.frame() #info from leap "frame"
		interactionBox = frame.interaction_box #provides the 3d rectangle for interaction space


		if len(frame.fingers) == 1:
			self.storage['nofingers'] = False
			self.storage['fingers']   = frame.fingers
			pointerFinger = frame.fingers.leftmost
			stabilizedPosition = pointerFinger.stabilized_tip_position
			normalizedPosition = interactionBox.normalize_point(stabilizedPosition)#normalizes the position in x,y,z space
		
			#self.storage['xr'] = normalizedPosition.x #right paddle
			self.storage['yr'] = normalizedPosition.y #right paddle
			self.storage['yl'] = HEIGHT/2


		if len(frame.fingers) >= 2:

			self.storage['nofingers'] = False
			self.storage['fingers']   = frame.fingers

			farLeft = frame.fingers.leftmost
			farRight = frame.fingers.rightmost

			stabilizedPositionL = farLeft.stabilized_tip_position
			normalizedPositionL = interactionBox.normalize_point(stabilizedPositionL)#

			stabilizedPositionR = farRight.stabilized_tip_position
			normalizedPositionR = interactionBox.normalize_point(stabilizedPositionR)#


			self.storage['yr'] = normalizedPositionR.y
			self.storage['yl'] = normalizedPositionL.y

		else:
			self.storage['nofingers'] = True
			self.storage['fingers']   = []


def runPygame(controller, listener):
	screen = pygame.display.set_mode(SIZE) #Make the pygame window
	background = pygame.Surface(screen.get_size()) #Get the Surface for the Background
	font = pygame.font.SysFont("Times New Roman", 200)#font for text
	pygame.display.set_caption("Pong")#set title


	PongBallobj = Ball(PongBall, (50,50), SIZE)
	LeftPaddleobj = Paddle(LeftPaddle, (50,100), SIZE)
	RightPaddleobj = Paddle(RightPaddleobj, (50, 100), SIZE)

	outOfBounds = True
	lastPoint = -1#-1 means ball st
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				controller.remove_listener(listener)
				pygame.quit()
				sys.exit()

			if not('yr' in listener.storage):
				print"waiting for input..."
				continue
			left = (1-listener.storage['yl']) * HEIGHT
			right = (1-listener.storage['yr']) * HEIGHT
		
			screen.fill(BLACK)

			if outOfBounds:
				screen.blit(PongBallobj.image, startBall(lastPoint))

			screen.blit(LeftPaddleobj.image, (0, left))
			screen.blit(RightPaddleobj.image, (WIDTH-50, right))
			screen.blit(PongBallobj.image, moveBall())

			pygame.display.update()





def main():
	# Initialize Leap stuff
	controller = Leap.Controller()
	listener = LeapListener()
	controller.add_listener(listener)

	# Run the function for all pygame behavior
	runPygame(controller, listener)

	# Once the game is done, remove the listener
	controller.remove_listener(listener)


if __name__ == '__main__':
	main()


































