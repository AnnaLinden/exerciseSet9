# Extend the program by adding an accelerate method into the new class. The method should receive the change of speed
# (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the
# speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50
# km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change
# on the speed and then print out the final speed. The travelled distance does not have to be updated yet.

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
        self.curr_speed = self.curr_speed + change_of_speed
        if change_of_speed >= 0:
            if self.curr_speed > car.max_speed:
                self.curr_speed = car.max_speed
            print(f"The car has accelerated {change_of_speed} km/h.")
        if change_of_speed < 0:
            if self.curr_speed < 0:
                self.curr_speed = 0
            print(f"The car has decelerated {change_of_speed} km/h.")


car = Car("ABC-123", 142)
acceleration1 = car.accelerate(30)
print(f"The speed of the car is {car.curr_speed} km/h.\n")
car.accelerate(70)
print(f"The speed of the car is {car.curr_speed} km/h.\n")
car.accelerate(50)
print(f"The speed of the car is {car.curr_speed} km/h.\n")
car.accelerate(-200)
print(f"The speed of the car is {car.curr_speed} km/h.\n")
