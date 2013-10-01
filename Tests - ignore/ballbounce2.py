from graphics import *
import random


#STEP_SIZE = 10
WINDOW_SIZE = 500

def reDrawWhereIam(Win, old, new, hereX, hereY, locationx, locationy):
	
	if ((hereX-locationx)**2 + (hereY-locationy)**2 < (30**2)):
	
		ant = Point(hereX, hereY)
		ant = Image(ant, "mariohappy.gif")
		ant.draw(Win) 
		time.sleep(.5)
		ant.undraw()
		
	else:
		ant = Point(hereX, hereY)
		ant = Image(ant, "mario.gif")
		ant.draw(Win) 
		time.sleep(.001)
		ant.undraw()		

def drawConcentricSquares(Win, locationx, locationy, STEP_SIZE, hereX, hereY):
	while (hereY >= (WINDOW_SIZE-240)):
		stepCount = stepCount + 1
		counter.setText(stepCount)		
		iWasHere = iAmHere
		hereY = hereY - STEP_SIZE
		iAmHere = Point(hereX, hereY)
		vector = Line(iWasHere, iAmHere)
		vector.draw(Win)
							
		reDrawWhereIam(Win, iWasHere, iAmHere, hereX, hereY, locationx, locationy)
					
		time.sleep(0.0001)


def drawCircle(win, locationx, locationy):
	
	honey = Point(locationx, locationy)
	honey = Image(honey, "basketball.gif")
	honey.draw(win) 	

def main():
	STEP_SIZE = eval(input("Enter the desired step size for Mario (Must be 10 or less):"))
	#WINDOW_SIZE = eval(input("Enter the desired window size for the adventure:")) 
	
	#Here i have a little trap to keep the user from entering an incorrect Step size
	while (STEP_SIZE != -1):
		
		if (0< STEP_SIZE <= 10):
			print("You chose,", STEP_SIZE, "as Marios step size")
			break
		else:
			#Foolproofing the system so if the user inputs 0, or 15 the program will prompt them for a correct input.
			print ("HUH? Mario can't take", STEP_SIZE,"steps")
			STEP_SIZE = eval(input("Enter the desired step size for Mario (Must be 10 or less):"))
			
	Win = GraphWin("Shapes Lab", 500, 500)
		
	Win.setCoords(0.0, 0.0, WINDOW_SIZE, WINDOW_SIZE)
	
	hereX = randAntx
	hereY = randAnty
	iAmHere = Point(hereX, hereY) 	
	
	
	locationx = 250
	locationy = 250	
	
	drawCircle(Win, locationx, locationy)
	
	#calls the Mario function to make him start his adventure
	drawConcentricSquares(Win, locationx, locationy, STEP_SIZE, hereX, hereY)
	
	pause = input("Hit enter to exit")
		
	Win.close()
	
	
main()