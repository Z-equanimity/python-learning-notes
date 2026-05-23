"""
条件判断
"""

"""
输出方法  input("这个位置可以以字符串的形式提示输入信息：")   可以将用户输入的值保存起来
   input方法输入的是字符串形式
score = int(input("请输入成绩："))
print(type(score))


"""

"""
语法
if  要判断的条件：
    要执行的代码
elif 判断条件                  # 代表多条件判断
slse:                         # else后面不加条件   
    否则就执行这里的代码 
      
"""

"""
1、以提前输入
age = 18
#
if age < 12:        # Python 用 4个空格 表示代码块，不要混用 Tab 和空格！
    print("儿童")    # 规范来说，必须要有四个空格的缩进，缩进代表里面的内容属于上面代码里面的
elif age < 18:
    print("青少年")
elif age < 60:
    print("成年")
else:               
    print("老年")
    
2、客户自行输入

 score = int(input("请输入成绩："))    # 将用户输入的值通过int方法转化为整数值，才能和数字比大小
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "不及格"

print(f"你的等级是：{grade}")
        
"""

"""
# 三元表达式

score = int(input("请输入你的成绩"))
print("良好") if score>=60 else print("下去沉淀")

age = 20
status = "成年" if age >= 18 else "未成年"
print(status)  # "成年"
"""






























