# 乘法表从1到10
def do_something():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j}", end="\t")  # 使用\t来添加制表符，使输出更整齐
        print()  # 每完成一行后换行
if __name__ == '__main__':
    do_something()
