import Leap, sys, random
from graphics import *
from Leap import SwipeGesture

class MyListener(Leap.Listener):
	#NOTE: No __init__ function, 
	#Listener object instantiated on inherited Leap

	def on_init(self, controller):
		print "Initialized"#Leap read out started

	def on_connect(self, controller):
		print "Connected"# confirmation Leap equipment connected
		
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);#SWIPE enabled

	def on_disconnect(self, controller):
		print "Disconnect" #called when tracking is stopped

	def on_exit(self, controller):
		print "Exited" # called when program is stopped

	def on_frame(self, controller):#Instantiate a Frame object
	#this has the information of hands present with the view of controller
		frame = controller.frame()#variable allowing access to the frames information

		print "frame going"

		if not frame.hands.is_empty: #if there is something in the frames view
			#get the first hand 
			hand = frame.hands[0] 
			# NOTE: The Frame object stores the amount of hand objects (extends Interface) in a list

			#get fingers on hand_1
			fingers = hand.fingers 
			#NOTE each hand object has its own list of finger objects(extends pointable)

			#if no hand present stop the ball animation


			if not hand.fingers.is_empty: #checks if fingers are present
				print len(fingers), "number of fingers"#fingers is a list

			for gesture in frame.gestures(): 
				##for as long as the gesture occurs in Frame
				if gesture.type == Leap.Gesture.TYPE_SWIPE:
					print "SwipeGesture\n"

					swipe = SwipeGesture(gesture)
					print "Swipe id: %d, \n state: %s, \n position: %s, \n direction: %s, \n speed: %f" % (gesture.id, self.state_string(gesture.state), swipe.position, swipe.direction, swipe.speed)
					sys.exit()
							

			if not (frame.hands.is_empty and frame.gestures().is_empty):
				print ""

	def state_string(self, state):
		if state == Leap.Gesture.STATE_START:
			return "STATE_START"
		if state == Leap.Gesture.STATE_UPDATE:
			return "STATE_UPDATE"
		if state == Leap.Gesture.STATE_STOP:
			return "STATE_STOP"
		if state == Leap.Gesture.STATE_INVALID:
			return "STATE_INVALID"

	


class Ball():
	def __init__(self):
		### Variables
		self.ballSpeed = 10
		self.STEP_SIZE = self.ballSpeed
		self.WINDOW_SIZE = 400	
		self.ballx = (self.WINDOW_SIZE/2)
		self.bally = (self.WINDOW_SIZE/2)
		Self.Win = GraphWin("Shapes Lab", self.WINDOW_SIZE, self.WINDOW_SIZE)
		Win.setCoords(0.0, 0.0, self.WINDOW_SIZE, self.WINDOW_SIZE)
	
		drawBall(self.Win, self.ballx, self.bally)
		
		###	
	def drawBall(self, win, ballx, bally):
	
		ball = Point(ballx, bally)
		ball = Image(ball, "basketball.gif")
		ball.draw(win) 	
		time.sleep(.01)
		ball.undraw()
		ballBounce(Win, ballx, bally)
		Win.close()


	def ballBounce(self, win, ballx, bally):
	
		STEP_SIZE = self.ballSpeed
		falling = True
		while (falling == True):
			while (bally >= 60): 
				#ballSpeed(win, STEP_SIZE, bally)
				bally = bally - self.STEP_SIZE
				
				drawBall(win, ballx, bally)	
			falling = False
		while (falling == False):
		
			while (bally <= (self.WINDOW_SIZE/2)):
				#ballSpeed(win, STEP_SIZE, bally)
				bally = bally + self.STEP_SIZE
						
				drawBall(win, ballx, bally)	
			falling = True
	

		ballBounce(win, ballx, bally)


def main():
	listener = MyListener()
	controller = Leap.Controller()
	#sample listener

	controller.add_listener(listener)
	#have listner receive events from the contoller

	print "Press Enter to QUIT..."
	sys.stdin.readline()


	controller.remove_listener(listener)
	#remove listener from controller

if __name__ == '__main__':
	main()






