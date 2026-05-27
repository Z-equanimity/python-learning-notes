"""
闭包：通常由嵌套函数实现；外层函数中包含内层函数，内层函数引用了外层函数的变量，外层函数将内层函数作为返回值返回。
"""
def outer(x):
    def inner(y):
        return x + y      # 内层函数引用了外层函数的变量x
    return inner          # 外层函数将内层函数作为返回值返回
# 将 外部函数的返回值存放到 变量a里面
a = outer("我真的爱你")
# <function outer.<locals>.inner at 0x000001F7B22FA290>        # 内部函数的地址
print(a)
# 调用函数本质形式是：函数地址()  eg：  outer()
# 所以a = outer("我真的爱你")，即是将内部函数的地址赋值给a。此时若调用内部函数的地址即为 a()
print(a(",没人能比拟"))

