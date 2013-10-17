#MyPersonalFile.py
#Basic Game

#Imports
import Leap, sys, pygame
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pygame.locals import *
from ClassesFile import *
pygame.init()

#information for later use is class initialization		
MYBALL = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/basketball.jpg"
ball_image = pygame.transform.scale(pygame.image.load(MYBALL), (50, 50))

MYOPENPOINTER = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/handEmpty.jpg"
openHand_image = pygame.transform.scale(pygame.image.load(MYOPENPOINTER), (60, 60))

MYCLOSEDPOINTER = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/handWithBall.jpg"
closedHand_image = pygame.transform.scale(pygame.image.load(MYCLOSEDPOINTER), (60, 60))

OPORTAL = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/Oportal.jpg"
oPortal_image = pygame.transform.scale(pygame.image.load(OPORTAL), (50, 100))

BPORTAL = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/Bportal.jpg"
bPortal_image = pygame.transform.scale(pygame.image.load(BPORTAL), (50, 100))
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
		frame = controller.frame() #info from leap "frame"
		interactionBox = frame.interaction_box #provides the 3d rectangle for interaction space
		# if len(self.frame.fingers) > 1:
		# 	finger1 = self.frame.fingers[0]
		# 	finger2 = self.frame.fingers[1]
		# 	stabilizedPosition1 = finger1.stabilized_tip_position
		# 	normalizedPosition1 = finger1.normalize_point(stabilizedPosition)
		# 	stabilizedPosition2 = finger2.stabilized_tip_position
		# 	normalizedPosition2 = finger2.normalize_point(stabilizedPosition)
		
		# 	self.storage['nofingers'] = False
		# 	self.storage['fingers']   = self.frame.fingers
		# 	self.storage['x1'] = normalizedPosition1.x
		# 	self.storage['y1'] = normalizedPosition1.y
		# 	self.storage['x2'] = normalizedPosition2.x
		# 	self.storage['y2'] = normalizedPosition2.y
			
		if len(frame.fingers) == 1:
			

			self.storage['nofingers'] = False
			self.storage['fingers']   = frame.fingers
			finger = frame.fingers.frontmost
			stabilizedPosition = finger.stabilized_tip_position
			normalizedPosition = interactionBox.normalize_point(stabilizedPosition)#normalizes the position in x,y,z space
		
			self.storage['x1'] = normalizedPosition.x
			self.storage['y1'] = normalizedPosition.y
			self.storage['throw'] = False
			self.storage['velocity'] = finger.tip_velocity
			self.storage['grabBall'] = True


		elif len(frame.fingers) >= 2:

			self.storage['nofingers'] = False
			self.storage['fingers']   = frame.fingers
			finger = frame.fingers.frontmost
			stabilizedPosition = finger.stabilized_tip_position
			normalizedPosition = interactionBox.normalize_point(stabilizedPosition)#normalizes the position in x,y,z space
		
			self.storage['x1'] = normalizedPosition.x
			self.storage['y1'] = normalizedPosition.y
			self.storage['throw'] = True
			self.storage['velocity'] = 0
			self.storage['grabBall'] = False


			#self.storage['x1'] = normalizedPosition.x
			#self.storage['y1'] = normalizedPosition.y
			#self.storage['x2'] = None
			#self.storage['y2'] = None

		else:
			self.storage['nofingers'] = True
			self.storage['fingers']   = []

			# self.storage['point'] = normalizedPosition
			
			#self.storage['x2'] = None
			#self.storage['y2'] = None

		


def runPygame(controller, listener):
	#HEIGHT = 200
	#WIDTH = 400
	#SIZE = WIDTH, HEIGHT
	screen = pygame.display.set_mode(SIZE) #Make the pygame window
	background = pygame.Surface(screen.get_size()) #Get the Surface for the Background
	#playSurface = pygame.Surface(screen.get_size())#Surface for the play to happen
	font = pygame.font.SysFont("Times New Roman", 200)#font for text
	pygame.display.set_caption("Catch")#set title

	screen.fill(BLACK)#fill background apperatnel
	#print"should fill background"
	#playSurface.set_colorkey(BLACK)
	# instantiate classes here
		#Ball onFrame
	Ballobj = Ball(ball_image, (50, 50), (WIDTH//2, HEIGHT-50), SIZE)
		#Hand onFrame
	OpenHand  = Hand(openHand_image, (50, 50), (WIDTH//2, 0), SIZE)
		#Closed Hand onFrame
	ClosedHand  = Hand(closedHand_image, (60, 60), (WIDTH//2, 0), SIZE)
		#Orange Portal
	Oportal = Portal(oPortal_image, (50, 100), (0, HEIGHT-100), 1, SIZE)
		#Blue Portal
	Bportal = Portal(bPortal_image, (50, 100), (WIDTH-50, 0), 0 , SIZE)
	
 

	#COMMAND KEY
	ballImage = Ballobj.image #ball image access
	openHandImage = OpenHand.image
	closedHandImage = ClosedHand.image
	oPortalImage = Oportal.image
	bPortalImage = Bportal.image
	#end COMMAND KEY
	
	#WIDTH = 682
	#HEIGHT = 384

	pos_x = 0
	pos_y = 0
	score = 0
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				controller.remove_listener(listener)
				pygame.quit()
				sys.exit()

		
		if not ('x1' in listener.storage):
			print "waiting for input..."
			continue

		pos_x = listener.storage['x1'] * WIDTH
		pos_y = (1-listener.storage['y1']) * HEIGHT
		
		

		if listener.storage['grabBall'] == True and Ballobj.surrounds((pos_x,pos_y)):
			screen.blit(closedHandImage, (pos_x, pos_y))
			Ballobj.addVelocity(listener.storage['velocity'])
			pygame.display.update()
			print"if 1"
			

		elif listener.storage['throw'] == True and listener.storage['grabBall'] == False:
			screen.blit(ballImage, Ballobj.throw((pos_x, pos_y)))
			pygame.display.update()
			print"elif 1"

		#	print "grab ball"
		
		else:
			print"else"
			
			screen.fill(BLACK)
			
			
			screen.blit(ballImage, Ballobj.bounce())
			screen.blit(openHandImage, (pos_x, pos_y))
			screen.blit(oPortalImage, Oportal.move())
			screen.blit(bPortalImage, Bportal.move())	
				
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
