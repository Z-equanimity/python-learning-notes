"""
1、定义一个函数a，功能是打印你好，我好，大家好，并调用此函数
"""

# def a():
#     print("你好")
#     print("我好")
#     print("大家好")
# a()
"""
2、在函数a的前提下，运行100次
"""
# i = 0 
# while i < 105:
#     a()
#     i += 1
#     print(f"这是第{i}次打印")
# for i in range(100):
#     a()
#     print(f"这是第{i+1}次打印")

"""
3、定义一个函数，实现两个数的计算（加减乘除）
"""
# def calculator(a, b, op):             #  函数中的参数为形参，调用函数时参数为实参
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '/':
#         return a / b         # 如果是return，则调用函数时需要print 
#     else:
#         raise ValueError(f"不支持的操作符: {op}")
# q = int(input("请输入数字"))
# w = int(input("请输入数字"))
# e = input("请输入符号")
# print(calculator(q, w, e))

# def calculator(a, b, op):
#     if op == '+':
#         print(a + b)            #  如果是print，则调用函数时不需要使用print
#     elif op == '-':
#         print(a - b)
#     elif op == '*':
#         print(a * b)
#     elif op == '/':
#         print(a / b)
#     else:
#         raise ValueError(f"不支持的操作符: {op}")
# q = int(input("请输入数字"))
# w = int(input("请输入数字"))
# e = input("请输入符号")
# calculator(q, w, e)


"""
4、定义一个函数，输出两个数中的最大值
"""
# def get_MAX(a,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# print(get_MAX(5,8))      # 输出结果为 8 和 None
                    #  原因： 定义的函数没有return语句
# 修改方法一
# def get_MAX(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(get_MAX(5,8)) 

# # 修改方法二
# def get_MAX(a,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# get_MAX(5,8)

"""
5、定义一个函数，输出字符串中的内容，如果字符串长度为1，则获取第一个字符，否则获取最后一个字符
"""

# def quzhi(str):
#     if len(str) == 1:
#         print(str[0])
#     else:
#         print(str[-1])
# a = "你想要什么"
# quzhi(a)


"""
6、定义一个函数，输出两个列表合并后的结果
"""
# def hb(list1,list2):
#     list1.extend(list2)
#     return list1
# a = ["我真的爱你"]
# b = ["没人能比拟"]
# print(hb(a,b))

# def hb(list1,list2):
#         return list1+list2
# a = ["我真的爱你"]
# b = ["没人能比拟"]
# print(hb(a,b))

# append方法+循环
# def hb(list1,list2):    
#     for i in list2:
#         list1.append(i)
#     return list1    
# a = ["我真的爱你"]
# b = ["没人能比拟"]
# print(hb(a,b))

# # 解包  *
# def hb(list1,list2):
#         return [*list1,*list2]
# a = ["我真的爱你"]
# b = ["没人能比拟"]
# print(hb(a,b))