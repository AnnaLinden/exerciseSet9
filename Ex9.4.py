# Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the
# main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car
# is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1",
# "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:

# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This
# is done using the accelerate method. Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each
# car are printed out formatted into a clear table.

import random
from texttable import Texttable


# a Car class that has the following properties: registration number, maximum speed, current speed and
# travelled distance.
class Car:
    # class initializer that sets the first two of the properties based on parameter values. The current speed and
    # travelled distance of a new car are automatically set to zero.
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = 0
        self.travel_dist = 0

    # accerelate method, that receives the change of speed (km/h) as a parameter. If the change is negative,
    # the car reduces speed. The speed of the car is set below maximum and is not less than zero.
    def accelerate(self, change_of_speed):
        self.curr_speed = self.curr_speed + change_of_speed
        if change_of_speed >= 0:
            if self.curr_speed > car.max_speed:
                self.curr_speed = car.max_speed
            # print(f"The car has accelerated {change_of_speed} km/h.")
        if change_of_speed < 0:
            if self.curr_speed < 0:
                self.curr_speed = 0
            # print(f"The car has decelerated {change_of_speed} km/h.")

    # drive method that receives the number of hours as a parameter. The method increases the travelled distance by
    # how much the car has travelled in constant speed in the given time.
    def drive(self, num_of_hours):
        self.travel_dist = self.travel_dist + self.curr_speed * num_of_hours
        # print(f"The travelled distance is now {car.travel_dist} km.\n")


cars = []
num = 0
while num < 10:
    num += 1
    car = Car(f"ABC-{num}", random.randint(100, 200))
    cars.append(car)
    print(f"The car with {car.reg_num} is created, the maximum speed is {car.max_speed} km/h.")

print("The race begins")
hour = 0
while car.travel_dist < 10001:
    hour += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travel_dist > 10000:
            break


table = Texttable()
table.header(["registration number", "maximum speed", "current speed", "travelled distance"])
for car in cars:
    table.add_row([car.reg_num, car.max_speed, car.curr_speed, car.travel_dist])
print(table.draw())
