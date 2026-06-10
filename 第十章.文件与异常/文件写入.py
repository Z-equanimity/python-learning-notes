# 写入文件
with open("test.txt", "w", encoding="utf-8") as f:  # as f 将变量赋值给f
    f.write("第一行\n")
    f.write("第二行\n")
print("写入完成！")

# 读取全部内容
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(repr(content))       # 输出：'第一行\n第二行\n'

# 逐行读取
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())    # 第一行\n第二行

# 追加写入
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("追加的内容\n")

# 验证追加结果
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())            # 第一行\n第二行\n追加的内容\n

# with 语句会自动关闭文件
# 等价于：
f = open("test.txt", "r",encoding="utf-8")
try:
    data = f.read()
finally:
    f.close()