from graphics import *
import random

oportalSpeed = 10
STEP_SIZE = oportalSpeed
WINDOW_SIZE = 600


def oportalBall(win, oportalx, oportaly):
	
	oportal = Point(oportalx, oportaly)
	oportal = Image(oportal, "C:\Users\Mejia_000\Documents\GitHub\Surgeon-Sim\jpgs\Oportal.gif")
	oportal.draw(win) 	
	time.sleep(.01)
	oportal.undraw()
"""
def ballSpeed(win, STEP_SIZE, bally):
	STEP_SIZE = ((500-(bally)))*.1
	return STEP_SIZE
	STEP_SIZE = 10
        """
def oportalBounce(win, ballx, bally):
	
	STEP_SIZE = oportalSpeed
	falling = True
	while (falling == True):
		while (oportaly >= 60): 
			#ballSpeed(win, STEP_SIZE, bally)
			oportaly = oportaly - STEP_SIZE
				
			drawoportal(win, ballx, bally)	
		falling = False
	while (falling == False):
		
		while (oportaly <= (WINDOW_SIZE/2)):
			#ballSpeed(win, STEP_SIZE, bally)
			oportaly = oportaly + STEP_SIZE
						
			drawoportal(win, oportalx, oportaly)	
		falling = True
	

	oportalBounce(win, oportalx, oportaly)



def main():
	#STEP_SIZE = eval(input("Enter the refresh rate that you want"))
	
			
	Win = GraphWin("Shapes Lab", WINDOW_SIZE, WINDOW_SIZE)
		
	Win.setCoords(0.0, 0.0, WINDOW_SIZE, WINDOW_SIZE)
	
	
	
	
	oportalx = (WINDOW_SIZE/2)
	oportaly = (WINDOW_SIZE/2)	
	
	drawoportal(Win, oportalx, oportaly)
	
	oportalBounce(Win, oportalx, oportaly)
	
	pause = input("Hit enter to exit")
		
	Win.close()
	
	
main()