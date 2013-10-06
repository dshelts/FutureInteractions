#classes file 
#Andrew Shelton

#-----BALL CLASS----------------------------------------------------------
class Ball():
	def __init__(self, image, size=(50, 50), pos=(0, 0), bounds=(350, 350)):
		#Initializer method for Ball class
		
		self.image = image #sets the image of the ball

		self.x, self.y = pos #puts the ball in the starting position
		self.width, self.height = size #gives the ball its size
		self.xBound, self.yBound = bounds #sets the boundaries for where the ball can go in the screen

		self.vX = 0 #sets the initial velocity of the ball in the horizontal to 0
		self.vY = 0 #sets the inital velocity of the ball in the vertical to 0

		self.state = 0 # 0 = Falling, 1 = Rising

	def nextLocation(self, x, y):
		#updates the position of the ball
		#if x or y !=0
		#...

		self.x += self.vX #updates the x coordinate
		self.y += self.vY #updates the y coordinate

		self.checkBounds()#calls the Ball class checkbounds method

		return (self.x, self.y) #returns the new location

	def checkBounds(self):
		#The update method for the Ball class
		
		if self.y > self.yBound:
			self.y = self.yBound
			if self.state == 0:
				self.state = 1
			else:
				self.state = 0

			self.vY = -self.vY

		if self.x > self.xBound or self.x < 0:
			self.x = self.xBound

		self.vY += .05 # Gravity
		self.vX *= .9 # Friction

	def surrounds(self, pointer_pos):
		#surrounds method checks to see if your finger is holding the ball
		
		x, y = pointer_pos  #position of the pointer
		
		if x < (self.x + self.width) and x > (self.x) and y < (self.y + self.height) and y > (self.y): #if statement to check to see if your finger and the ball share the same coordinates
		#returns a boolean
			return True
#-----BALL CLASS END------------------------------------------------------


#-----HAND CLASS----------------------------------------------------------
class Hand():
	def __init__(self, image, size=(50, 50), pos=(0, 0), bounds=(350,350)):

		
		self.image = image

		#initializer for the Hand class
		

		#initializer for the Hand class
		

		self.hx, self.hy = pos #sets the initial position of the hand
		self.width, self.height = size #sets the size of the ball
		self.xBound, self.yBound = bounds #sets the boundaries of the ball within the screen



		self.hx = 0 #sets  hand in the horizontal to 0
		self.hy = 0 #sets  hand in the verticle to 0 

	def move(self):
		hx+=hx
		hy+=hy

		#self.update()

		return(self.x, self.y)


	def openToClose(self):#in process of working want to save more images to hand class 
		
		if not self.ball.surrounds((scaledX, scaledY)):
			self.screen.blit(openHand_image, (scaledX, scaledY))
		else:
			self.screen.blit(closedHand_image, (scaledX, scaledY))

	

#-----HAND CLASS END------------------------------------------------------



#-----PORTAL CLASS--------------------------------------------------------


class Portal():
	def __init__(self, image, size=(50, 100), pos=(0, 0), bounds=(350, 350)):
		self.image = image
		self.x, self.y = pos
		self.state = 0
		self.vX = 0
		self.vY = 0

		self.width, self.height = size
		self.xBound, self.yBound = bounds

<<<<<<< HEAD
=======

>>>>>>> 25b259939aa3980bdc69e3dd74a7866a362b9a29

	def directionCheck(self):
		if self.checkOutOfBounds():
			self.state += 1
			if self.state > 3:
				self.state = 0
		
		if state == 0:
			self.vX = 1
			self.vY = 0
		if state == 1:
			self.vX = 0
			self.vY = 1
		if state == 2:
			self.vX = -1
			self.vY = 0
		if state == 3:
			self.vX = 0
			self.vY = -1



	def move(self):
		self.x+= self.vX
		self.y+= self.vY




	def checkOutOfBounds(self):
		
		
		#Checkes if self.x or self.y is out of bounds and puts it in bounds if it is.
		#also sets booleon to true if at one of the edges so it can change direction
		if self.x >= self.xBound:
			self.x = self.xBound
			return True
		elif self.y >= self.yBound:
			self.y = self.yBound
			return True
		elif self.y <= 0:
			self.x = 0
			return True
		elif self.x <= 0:
			self.y = 0
			return True
		




	def samePlace(self, pointer_pos):#change 
		x, y = pointer_pos
		if x < (self.x + self.width) and x > (self.x) and y < (self.y + self.height) and y > (self.y):
			return True

	#def teleport(self, portal2)
		#if self.samePlace():
			#take ball set it to the location of portal2
		
#------ END portal Class----------------------------------------------------------------------------------
	
