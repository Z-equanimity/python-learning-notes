class Car:
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100
    def get_descriptive_name(self):
        long_time = f"{self.make} {self.model} {self.year}"
        return long_time.title()
    def read_odometer(self):    #  打印一条指出汽车行驶里程的消息
        print(f"this car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):         # 更新属性的方法
        if  mileage >= self.odometer_reading:  # 添加逻辑，使得里程不能回调
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")
    def increment_odometer(self,miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("don't back")
# my_new_car = Car("bnw","A6",2026)
# print(my_new_car.get_descriptive_name(),my_new_car.read_odometer())

"""修改属性的值"""
# 通过方法修改属性的值
my_new_car = Car("bnw","A6",2026)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(400)
my_new_car.read_odometer()
my_new_car.increment_odometer(2)
my_new_car.read_odometer()