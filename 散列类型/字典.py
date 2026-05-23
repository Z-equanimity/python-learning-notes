"""
字典
"""

"""
# 字典：用来保存对应关系的数据
1.1特征：①使用  {}  存储元素
        ②每一个元素以  键值对  存储，多个键值对之间使用逗号分割，分格写也要使用逗号隔开

 name是键(key)，芗泽是值(value)。 字典当中的键可以重复，值不可重复，如果重复了，后面的值会覆盖前面的值
        
        
 
 
第一种书写方式   
a = {'name':'芗泽'，'age':18,'diz':'河南'}
第二种书写方式
a = {
    'name':'芗泽',
    'age':18,
    'diz':'河南'
}
"""


"""
student = {
    "name": "小明",
    "age": 18,
    "scores": {"math": 95, "english": 88}
}
print(student)                 # {'name': '小明', 'age': 18, 'scores': {'math': 95, 'english': 88}}


# 访问
print(student["name"])         # 小明
print(student.get("grade", "未知"))   # 未知（安全访问，不存在返回默认值）

# 增改
student["grade"] = "高一"       #变量["new_键"] = "new_值"
print(student)                  # 新增了 grade 键

student["age"] = 19
print(student)                 # age 已被修改为 19

# 删除：删除整个键值对
del student["grade"]
print(student)                 # grade 已被删除

age = student.pop("age")       # pop方法会有一个返回值，返回的就是被删除的那个元素
print(age)                     # 19（被取出的值）
print(student)                 # age 已被删除

# 取值
字典[键]


"""
# 添加的内容
student = {
    "name": "小明",
    "age": 18,
    "scores": {"math": 95, "english": 88}
}



















































