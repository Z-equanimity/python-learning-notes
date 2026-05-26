"""
1、形参和实参一一对应
"""
# def a(name,age,sex):
#     print(f"我是{name}，今年{age}，性别{sex}")
# a("Zzw",18,"man")

"""
2、关键字参数，可以指定参数传递，不需要一一对应形参的位置
"""
# def a(name,age,sex):
#     print(f"我是{name}，今年{age}，性别{sex}")
# a(age=18, sex="man",name="Zzw")

"""
3、默认参数
"""
# def power(a, exp=2):      # exp=2 是Python 函数的默认参数，当调用函数时，如果没有提供exp参数的值，那么exp就会默认使用2
#                           # 如果调用函数时提供了exp参数的值，那么就会使用提供的值，而不是默认值
#     return a ** exp

# print(power(3))      # 3² = 9
# print(power(3, 3))   # 3³ = 27

"""
4、不定长参数
"""
# 4.1  *args
#  传过去的会被args接受，合并成一个元组（元组取值为索引取值）
# def a(*args):
#     print(args)
# a("Zzw")
# #   传过去的值被kwargs接受，合并为一个字典
# # 4.2  **kwargs
# def a(**kwargs):
#     print(kwargs)
# a(name="Zzw",age=18, sex="man")

