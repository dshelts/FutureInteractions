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

	def move(self):
		#updates the position of the ball
		self.x += self.vX #updates the x coordinate
		self.y += self.vY #updates the y coordinate

		self.update()#calls the Ball class update method

		return (self.x, self.y) #returns the new location

	def update(self):
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
		#initializer for the Hand class
		
		self.hx, self.hy = pos
		self.width, self.height = size
		self.xBound, self.yBound = bounds

		self.vhx = 0
		self.vhy = 0

	def move(self):
		hx+=vhx
		hy+=vhy

		#self.update()

		return(self.x, self.y)

	#def update(self, vhx, vhy):
	
		
	def surrounds(self, pointer_pos):
		x, y = pointer_pos
		if x < (self.hx + self.width) and x > (self.hx) and y < (self.hy + self.height) and y > (self.hy):
			return True

#-----HAND CLASS END------------------------------------------------------