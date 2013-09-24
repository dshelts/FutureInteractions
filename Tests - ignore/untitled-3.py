from graphics import *
import random

ballSpeed = 10
STEP_SIZE = ballSpeed
WINDOW_SIZE = 800


def drawBall(win, ballx, bally):
	
	ball = Point(ballx, bally)
	ball = Image(ball, "basketball.gif")
	ball.draw(win) 	
	time.sleep(.01)
	ball.undraw()
"""
def ballSpeed(win, STEP_SIZE, bally):
	STEP_SIZE = ((500-(bally)))*.1
	return STEP_SIZE
	STEP_SIZE = 10
        """
def ballBounce(win, ballx, bally):
	
	STEP_SIZE = ballSpeed
	falling = True
	while (falling == True):
		while (bally >= 60): 
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
	#while (bally >= 65):
		#bally = bally - STEP_SIZE
		
		#drawBall(win, ballx, bally)
	
	#while (bally <= 250):
		#bally = bally + STEP_SIZE
				
		#drawBall(win, ballx, bally)		
		

def main():
	#STEP_SIZE = eval(input("Enter the refresh rate that you want"))
	
			
	Win = GraphWin("Shapes Lab", WINDOW_SIZE, WINDOW_SIZE)
		
	Win.setCoords(0.0, 0.0, WINDOW_SIZE, WINDOW_SIZE)
	
	
	
	
	ballx = (WINDOW_SIZE/2)
	bally = (WINDOW_SIZE/2)	
	
	drawBall(Win, ballx, bally)
	
	ballBounce(Win, ballx, bally)
	
	pause = input("Hit enter to exit")
		
	Win.close()
	
	
main()