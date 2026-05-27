"""
函数的说明文档
"""
# eg
def calculator(a, b, op):
    """
    用来计算数字的功能    
    :param a：第一个数字
    :param b：第二个数字
    :param op：符号
    :return：两个数的运算结果！
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b         
    else:
        raise ValueError(f"不支持的操作符: {op}")
  
"""查看函数说明文档的方法"""
"""1、help()   方法"""
# help(calculator)
"""2、调用函数的时候将鼠标放上去"""


"""
函数的作用域
1、全局作用域：函数之外的地方称为全局作用域
2、局部作用域：函数以内的地方，称为局部作用域
"""
# 变量a就是全局变量，在任何地方都能被调用
# 变量b就是局部变量，只能在调用函数func()时，才能被调用
# 全局变量和局部变量互不干扰
# 在函数中，使用变量时，优先从自身找有没有这个变量，如果有，就用自己的
# a = 10 
# def func():
#     a = 33
#     print(a)
# print(a)
# func()
"""
在函数里面修改函数外面的变量
使用关键字   global
"""
# a = 10 
# def func():
#     #在函数里面  声明  全局变量，并且函数里的可以覆盖函数外的变量
#     global a
#     a = 33
#     print(a)
# func()