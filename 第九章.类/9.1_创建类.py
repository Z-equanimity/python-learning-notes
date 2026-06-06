"""
1、面向过程：实现某个东西，一步步的方式去完成
def hb(list1,list2):
#     for i in list2:
#         list1.append(list2)
#     return list1
# a = ["我真的爱你"]
# b = ["没人能比拟"]
# print(hb(a,b))

2、面向对象：只要找到对象，让对象帮我们完成工作，不需要管对象是怎么实现的
"""
class Dog:   # 在python中，首字母大写的名称代指的是类
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """
        __init__()方法两边各有两个下划线
        代码含义：初始化属性name和age
        """
        self.name = name
        self.age = age 
        """
        形参name，接受传入的值；实例属性self.name
        代码含义：将传入的name参数的值赋给实例的属性self.name
        """
    def sit(self):
            print(f"{self.name}is now sitting")
    def roll_over(self):
             print(f"{self.name} rolled over")
"""创建实例"""
my_dog = Dog("willie",18)       # my_dog命名约定，首字母大写为类，全小写指的是根据类创建的实例
print(f"my dog's name is {my_dog.name}")     # 访问属性：使用my_dog.name访问my_dog的属性name的值
print(f"my dog is {my_dog.age} years old")
my_dog.sit()                # 调用方法：指定实例名和要调用的方法，之间使用句点分割
my_dog.roll_over()
"""创建多个实例"""
your_dog = Dog("lucy",20)
print(f"your dog's name is {your_dog.name}")
print(f"your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()