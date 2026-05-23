"""
循环
1.while循环                   #条件满足时持续执行，条件1不成立，自动停止
2.for循环                     #用于 遍历序列（列表、字符串、range等）
"""

"""
while循环

# 从 1 加到 100
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(f"总和是：{total}")  # 5050

# 继续加油
i = 0
while i < 6:
    print("继续加油")
    i += 1
"""

"""
while循环做嵌套,
嵌套循环的特点：外层循环执行一次，内层循环执行所有次
 eg：写三遍我错了，并且今晚去洗碗。这套惩罚执行三天

j = 0
while j < 3:
    i = 0
    while i < 3:
        print("我错了")
        i += 1
    print("今晚洗碗")
    j += 1
"""

"""
for循环：对 可迭代的对象（列表、元组、字符串、集合、字典） 循环
语法形式：   for 变量名(可随便取，不需要提前定义) in 可迭代对象:
"""

"""
遍历字符串
a = "zw"
for i in a:              # 对变量 a 这个字符串 进行 for循环
      print(i)           # for循环特点：将里面的内容一个一个取出来
                         #循环的次数：取决于这个对象里面有多少个值
    
                         
                         
# 遍历列表
list = ["苹果", "香蕉", "橘子"]
for fruit in list:
    print(fruit)

使用for循环，将列表 a =[1,4,5,100,5,78,5]筛选出除了5以外的其他元素并存入一个新的列表当中
a =[1,4,5,100,5,78,5]
result = []
for num in a:
    if num == 5:
        continue
    result.append(num)
print(result)

# 遍历范围
for i in range(5):            
    print(i)                  # 0, 1, 2, 3, 4
    print("字符串")            # 循环五次字符串    

# 所有的方法当中都是用逗号隔开的
for i in range(1, 10, 2):     # 1, 3, 5, 7, 9（步长为 2）
    print(i)

# 遍历字典
student = {"name": "小明", "age": 18}
for key, value in student.items():
    print(f"{key}: {value}")

# enumerate：同时获取索引和值
for idx, fruit in enumerate(["苹果", "香蕉"]):
    print(f"{idx}: {fruit}")

"""
"""
for 循环嵌套
外层循环一次，内层执行所有次

for i in range(2):
    for j in range(2):
        print(i,j)
"""

"""
循环中断
"""

"""
continue  # 跳过当前满足条件的循环，进入下次循环
for i in range(10):
    if i < 3 or i > 6:
        continue
    print(i)

"""

"""
break #退出整个循环，将循环直接结束

 for i in range(10):
    if i > 3 :
        break
    print(i)
"""













































