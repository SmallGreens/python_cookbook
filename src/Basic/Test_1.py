if __name__ == '__main__':

    # use python as calculator
    print(5 ** 2)    # ** 表示 幂 运算
    print(5 ^ 2)    # 位异或
    print(5/2)      # 除法会自动将整数转为浮点数，输出 2.5
    print(5//2)     # 如果想得到整数部分，使用双 `//`， 输出 2

    # 字符串相关操作
    print('Hello "double quotes"')  # 可以单引号表示字符串，这时 里面可以用 双引号无需转义
    print("Hello 'single quote' ")  # 同上
    print("use '\\' to escape quotes: \"")
    print(r'C:\name')               # 使用 r + 字符串，后面的 '\' 将不表示转义
    print('first line'
          ' second line')            # 相邻字符串可以自动拼接成单行 -- 字符串变量不行
    print(3 * 'Hello ' + 'world!')  # 字符串拼接
    word = "Python"
    print(word[-1])     # 输出 'n'， python 中支持 负的 index，表示从 string 尾部开始数
    # string 是 immutable 的，word[0] = 'J' 会报错
    print(len(word))          # len() 函数，获取 word 的长度

    # List 相关操作 -- 这里所谓的list 其实就是 java 中的数组
    square = [1, 4, 9, 16, 25]
    print(square)           # 直接打印出 [1, 4, 9, 16, 25] -- 比 java：Arrays.toString(square) 方便太多！！
    square[0] = 0           # 数组 是 mutable 的
    square.append(6 ** 2)   # 向数组中添加元素
    words = ['a', 'b', 'c']
    arr = [square, words]   # 支持多维数组且数组中的元素不需要都为同一类型。这里二维数组的第一个元素是整数数组，第二个为 string 数组
