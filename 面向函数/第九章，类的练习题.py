# 练习9.1、9.2、9.4：餐馆
class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.name},{self.type}")
    def open_restaurant(self):
        print("正在营业")
    def update_number_served(self,number):
        self.number_served = number        
    def read_number_served(self):
        print(f"就餐人数{self.number_served}")
    def increment_number_servrd(self,newing):
        if newing > 0:
            self.number_served += newing 
        else:
            print("今天生意不太行啊，下去沉淀")
name1_restaurant = Restaurant("江南","shuang")
name1_restaurant.describe_restaurant()
name1_restaurant.update_number_served(3)
name1_restaurant.read_number_served()
name1_restaurant.increment_number_servrd(8)
name1_restaurant.read_number_served()
name1_restaurant.open_restaurant()
name2_restaurant = Restaurant("henan","shuang")
name2_restaurant.describe_restaurant()
name3_restaurant = Restaurant("hebei","shuang")
name3_restaurant.describe_restaurant()

# 练习9.3、9.5
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"我的名字是{self.first_name},{self.last_name}")
    def greet_user(self):
        print(f"{self.first_name}{self.last_name}你好")
    def read_login_attempts(self):
        print(f"已经尝试登录{self.login_attempts}")
    def increment_login_attempts(self,add=1):
        self.login_attempts += add
    def reset_login_attempts(self):
        self.login_attempts = 0
user = User("zhang","san")
user.increment_login_attempts(5)
user.increment_login_attempts(1)
user.read_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()