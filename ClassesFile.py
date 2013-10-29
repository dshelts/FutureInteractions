#classes file 
#Andrew Shelton

#-----BALL CLASS----------------------------------------------------------
class Ball():
	def __init__(self, image, size=(50, 50), pos=(0, 0), bounds=(350, 350)):
		#Initializer method for Ball class
		
		self.image = image #sets the image of the ball
		self.sizeX, self.sizeY = size
		self.x, self.y = pos # puts the ball in the starting position
		self.width, self.height = size # gives the ball its size
		self.xBound, self.yBound = bounds # sets the boundaries for where the ball can go in the screen

		self.vX = 0 #sets the initial velocity of the ball in the horizontal to 0
		self.vY = 0 #sets the inital velocity of the ball in the vertical to 0

		self.state = 0 # 0 = x direction, 0 = y direction

	def bounce(self):
		self.x += self.vX #updates the x coordinate
		self.y += self.vY #updates the y coordinate

		self.checkBounds()#calls the Ball class checkbounds method

		return (self.x, self.y) #returns the new location

	

	def checkBounds(self):
		#The update method for the Ball class
		
		if self.y >= self.yBound:
			self.y = self.yBound-1
			if self.state == 0:
				self.state = 1
			else:
				self.state = 0

			self.vY = -self.vY

		if self.x >= self.xBound:
			self.x = self.xBound
			self.vX = -self.vX
		elif self.x <= 0:
			self.x = 0
			self.vX = -self.vX

		self.vY += .2 # Gravity
		self.vX *= .995 # Friction

	def resetGravity():
		self.vY = 0
		self.vX = 0

	def grabBall(self, pos):
		self.x, self.y = pos
		self.resetGravity()
		self.checkBounds()
		return(self.x, self.y)

	def surrounds(self, pointer_pos):
		#surrounds method checks to see if your finger is holding the ball
		
		x, y = pointer_pos  #position of the pointer

		if x < (self.x + self.width) and x > (self.x) and y < (self.y + self.height) and y > (self.y): 
		#if the pointer is the image box
		#if statement to check to see if your finger and the ball share the same coordinates
		#returns a boolean
			return True

	def updateV(self, velocity):
		newVX = velocity[0]
		newVY = -velocity[1]

		vScalar = float(8)/400

		self.vX = newVX * vScalar
		self.vY = newVY * vScalar

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

	

#-----HAND CLASS END------------------------------------------------------



#-----PORTAL CLASS--------------------------------------------------------


class Portal():
	def __init__(self, image, size, pos, state, bounds):
		'''Key for image corners
		self.y, x = top left  
		self.y, self.sizeX = bot left
		self.sizeY, x = top right
		self.sizeY, self.sizeX = bot right
		'''

		self.image = image
		self.sizeY, sizeX = size#bottom right corner
		self.x, self.y = pos#y,x top left corner
		self.state = state#direction of movement 1^, 0down
		self.width, self.height = bounds#the full size of screen

	def swap(self, ballPos):
		return self.samePlace(ballPos)

	def samePlace(self, pointer_pos):#change
		x, y = pointer_pos
		if (abs(self.x - x) < 50) and (abs(self.y - y) < 50):
			return True
		else:
			return False


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
		#self.directionCheck()
		#print "move self.y, self.sizeY", self.y, self.sizeY
		#print "move self.height", self.height

		if self.y <= 0:
			self.state = 0
			return self.down()
			
		elif (self.y+self.sizeY+20)>= self.height:
			self.state = 1
			return self.up()
			
		else:
			if self.state == 0:
				return self.down()
			if self.state == 1:
				return self.up()

	def down(self):
		self.y += 2
		#print"down x,y", self.x, self.y 
		
		return(self.x, self.y)

	def up(self):
		self.y -= 2
		#print"up, x,y", self.x, self.y 
		
		return(self.x, self.y)
		
		
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

	#def teleport(self, portal2)
		#if self.samePlace():
			#take ball set it to the location of portal2
		
#------ END portal Class----------------------------------------------------------------------------------
	
