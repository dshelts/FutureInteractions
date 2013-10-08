#Basic Game

#Imports
import Leap, sys, pygame
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from ClassesFile import *
#=======GLOBALS=======================================================================================
pygame.init()
available_resolutions = pygame.display.list_modes()

#GAME WINDOW
WIDTH = 800
HEIGHT = 400
SIZE = WIDTH, HEIGHT
BG = pygame.image.load("C:\Users\Mejia_000\Documents\GitHub\Surgeon-Sim\jpgs\court.png")
#screen.blit(BG(0,0))
#GAME WINDOW

#GLOBAL IMAGES
image_width = 50
image_height = 50

MYBALL = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/basketball.jpg"
ball_image = pygame.transform.scale(pygame.image.load(MYBALL), (image_width, image_height))

MYOPENPOINTER = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/HandWithoutBall.jpg"
openHand_image = pygame.transform.scale(pygame.image.load(MYOPENPOINTER), (image_width, image_height))

MYCLOSEDPOINTER = "/Users/dshelts9306/Desktop/Surgeon-Sim/jpgs/HandWithBall.jpg"
closedHand_image = pygame.transform.scale(pygame.image.load(MYCLOSEDPOINTER), (image_width, image_height))
#GLOBAL IMAGES

#=======GLOBALS===== END =============================================================================

#-----LEAP CLASS----------------------------------------------------------
class SampleListener(Leap.Listener):
	def on_init(self, controller):
		#General image size
		image_width = 50
		image_height = 50


		#Ball onFrame
		self.ball = Ball(ball_image, (image_width, image_height), (WIDTH//2, 0), SIZE)
		#Hand onFrame
		self.openHand  = Hand(openHand_image, (image_width, image_height), (WIDTH//2, 0), SIZE)
		#Closed Hand onFrame
		self.closedHand  = Hand(closedHand_image, (image_width, image_height), (WIDTH//2, 0), SIZE)
		
		#SCREEN SET
		self.screen = pygame.display.set_mode(SIZE)
		self.last_pos = (0, 0)
		
		print "Initialized"

	def on_connect(self, controller):
		print "Connected"

		# Enable gestures
		# controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		# controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		# controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		# controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		# Note: not dispatched when running in a debugger.
		print "Disconnected"

	def on_exit(self, controller):
		print "Exited"

	def on_frame(self, controller):
		
		frame = controller.frame()

		interactionBox = frame.interaction_box

		finger = frame.fingers.frontmost

		# for finger in frame.fingers:
		self.screen.fill((0, 0, 0))
		normalizedPosition = interactionBox.normalize_point(finger.stabilized_tip_position)

		x, y = normalizedPosition.x, normalizedPosition.y

		scaledX, scaledY = (int((x*WIDTH)), int(HEIGHT-((y*HEIGHT))))
		
		# Draw a line on top of the image on the screen
		#pygame.draw.circle(self.screen, (255, 55, 55), (scaledX, scaledY), 20)#color pointer for finder tip
		#self.screen.blit(self.openHand.image, self.openHand.move(scaledX, scaledY))
		

		

		#pygame.draw.circle(self.screen, (255, 55, 55), (scaledX, scaledY), 20)

		if not self.ball.surrounds((scaledX, scaledY)):
			self.screen.blit(self.ball.image, self.ball.moveLocation("""x, y"""))
			self.screen.blit(self.openHand.image, (scaledX, scaledY))

		if self.ball.surrounds((scaledX, scaledY)):
			self.screen.blit(closedHand_image, (scaledX, scaledY))


			old_x, old_y = self.last_pos

			self.ball.vY = 0
			self.ball.vX = 0

			self.ball.x = scaledX-(self.ball.width//2)
			self.ball.y = scaledY-(self.ball.height//2)

		self.last_pos = (scaledX, scaledY)

		pygame.display.update()
		


	def state_string(self, state):
		if state == Leap.Gesture.STATE_START:
			return "STATE_START"

		if state == Leap.Gesture.STATE_UPDATE:
			return "STATE_UPDATE"

		if state == Leap.Gesture.STATE_STOP:
			return "STATE_STOP"

		if state == Leap.Gesture.STATE_INVALID:
			return "STATE_INVALID"
#-----LEAP CLASS END------------------------------------------------------


#-----MAIN----------------------------------------------------------------
def main():
	# Create a sample listener and controller
	listener = SampleListener()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	sys.stdin.readline()

	# Remove the sample listener when done
	controller.remove_listener(listener)

if __name__ == "__main__":
	main()