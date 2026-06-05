from car import Car
my_new_car = Car("wenjie","dianche",2026)
print(my_new_car.get_descriptive_name().title())
my_new_car.read_odometer()
my_new_car.increment_odometer(55)
my_new_car.read_odometer()