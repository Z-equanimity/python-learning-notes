from car import ElectricCar
my_leaf = ElectricCar("wenjie","leaf",2026)
print(my_leaf.get_descriptive_name())
my_leaf.battery.descriptive_battery()
my_leaf.battery.get_battery_size()
"""my_leaf.battery.get_battery_size()
# 分步拆分：
# ① my_leaf → 电车实例
# ② .battery → 取出电车身上绑定的Battery对象
# ③ .get_battery_size() → 调用电池对象自身的方法"""


"""从一个模块中导入多个类"""
from car import Car,ElectricCar
my_mustang = Car("ford","mustang",2026)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar("wenjie","leaf",2026)
print(my_leaf.get_descriptive_name())


"""导入整个模块"""
import car
my_mustang = car.Car("ford","mustang",2026)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar("wenjie","leaf",2026)
print(my_leaf.get_descriptive_name())


