class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self. year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
       """返回格式规范的描述性名称"""
       long_name = f"{self.make},{self.model},{self.year}"
       return long_name
    def read_odometer(self):
        """打印一条信息指出汽车行驶里程"""
        print(f"已经行驶{self.odometer_reading}")
    def update_odometer(self,milage):
        """将里程设置为指定的量"""
        if milage >= self.odometer_reading:
            self.odometer_reading += milage
        else:
            print("拒绝回调")
    def increment_odometer(self,miles):
        """增加特定的里程"""
        self.odometer_reading += miles
        
class ElectricCar(Car):
    """在父类Car中添加子类ElectricCar的独特之处"""
    def __init__(self,make,model,year):
        """先初始化父类的属性，在初始化电动汽车的特有的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()

class Battery:
    def __init__(self,battery_size= 40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    def descriptive_battery(self):
        """打印电池的信息"""
        print(f"电池含量{self.battery_size}")
    def get_battery_size(self):
        """打印描述电池剩余里程的信息"""
        if self.battery_size >= 30:
            range = 300
            print(f"剩余里程{range}")
        elif self.battery_size >= 20:
            range = 200
            print(f"剩余里程{range}")
        elif self.battery_size >= 10:
            range = 100
            print(f"剩余里程{range}")
        else:
            print("该充电了")
        