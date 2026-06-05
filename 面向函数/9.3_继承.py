class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.make},{self.model},{self.year}"
        return long_name.title()
    def read_odometer(self):
        """打印一个句子，描述汽车的里程"""
        print(f"这辆车已经行驶{self.odometer_reading} miles")
    def update_odometer(self,milage):
        """将里程设置为给定的量，且不可调低"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            pring("不可恢复出厂设置")
    def increment_odometer(self,mils):
        """将里程表增加到给定的量"""
        self.odometer_reading += mils
class ElectricCar(Car):
    """定义子类ElectricCar时，将括号内指定父类的名称"""
    def __init__(self,make,model,year): # 初始化父类的属性
        super().__init__(make,model,year)   
        # 这行代码使python调用Car类的__init__()方法，从而ElectricCar实例包含这个方法定义的所有属性
        self.battery_size = 0
        self.battery = Battery()  #  在ElectricCar类中，创建一个Battery的实例
    """编写子类特有的属性"""
    def describe_battery(self):
        """编写子类特有的方法。打印一条描述电池容量的消息"""
        print(f"电池剩余容量{self.battery_size}")
"""重写父类中的方法：在子类中定义一个与需要重写的父类方法同名的方法"""
"""将实例用作属性"""
class Battery:
    """一次模拟电动车电池的简单尝试"""
    def __init__(self,battery_size = 10):
        self.battery_size = battery_size
        """初始化电池的属性"""
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"电池剩余容量{self.battery_size}")
    def get_range(self):
        if self.battery_size <= 20:
            range = 150
            print(f"还能行驶{range}")
        elif self.battery_size <= 30:
            range = 200
            print(f"还能行驶{range}")
        else:
            print(f"该充电了")
    def update_battery(self,x):
        if x >= 0:
            self.battery_size += x
        else:
            print("停电了")
my_leaf = ElectricCar("yadi","leaf",2026)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
# my_car = Car("wenjie","dian",2026)
# print(my_car.get_descriptive_name())
my_leaf.battery.update_battery(25)
my_leaf.battery.describe_battery()  
# 代码含义：python在实例my_leaf中查找属性battery，并对储存在该属性中的Battery实例调用describe_battery()方法
# my_leaf.battery.get_range()  

my_leaf.battery.get_range()