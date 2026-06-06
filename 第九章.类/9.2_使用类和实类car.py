# class Car:
#     def __init__(self,make,model,year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 100
#     def get_descriptive_name(self):
#         long_time = f"{self.make} {self.model} {self.year}"
#         return long_time.title()
#     def read_odometer(self):    #  打印一条指出汽车行驶里程的消息
#         print(f"this car has {self.odometer_reading} miles on it")
#     def update_odometer(self,mileage):         # 更新属性的方法
#         if  mileage >= self.odometer_reading:  # 添加逻辑，使得里程不能回调
#             self.odometer_reading = mileage
#         else:
#             print("you can't roll back an odometer")
#     def increment_odometer(self,miles):
#         if miles >= 0:
#             self.odometer_reading += miles
#         else:
#             print("don't back")

# my_new_car = Car("bnw","A6",2026)
# print(my_new_car.get_descriptive_name(),my_new_car.read_odometer())

# """修改属性的值"""
# # 通过方法修改属性的值
# my_new_car = Car("bnw","A6",2026)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(400)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(2)
# my_new_car.read_odometer()




class Hero():
    """做一个hero类"""
    def __init__(self,power,name):
        """初始化属性，体力值和名字"""
        self.power = 100
        self.name = name
    def wall_hero(self):
        if self.power == 0:
            print("you die")
        else:
            print("可以继续游戏")
    def update_eat_hero(self,n):
        self.power += n
        if self.power <= 100:
            print(f"{self.name}当前体力{self.power}")
        else:
            self.power = 100
            print(f"{self.name}当前体力{self.power}")
    def decrease_power(self,m=-10):
        self.power += m
        if self.power >= 0:
            print(f"{self.name}当前体力{self.power}")
        else:
            self.power = 0
            print(f"{self.name}当前体力{self.power}")
David_name = Hero(95,"David")
David_name.wall_hero()
David_name.update_eat_hero(55)
for i in range(5):
    David_name.decrease_power()
David_name.wall_hero()