import Leap
import sys
from graphics import *
from Leap import SwipeGesture

ballSpeed = 10
STEP_SIZE = ballSpeed
WINDOW_SIZE = 400




class MyListener(Leap.Listener):
	# NOTE: No __init__ function. Listener object instantiated on inherited Leap.Listener object

	def on_init(self, controller, win, ballx, bally):
		self.win =  win
		self.ballx = ballx
		self.bally = bally

		print "Initialized"

	def on_connect(self, controller):
		print "Connected"

		# can enable gestures here using the enable_gesture function
		 # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		
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
						drawBall(win, ballx, bally)
						ballBounce(win, ballx, bally)

	def drawBall(win, ballx, bally):
	
		ball = Point(ballx, bally)
		ball = Image(ball, "basketball.gif")
		ball.draw(win) 	
		time.sleep(.01)
		ball.undraw()
 
	def ballBounce(win, ballx, bally):
	
		STEP_SIZE = ballSpeed
		falling = True
		while (falling == True):
			while (bally >= 50): 
				#ballSpeed(win, STEP_SIZE, bally)
				bally = bally - STEP_SIZE
				
				drawBall(win, ballx, bally)	
			falling = False
	
		while (falling == False):
		
			while (bally <= (WINDOW_SIZE/2)):
				#ballSpeed(win, STEP_SIZE, bally)
				bally = bally + STEP_SIZE
							
				drawBall(win, ballx, bally)	
			falling = True
	
		ballBounce(win, ballx, bally)

				
		# if gestures were enabled, should also check if any gestures are present in the frame as well
		# can check gestures with frame.gestures().empty -> returns list of gestures present in Frame object
		if frame.hands.empty:
			
			print "No fingers"

def main():

	Win = GraphWin("Shapes Lab", WINDOW_SIZE, WINDOW_SIZE)
		
	Win.setCoords(0.0, 0.0, WINDOW_SIZE, WINDOW_SIZE)
	
	
	ballx = (WINDOW_SIZE/2)
	bally = (WINDOW_SIZE/2)	



	controller = Leap.Controller(Win, ballx, bally)

	listener = MyListener()
	
	controller.add_listener(listener)

	print "Press enter to quit..."
	sys.stdin.readline() # Continue to run until you hit a key

	controller.remove_listener(listener) # remove listener when program not running (good practice)

if __name__ == '__main__':
	main()