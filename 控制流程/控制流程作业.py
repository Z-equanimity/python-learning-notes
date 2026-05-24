"""
"""
"""
1、使用for循环,将列表 a =[1,4,5,100,5,78,5]筛选出除了5以外的其他元素并存入一个新的列表当中
"""
# a =[1,4,5,100,5,78,5]
# result = []    # 列表放在循环的外面，若写在循环中，每次循环都会创建一个新的列表，导致之前的结果丢失
# for num in a:
#     if num == 5:
#         continue
#     result.append(num)
# print(result)


# a =[1,4,5,100,5,78,5]
# result = []
# for num in a:
#     if num != 5:     #  != 5 代表不等于5
#         result.append(num)
# print(result)



# age = int(input("请输入年龄："))
# if age > 64:
#     print("可以退休")
# else:
#     print("接着沉淀")


# money = int(input("请输入账户余额："))
# if money >=5000:
#     print("可以旅游")
# elif money >=2000:
#     print("可以购物")


# age = int(input("请输入年纪："))
# ID = input("是否为学生：")
# if age <= 18 and ID == "学生":
#     print("可以获得学生优惠")
# else:
#     print("无法获得学生优惠")



"""
循环题目
"""
# 3、已知一个数字列表 list = [59,23,56,78,90,234,64,12,9],求列表中所有数据和
# list = [59,23,56,78,90,234,64,12,9]
# total = 0
# for num in list:
#     total += num
# print(total)    


# 4、控制台输入用户名，判断用户名是否合法（用户名长度6-10位即为合法，最多十次输入，满足条件结束
# name = input("请输入用户名：")
# count = 0
# while count < 10:
#     if 6 <= len(name) <= 10:
#         print("用户名合法")
#         break
#     else:
#         print("用户名不合法，请重新输入")
#         name = input("请输入用户名：")
#         count += 1

# name = input("请输入用户名：")
# for count in range(10):
#     if 6 <= len(name) <= 10:
#         print("可以使用")
#         break
#     else:
#         print("重起")
#         name = input("请输入用户名：")




