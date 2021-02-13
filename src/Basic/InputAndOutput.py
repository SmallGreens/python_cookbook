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

    # to 7.1.3 of: https://docs.python.org/3.8/tutorial/inputoutput.html
