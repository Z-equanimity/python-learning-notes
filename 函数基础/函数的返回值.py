
# 函数的定义及调用
def greet(任意参数):
    """向指定用户打招呼"""
    print(f"你好，{任意参数}！")
greet("任意内容")  # 调用函数，，任意内容处的值会被传递给函数的任意参数，输出"你好，任意内容！"


"""
返回值问题
"""
# def a():
#     # return 关键字   可以返回函数的结果
#     return 5+6
# result = a()
# print(result)

def add(a,b):
    return a + b

result = add(3,5)
print(result)  # 8

# 默认参数
def power(a, exp=2):      # exp=2 是Python 函数的默认参数，当调用函数时，如果没有提供exp参数的值，那么exp就会默认使用2
                          # 如果调用函数时提供了exp参数的值，那么就会使用提供的值，而不是默认值
    return a ** exp

print(power(3))      # 3² = 9
print(power(3, 3))   # 3³ = 27

# 返回多个值（本质是元组）
def calc(a, b):
    return a+b, a-b, a*b, a/b

s, d, p, q = calc(10, 3)