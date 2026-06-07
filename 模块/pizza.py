"""模块：
1、本质是py文件，包含了许多函数、类、变量
2、作用：相当于一个工具包
3、分类
    内置模块：py自带
    第三方模块：需要下载pip python提供给我们包管理工具，就可以通过这个工具去下载第三方模块
"""


def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")