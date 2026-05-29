# 1、修改全局便的值：函数外部定义一个全局变量等于10，在函数内部将全局变量的值修改为15
a = 10
def num():
    global a
    a = 15
    return a
print(num())
# 闭包：函数的嵌套，外层函数中包含内层函数，内层函数引用了外层函数的变量，外层函数将内层函数作为返回值返回。

def a(x):
    def b(y):
        return x+y
    return b
c = a(5)
print(c(5))

# 3、定义一个函数“add_numbers",该函数接受两个整数参数num1和num2，并返回他们的和，请为这个函数添加说明文档
def add_numbers(num1,num2):
    """
    此函数计算num1和num2的和
    :param：num1整数参数
    :param：num1整数参数
    :param：return为两个整数的和
    """
    return num1 + num2 
print(add_numbers(5,6))