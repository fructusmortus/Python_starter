class Vehicle:
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage

subaru = Vehicle(260, 300000)
print(subaru.max_speed, subaru.mileage)