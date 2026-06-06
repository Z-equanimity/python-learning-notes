from random import choices
list = [1,2,3,5,4,9,"s","d","f","g"]
a = choices(list,k=4)
print(f"如果彩票上是{a}，中奖")