from collections import deque
from decimal import Decimal
from heapq import heapify, heappush, heappop
from string import Template

if __name__ == '__main__':
    '''
    https://docs.python.org/3.8/tutorial/stdlib2.html
    介绍一些更加高阶的标准库module
    
    输出格式化
        reprlib module - 对对象输出的格式进行控制
        pprint module - 提供更加高阶的对象输出格式控制
        textwrap - 提供对段落的优化显示
        local - 使用本地（数据库中）定义的数据格式。
        
    模板（templating）
        string module 中的 Template 类。参考下面的例子
        
    处理二进制数据
        struct module 提供 pack() 和 unpack() 方法来处理可变长的二进制数据记录。
        
    多线程 - threading.Thread
        python 中实现多线程可以通过让类继承 threading.Thread 类来实现。具体的线程需要执行的任务，通过复写 run 方法来指定
        多线程最终要的问题是线程间共享数据的安全问题。python 提供 locks，events, condition variables 以及 semaphore
        自己实现多线程同步共享文件同步容易出现问题。可以通过 queue module 来实现两个线程间数据的传输-- 一个将内容推进 queue，一个取出。
        
    logging module
        logging.debug(), logging.info(), logging.warning(), logging.error(), logging.critical() 
        重要程度依次上升。
        
    weak reference 弱引用
        使用弱引用 引用的对象随时都可能被垃圾回收机制销毁，从而可以减少循环引用引起的问题（对循环引用。垃圾回收机制可能无法自动释放资源）
        https://segmentfault.com/a/1190000005729873
        
    更多集合类相关的工具
        array module。 array.array() 方法，可以更加紧凑的存储元素（固定类型，固定存储空间大小），例如：
           a.array('H', [100, 200, 23]) # H 为存储内容的 typecode，表示 2 byte unsigned 二进制数。
           -- python 中的 list 默认每个元素占用 16 bytes
        collections module 的 deque() 提供对象，可以提升从左边增删元素的效率（但查询效率较低）。
        bisect module 用于处理 排序的 list
        heapq module: 堆功能，实现了一个小顶堆，总是让最小值位于 list 第一个 - 常用方法有 heapify(data), heappush(), heappop() 
        
    Decimal 浮点计算
        decimal module 中提供 Decimal 数据类型，可以提供更加精确的小数计算， 常见的用处有以下几点：
            金融等领域，需要更加精确的小数计算；
            用于控制计算精度；
            控制 round 方法；
            ...
    '''

    t = Template('${village}folk send $$10 to $cause.')
    print(t.substitute(village='Nottingham', cause='the ditch fund'))
    # 上述代码输出： Nottinghamfolk send $10 to the ditch fund.
    # substitute() 方法在 占位符不存在时会返回 KeyError exception,
    # 可以使用 safe_substitute() 方法，当占位符不存在会使用占位符的名字直接替代

    d = deque(['task1', 'task2', 'task3'])
    d.append('task4')
    print(d)  # deque(['task1', 'task2', 'task3', 'task4'])
    print(d.popleft())   # task1

    data = [84, 11, 1, 6, 8, 45, 76, 89, 12, 34, 21, 66]
    heapify(data)
    print(data) # [1, 6, 45, 11, 8, 66, 76, 89, 12, 34, 21, 84]
    heappush(data, -1)
    for i in range(3):
        print(heappop(data), end=' ')  # -1 1 6

    print('\n'+ '*' * 40)
    print(round(Decimal('0.70') * Decimal('1.05'), 3))  # 保留3位小数




