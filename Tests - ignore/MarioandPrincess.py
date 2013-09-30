

from graphics import *
import random


#STEP_SIZE = 10
WINDOW_SIZE = 500
smellHoney = False 


#This function takes in the locations of Mario, and Princess peach to eithor make mario normal while he is looking for Princess peach or happy once he can see her. It prints these different emotions onto the game window.
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
		
#This function is the movement function of this program. It controls Marios standard walking directions, his reaction once he sees Peach, and his direction once he sees peach as well as counting and printing his total steps and sending information to reDrawWhereIAm to change his emotion durring his acventure.
def drawConcentricSquares(Win, locationx, locationy, randAntx, randAnty, STEP_SIZE):
		
	#step counter, printed to window
	stepCount = 0
	counter = Text(Point(250, 270), stepCount)
	counter.draw(Win)
	
	#Declares that Mario doesnt know where Peach is yet 
	smellHoney = False
	
	#Marks Peach on the window, yet mario cannot see her yet
	drawCircle(Win, locationx, locationy)
	
	#Declares where Mario is
	hereX = randAntx
	hereY = randAnty
	iAmHere = Point(hereX, hereY) 	
	
	#This sends the location information to be drawn so it flashes marios image as he moves along and makes him more excited as he gets closer.
	reDrawWhereIam(Win, iAmHere, iAmHere, hereX, hereY, locationx, locationy)
	
	#Defining the leng to travel
	LENGTH = WINDOW_SIZE // STEP_SIZE 
	
	#This while loop makes mario keep operating until he has come into sight of Peach
	while (smellHoney == False):
		#This text reminds you that Mario is looking for peach
		looking = Text(Point(250, 290), "I wonder where she is...")
		looking.draw(Win)
		
		#Moves mario to the right side of the window
		while (hereX < (WINDOW_SIZE-10)):
			stepCount = stepCount + 1
			counter.setText(stepCount)		
			iWasHere = iAmHere
			hereX = hereX + STEP_SIZE
			iAmHere = Point(hereX, hereY)
			vector = Line(iWasHere, iAmHere)
			vector.draw(Win)
						
			reDrawWhereIam(Win, iWasHere, iAmHere, hereX, hereY, locationx, locationy)
				
			time.sleep(0.0001)
		#Moves Mario to the bottom of the window
		while (hereY > (WINDOW_SIZE-490)):
			stepCount = stepCount + 1
			counter.setText(stepCount)		
			iWasHere = iAmHere
			hereY = hereY - STEP_SIZE
			iAmHere = Point(hereX, hereY)
			vector = Line(iWasHere, iAmHere)
			vector.draw(Win)
							
			reDrawWhereIam(Win, iWasHere, iAmHere, hereX, hereY, locationx, locationy)
					
			time.sleep(0.0001)
		#Moves Mario to the far left corner (30,30) of the wondow		
		while (hereX > (10)):
			stepCount = stepCount + 1
			counter.setText(stepCount)		
			iWasHere = iAmHere
			hereX = hereX - STEP_SIZE
			iAmHere = Point(hereX, hereY)
			vector = Line(iWasHere, iAmHere)
			vector.draw(Win)
								
			reDrawWhereIam(Win, iWasHere, iAmHere, hereX, hereY, locationx, locationy)
					
			time.sleep(0.0001)		
		#This for loop begins a series of loops that move mario around in concentric squares
		for h in range(50):
		
			#This moves mario around 3 times before changing the distance that he travels each time 
			for i in range(LENGTH * 4 - 5):
				
				iWasHere = iAmHere
				
				#Tells Mario to check if he is within sight range of Peach, if he is he leaves this walking loop and goes on to the close range walking loop
				if ((hereX-locationx)**2 + (hereY-locationy)**2 <= (30)**2):
					smellHoney = True
					break
				
				#The following four statments tell him to go one of the four cumpass directions
				if (i // (LENGTH - 1) == 0):
					stepCount = stepCount + 1
					counter.setText(stepCount)
					hereY = (hereY + STEP_SIZE)
					print ("NORTH")
				elif (i // (LENGTH - 1) == 1):
					stepCount = stepCount + 1
					counter.setText(stepCount)					
					hereX = hereX + STEP_SIZE+1
					print ("EAST")
				elif (i // (LENGTH - 1) == 2):
					stepCount = stepCount + 1
					counter.setText(stepCount)					
					hereY = (hereY - STEP_SIZE)
					print ("SOUTH")
				else:
					stepCount = stepCount + 1
					counter.setText(stepCount)					
					hereX = hereX - (STEP_SIZE)
					print ("WEST")
					
				#This coding is seen several times and is used to update and flash his image in the location that he visited.
				iAmHere = Point(hereX, hereY)
				vector = Line(iWasHere, iAmHere)
				vector.draw(Win)
				
				#This specific bit flashes his location, changing his emotion when he can see the princess
				reDrawWhereIam(Win, iWasHere, iAmHere, hereX, hereY, locationx, locationy)

				time.sleep(0.0001)
				
			LENGTH = LENGTH - 2
			
			#Once he can see the princes (still called Smellhoney because aint nobody got time fo dat) he breaks from the first movement loop
			if (smellHoney == True):
				break
		
	
		if (smellHoney == True):
		
				
			break
	#Declaring that he is in sight of peach
	print("I see my princess")
	
	#Let the short range walk begin. Same idea as last time, just now he has a target
	while ((hereX-locationx)**2 + (hereY-locationy)**2 > (4)**2):
		iWasHere = iAmHere
		
		#The below statments direct him to line up with the princesses cordinates one axis at a time:
		if (hereX < locationx):
			stepCount = stepCount + 1
			counter.setText(stepCount)
			hereX = (hereX + (STEP_SIZE+.5))			
			
		elif (hereY < locationy):
			stepCount = stepCount + 1
			counter.setText(stepCount)
			hereY = (hereY + STEP_SIZE)
		elif (hereX > locationx):
			stepCount = stepCount + 1
			counter.setText(stepCount)
			hereX = (hereX - STEP_SIZE)			
			
		elif (hereY > locationy):
			stepCount = stepCount + 1
			counter.setText(stepCount)
			hereY = (hereY - STEP_SIZE)
		iAmHere = Point(hereX, hereY)
		vector = Line(iWasHere, iAmHere)
		vector.draw(Win)
		
		reDrawWhereIam(Win, iWasHere, iAmHere, hereX, hereY, locationx, locationy)
		
		time.sleep(0.0001)
		
	#Once Mario has reached the princess their images combine and it shows them happily together (He is a little short for her).
	ant = Point(hereX, hereY)
	ant = Image(ant, "parioprincess.gif")
	ant.draw(Win) 	
	print("I found her! <3 ")
	#Just printing out how many steps it took for him to find her
	print("It only took mario", stepCount, "steps to find the princess")
	time.sleep(3.5)
	#Great succes!!! XD
	success = Point(250, 250)
	success = Image(success, "codeworking-jpg.gif")
	success.draw(Win) 	
	#Time to print out the total steps take on the GUI window
	totalSteps = Text(Point(140, 60), "It took a total of")
	totalSteps.setFill("green")
	totalSteps.draw(Win)
	totalSteps = Text(Point(200, 60), stepCount)
	totalSteps.setFill("green")
	totalSteps.draw(Win)
	totalSteps = Text(Point(310, 60), "steps for Mario to find the princess!")
	totalSteps.setFill("green")
	totalSteps.draw(Win)
	
#This function originally drew the honey circle. Now it draws the beautiful Princess peach. It takes the x and y cordinates from the random honey function so she appears in random places.
def drawCircle(win, locationx, locationy):
	
	honey = Point(locationx, locationy)
	honey = Image(honey, "princess1.gif")
	honey.draw(win) 	
	
#This bit here is a function that you can use to have the Mario start at random locations as well. I did an average of 10 with both Mario and Peach starting at random locations and got 523.1 steps for them to meet up. I have reason to believe this is not a bad number in comparison to the rest of the class
"""	
def randomAnt():
	
	randAntx = 0
	randAnty = 0
	randAntx = random.randrange(0, WINDOW_SIZE, STEP_SIZE)
	randAnty = random.randrange(0, WINDOW_SIZE, STEP_SIZE)
	print("ant x and y:", randAntx, randAnty)
	return randAntx, randAnty	
"""	

#This function generates a random location for Peach within the window and incramented by Marios step size.
def randomHoney(STEP_SIZE):
	
	locationx = 0
	locationy = 0
	
	locationx = random.randrange(0, WINDOW_SIZE, STEP_SIZE)
	locationy = random.randrange(0, WINDOW_SIZE, STEP_SIZE)
	print("Location x and y:", locationx, locationy)
	
	return locationx, locationy
#alas the main function. This can ask for user input for step size, window size and many other things, but my program did not run consistently with those inputs, so i limmited its variability so it can work 100% of the time.
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
	
	smellHoney = False
	#Setting the window size from the graphix library	
	Win = GraphWin("Shapes Lab", 500, 500)

	Win.setCoords(0.0, 0.0, WINDOW_SIZE, WINDOW_SIZE)
	
	#establishing some variables. If you are going to use the random ant variable you can comment these out
	randAntx = 250
	randAnty = 250
	locationx = 0
	locationy = 0
	locationx, locationy = randomHoney(STEP_SIZE)
	
	#Calls the Princess Peach function to draw her
	drawCircle(Win, locationx, locationy)
	
	#calls the Mario function to make him start his adventure
	drawConcentricSquares(Win, locationx, locationy, randAntx, randAnty, STEP_SIZE)
	
	#A prompt to finish and close the window
	pause = input("Hit enter to exit")
	
	Win.close()

	"""Thank you - and I hope you enjoyed"""
main()