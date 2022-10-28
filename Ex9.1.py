# 9.1
# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled
# distance. Add a class initializer that sets the first two of the properties based on parameter values. The current
# speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create
# a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.

# Write a Car class that has the following properties: registration number, maximum speed, current speed and
# travelled distance.
class Car:
    # class initializer that sets the first two of the properties based on parameter values. The current speed and
    # travelled distance of a new car are automatically set to zero.
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = 0
        self.travel_dist = 0


car = Car("ABC-123", 142)
print(f"The new car has:\n"
      f"registration number: {car.reg_num:s},\n"
      f"maximum speed {car.max_speed:d} km/h,\n"
      f"current speed = {car.curr_speed:d} km/h,\n"
      f"travelled distance = {car.travel_dist:d} km.")
