"""导入模块"""
# import modul_name
import pizza
"""python运行这行代码会让python打开pizza.py，并将其中所有的函数都复制到这个程序当中"""
pizza.make_pizza(16,"qwer")
pizza.make_pizza(12,"aa","ss","dd")
"""要调用被导入模块中的函数，可指定被导入被导入模块的名称（文件名）pizza和函数名make_pizza()，并用句点隔开"""

import time
print("你好")
time.sleep(3)   #  当前的程序睡眠三秒钟
print("你好")


"""导入模块中特定的函数"""
# from modul_name import function_name
# form modul_name import function_0,import function_1,import function_2
"""依据第二行可以从模块中任意数量的函数"""
from pizza import make_pizza
make_pizza(16,"qwer")
make_pizza(12,"aa","ss","dd")

"""使用as给函数指定别名"""
# # from modul_name import function_name as fn
from pizza import make_pizza as mp
"""给定之后，每当需要调用make_pizza()时，都可将其简写为mp()"""
mp(16,"qwer")
mp(12,"aa","ss","dd")

"""使用as给模块指定别名"""
# from modul_name as mn
import pizza as p
p.make_pizza(16,"qwer")
p.make_pizza(12,"aa","ss","dd")

"""导入模块中所有的函数"""
# form modul_name import *   #不推荐使用这种导入方式
from pizza import *
make_pizza(16,"qwer")
make_pizza(12,"aa","ss","dd")
"""
import语句中的*让python将模块pizza中的每个函数都复制到这个程序文件中
所以可通过函数名称来调用每个函数，无须使用句点
"""

"""函数命名一般形式：
def function_name(parameter_0,parameter_1='default value')
"""