from pathlib import Path
path = Path('D:\python\python_learn\第十章.文件与异常\pi_digits.txt')
contents = path.read_text()
print(contents)