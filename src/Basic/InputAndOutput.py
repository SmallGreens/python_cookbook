import json
import math

if __name__ == '__main__':
    '''
    格式化输出 string 有如下几种方式：
        1. 在用 '' 包裹的字符串前面添加 f， 然后使用 '{}' 引用对应的值
        2. 使用 str.format() 进行输出
    '''
    # 使用 f 格式化字符串输出
    year = 2021
    event = 'happy new year'
    print(f'Today is the {event} of {year}')
    print(f'the value of pi is {math.pi:.3f}.') # .3f 表示保留3位小数
    # 使用 str.format 进行格式化输出
    yes_vote = 1000
    no_vote = 200
    percentage = yes_vote / (yes_vote + no_vote)
    st = '{:-4} YES votes {:2.2%}'.format(yes_vote, percentage) # 第一个 {:-4} 指定了该字段占用的字符长度
    print(st)

    '''
    如果不需要格式化输出，简单的将对象变为可输出对象，可以直接使用 repr() 和 str() 函数
    上述二者的区别是， str() 主要是用于便于人阅读，而 repr() 返回结果则是便于 interpret 阅读
    如果 没有预设的便于人阅读的格式，str() 会返回与 repr 相同的值，例如 数字，lists, dictionaries 等结构
    '''
    s = 'Hello world!'
    print(str(s))   # 返回： Hello world!
    print(repr(s))  # 返回： 'Hello world!' -- 多了单引号

    '''
    更多细节 on ： f'字符串' 表达式
    '''
    table = {'test': 10, 'hehe': 20}
    for name, num in table.items():
        print(f'{name:10} ==> {num:10d}') # ':' 后添加整数(不能有空格！！)，表示对应字段占用的最小的长度-- 便于实现对齐.
    # 其他修饰符： !a : ascii(), !s : str(), !r : repr()
    tmp = 'hello'
    s = f'test {tmp!r}'
    print(s)        # 输出：test 'hello'

    '''
    更多 on string format() 方法
    '''
    print('This {} is {}.'.format('method', 'simple')) # 最简单使用，format 中的值与前面空的大括号一一对应
    print('This {arg1} is {arg2}.'.format(arg1='method', arg2='medium')) # 可以给参数命名
    table = {'Soph': 1086, 'Jimmy':2086, 'Kabi': 3066}
    print('Kabi: {0[Kabi]:d}; Soph: {0[Soph]:d}'.format(table)) # 通过 key 取出 dict 中元素。'[]' 中的为元素名
    print('Kabi:{Kabi:d}; Soph:{Soph:d}'.format(**table))  # 两个 ** 表示 keyword 参数

    '''
    读写文件：
        open() 函数返回一个 文件对象， 通常的使用方法为 open(filename, mode)
            mode 可以为：
                'r' 表示只读--如果缺省该参数，默认为只读模式； 
                'w' 只写，如果已经有了相同文件名的文件，则原文件会被删除；
                'a' 表示 append；
                'r+' 表示 可读可写。
        在文件使用完毕后，需要使用 close() 函数将文件资源关闭
        使用 with 关键字 来打开文件，可以让系统在处理完毕文件后自动关闭文件资源。e.g.
            with open('workfile') as f:
                read_data = f.read()
    '''
    with open('Test.txt', 'w') as f:
        f.write('hello world \nhahaha \ntest\n')
    with open('Test.txt', 'a') as f:
        for i in range(10):
            f.write(f'the {i}th line. \n')
    with open('Test.txt') as f:
        print(f.readline()) # 读取一行。并且最后添加 \n 换行。 -- note: 如果是空行，返回 '\n', 而如果是文件尾，返回空字串: ''
        print('*'*10)
        # note: f.read() 读取上面 readline() 接下来的内容，而不是从文件头部开始读起
        print(f.read())    # f.read(size) 指定读取的字符个数。-- 如果缺省 size，则读取所有内容。
    print('*' * 40)
    with open('Test.txt') as f:
        for line in f:
            print(line, end='')     # 推荐：使用 for 循环读取文件中的内容
    value_to_be_written = ('tuple', 1214)
    with open('Test.txt', 'a') as f:
        f.write(str(value_to_be_written))   # 必须先将对象转换为 str 才能写入。写入的 tuple 为: ('tuple', 1214)
        print(len(str(value_to_be_written)))
        print(f.tell())     # tell() 返回当前读写指针在文件中的位置
        # f.seek() 可以切换当前读写指针位于的位置

    '''
    在文件中使用 json 保存数据结构
        在 python 中，可以使用 标准 module json 来处理，
        将数据转换为 json 的过程称为 serializing，将 json 变回python 中数据则称为 deserializing.
    '''
    list = [1, 'simple', 'list']
    s = json.dumps(list)   # dumps() 函数将 list 转为 json 并返回
    print(s)
    with open('Test.txt', 'a') as f:
        f.write('\n')
        json.dump(list, f)      # dump() 函数 将 list 转为 json 并写入到文件中
    x = json.loads(s)       # loads()  从 json 串中解析出 python 数据结构。 load() 函数则是从文件中解析出对应结构
    print(x[1])