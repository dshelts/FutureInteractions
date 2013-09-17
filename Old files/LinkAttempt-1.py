import Leap
import sys
from graphics import *
from Leap import SwipeGesture






class MyListener(Leap.Listener):
	# NOTE: No __init__ function. Listener object instantiated on inherited Leap.Listener object

	def on_init(self, controller, WINDOW_SIZE):
		self.win = GraphWin("Shapes Lab", WINDOW_SIZE, WINDOW_SIZE) #setting window		self.ballx = ballx
		self.bally = (WINDOW_SIZE/2)
		self.ballx = (WINDOW_SIZE/2)
		self.WINDOW_SIZE = WINDOW_SIZE

		print "Initialized"

	def on_connect(self, controller):
		print "Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);# Enabling swipe
		
	def on_disconnect(self, controller):
		# Called when tracking is stopped
		print "Disconnected"

	def on_exit(self, controller):
		# Called when program stopped
		print "Exited"

	def on_frame(self, controller):

		# Instantiate a Frame object
		# This has information on if any hands are present within the controller's vision
		frame = controller.frame()

		if not frame.hands.empty: # If there is something within the controller's vision

			# Get the first hand
			# NOTE: The Frame object stores the amount of hand objects (extends Interface) in a list
			hand = frame.hands[0]

			# Get fingers on hand
			# NOTE: Each hand object has its own list of finger objects (extends Pointable)
			fingers = hand.fingers

			if not hand.fingers.empty: # Check if any fingers present
				
				# Check the length of the list of fingers
				print len(fingers), "number of fingers"
				
				for gesture in frame.gestures():
					if gesture.type == Leap.gesture.TYPE_SWIPE:
						drawBall(self.bally)
						ballBounce()

	def drawBall(bally):
	
		ball = Point(self.ballx, bally)
		ball = Image(ball, "basketball.gif")
		ball.draw(self.win) 	
		time.sleep(.01)
		ball.undraw()
 
	def ballBounce():
		ballSpeed = 10 #Ball speed


		STEP_SIZE = ballSpeed
		falling = True
		bally = self.bally

		while (falling == True):
			while (bally >= 50): 
				#ballSpeed(win, STEP_SIZE, bally)
				bally = bally - STEP_SIZE
				
				drawBall(self.win, self.ballx, bally)	
			falling = False
	
		while (falling == False):
		
			while (bally <= (self.WINDOW_SIZE/2)):
				#ballSpeed(win, STEP_SIZE, bally)
				bally = bally + STEP_SIZE
							
				drawBall(self.win, self.ballx, bally)	
			falling = True
	
		ballBounce(win, self.ballx, bally)

				
		# if gestures were enabled, should also check if any gestures are present in the frame as well
		# can check gestures with frame.gestures().empty -> returns list of gestures present in Frame object
		if frame.hands.empty:
			
			print "No fingers"

def main():


	WINDOW_SIZE = 400 #size of the display screen
	Win = GraphWin("Shapes Lab", WINDOW_SIZE, WINDOW_SIZE) #setting window
	Win.setCoords(0.0, 0.0, WINDOW_SIZE, WINDOW_SIZE)# setting window coordinates
	##DRAWS WINDOW##


	controller = Leap.Controller()##init leap controller

	listener = MyListener(WINDOW_SIZE)
	
	controller.add_listener(listener)

	print "Press enter to quit..."
	sys.stdin.readline() # Continue to run until you hit a key

	controller.remove_listener(listener) # remove listener when program not running (good practice)

if __name__ == '__main__':
	main()