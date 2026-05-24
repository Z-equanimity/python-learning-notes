
# 函数的定义及调用
# def greet(任意参数):
#     """向指定用户打招呼"""
#     print(f"你好，{任意参数}！")
# greet("任意内容")  # 调用函数，，任意内容处的值会被传递给函数的任意参数，输出"你好，任意内容！"


"""
返回值问题
"""
# def a():
#     # return 关键字   可以返回函数的结果
#     return 5+6
# result = a()
# print(result)

# def add(a,b):        # a,b 是函数的参数，参数是函数定义时小括号内的变量，用于接收调用函数时传递的值
#     return a + b

# result = add(3,5)    # 3,5 是函数的实参，实参是函数调用时小括号内的值，会被传递给函数的参数
# print(result)  # 8

# # 默认参数
# def power(a, exp=2):      # exp=2 是Python 函数的默认参数，当调用函数时，如果没有提供exp参数的值，那么exp就会默认使用2
                            # 如果调用函数时提供了exp参数的值，那么就会使用提供的值，而不是默认值
#     return a ** exp

# print(power(3))      # 3² = 9
# print(power(3, 3))   # 3³ = 27

# 返回多个值（本质是元组）
# def calc(a, b):
#     return a+b, a-b, a*b, a/b

# s, d, p, q = calc(10, 4)
# print(calc(10, 4)[2])   # 取出索引值为2的元素，即乘积
# print(s, d, p, q)       # 输出：14 6 40


# 3、已知一个数字列表 list = [59,23,56,78,90,234,64,12,9],求列表中所有数据和
# list = [59,23,56,78,90,234,64,12,9]
# total = 0
# for num in list:
#     total += num
# print(total)    




# def greet(任意参数):
#     """向指定用户打招呼"""
#     print(f"你好，{任意参数}！")
# greet("任意内容")  # 调用函数，，任意内容处的值会被传递给函数的任意参数，输出"你好，任意内容！"
# list1 = [59,23,56,78,90,234,64,12,9]
# list2 = [2,6,5,4,5,6,6,5,6,56,5,6]
# def a(list):               # list 可以为任意形式 ，list的位置也称为形参
#     sum = 0
#     for i in list:
#         sum += i
#     print(sum)                 # 输出列表中所有数据的和
# a(list1)                  # 调用函数a，list1的位置称为实参，实参的值会被传递给形参list，输出列表中所有数据的和
# a(list2)