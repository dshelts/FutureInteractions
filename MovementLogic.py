#I talked with bryan and he said we will most likely need two portal classes to move two images.

#This is what one of the classes will look like:

class Portal():
	def __init__(self, image, size=(50, 100), pos=(0, 0), bounds=(350, 350)):
		self.image = image
		self.x, self.y = pos
		#state is for which of the four directions the image will be moving:
		#the order is as follows: 0 is Right, 1 is Down, 2 is left, 3 is up.
		self.state = 0
		#we will be using the velocity like this. It will allow us to later implament changing velocities etc.
		self.vX = 0
		self.vY = 0

		self.width, self.height = size
		self.xBound, self.yBound = bounds


	def directionCheck(self):
		#make sure image is inbounds, and resets state to 0 if it is at 3
		if self.checkOutOfBounds():
			self.state += 1
			if self.state > 3:
				self.state = 0
		#assignment of movement intervals for each state.
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
		

