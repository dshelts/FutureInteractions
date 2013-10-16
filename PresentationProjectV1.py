#MyPersonalFile.py
#Basic Game

#Imports
import Leap, sys, pygame
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pygame.locals import *
from ClassesFile import *
pygame.init()

#information for later use is class initialization		
MYBALL = "/Users/zevirc/Desktop/Surgeon-Sim/jpgs/basketball.jpg"
ball_image = pygame.transform.scale(pygame.image.load(MYBALL), (50, 50))

MYOPENPOINTER = "/Users/zevirc/Desktop/Surgeon-Sim/jpgs/handEmpty.jpg"
openHand_image = pygame.transform.scale(pygame.image.load(MYOPENPOINTER), (60, 60))

MYCLOSEDPOINTER = "/Users/zevirc/Desktop/Surgeon-Sim/jpgs/handWithBall.jpg"
closedHand_image = pygame.transform.scale(pygame.image.load(MYCLOSEDPOINTER), (60, 60))

OPORTAL = "/Users/zevirc/Desktop/Surgeon-Sim/jpgs/Oportal.jpg"
oPortal_image = pygame.transform.scale(pygame.image.load(OPORTAL), (100, 50))

BPORTAL = "/Users/zevirc/Desktop/Surgeon-Sim/jpgs/Bportal.jpg"
bPortal_image = pygame.transform.scale(pygame.image.load(BPORTAL), (100, 50))
#end



#Retrieve Highest available screen Res and set window dim to it
available_resolutions = pygame.display.list_modes()
BLACK = (0,0,0)
WIDTH = available_resolutions[0][0]
HEIGHT = available_resolutions[0][1]
WIDTH, HEIGHT = WIDTH//2, HEIGHT//2
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
		self.frame = controller.frame() #info from leap "frame"
		interactionBox = self.frame.interaction_box#provides the 3d rectangle for interaction space

		finger = self.frame.fingers.frontmost

		stabilizedPosition = finger.stabilized_tip_position#stabilizes the finger for smoother movement
		normalizedPosition = interactionBox.normalize_point(stabilizedPosition)#normalizes the position in x,y,z space

		if len(self.frame.fingers) > 0:
			self.storage['nofingers'] = False
			self.storage['fingers']   = self.frame.fingers
		else:
			self.storage['nofingers'] = True
			self.storage['fingers']   = []

		self.storage['x'] = normalizedPosition.x
		self.storage['y'] = normalizedPosition.y

		self.storage['x'] = stabilizedPosition.x
		self.storage['y'] = stabilizedPosition.y

		


def runPygame(controller, listener):
	screen = pygame.display.set_mode(SIZE) #Make the pygame window
	background = pygame.Surface(screen.get_size()) #Get the Surface for the Background
	#playSurface = pygame.Surface(screen.get_size())#Surface for the play to happen
	font = pygame.font.SysFont("Times New Roman", 200)#font for text
	pygame.display.set_caption("Catch")#set title

	background.fill(BLACK)#fill background apperatnel
	
	# instantiate classes here
		#Ball onFrame
	Ballobj = Ball(ball_image, (50, 50), (WIDTH//2, 0), SIZE)
		#Hand onFrame
	OpenHand  = Hand(openHand_image, (50, 50), (WIDTH//2, 0), SIZE)
		#Closed Hand onFrame
	ClosedHand  = Hand(closedHand_image, (60, 60), (WIDTH//2, 0), SIZE)
		#Orange Portal
	Oportal = Portal(oPortal_image, (100, 50), (1, 0), SIZE)
		#Blue Portal
	Bportal = Portal(bPortal_image, (100, 50), (0, -HEIGHT//2), SIZE)
	
 

	#COMMAND KEY
	ballImage = Ballobj.image #ball image access
	openHandImage = OpenHand.image
	closedHandImage = ClosedHand.image
	oPortalImage = Oportal.image
	bPortalImage = Bportal.image
	#end COMMAND KEY
		
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				leapController.remove_listener(LeapListener)
				pygame.quit()
				sys.exit()
		
		if len(listener.storage['fingers']) == 2:
			screen.blit(ballImage, (-HEIGHT, WIDTH//2))
			print "Grab ball"
		print len(listener.storage['fingers'])



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

