# Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method
# increases the travelled distance by how much the car has travelled in constant speed in the given time. Example:
# The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases
# the travelled distance to 2090 km.

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

    # accelerate method, that receives the change of speed (km/h) as a parameter. If the change is negative,
    # the car reduces speed. The speed of the car is set below maximum and is not less than zero.
    def accelerate(self, change_of_speed):
        self.curr_speed = self.curr_speed+change_of_speed
        if change_of_speed >= 0:
            if self.curr_speed > car.max_speed:
                self.curr_speed = car.max_speed
            print(f"The car has accelerated {change_of_speed} km/h.")
        if change_of_speed < 0:
            if self.curr_speed < 0:
                self.curr_speed = 0
            print(f"The car has decelerated {change_of_speed} km/h.")

    # drive method that receives the number of hours as a parameter. The method increases the travelled distance by
    # how much the car has travelled in constant speed in the given time.
    def drive(self, num_of_hours):
        self.travel_dist = self.travel_dist + self.curr_speed*num_of_hours
        print(f"The travelled distance is now {car.travel_dist} km.\n")


car = Car("ABC-123", 142)
acceleration1 = car.accelerate(30)
print(f"The speed of the car is {car.curr_speed} km/h.\n")
print("The car drives one hour with the current speed.")
car.drive(1)
print("-------------------------------------------------------------------------------------------------------------\n")
acceleration2 = car.accelerate(30)
print(f"The speed of the car is {car.curr_speed} km/h.\n")
print("The car drives 1,5 hour with the current speed.")
car.drive(1.5)
print("-------------------------------------------------------------------------------------------------------------\n")