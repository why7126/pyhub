import os

# file_dir：目标文件夹
file_dir = "/Users/why/Downloads/最全最新Vue、Vuejs教程，从入门到精通"
print(os.walk(file_dir))
for root, dirs, files in os.walk(file_dir):
    print(root)  # 当前目录路径
    print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件