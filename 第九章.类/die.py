from random import randint

class Die():
    """骰子"""
    def __init__(self,sides =6 ):
        self.sides = sides
    def roll_die(self):
        """生成1-6之间的随机数"""
        return randint(1,self.sides)
"""6面筛子投掷十次的结果"""

die = Die()
for i in range(10):
    print(die.roll_die())