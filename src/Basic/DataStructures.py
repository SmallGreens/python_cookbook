from collections import deque
from math import pi

if __name__ == '__main__':
    '''
    List 的方法举例：
    - append(), 
    - extend(iterable): 将iterable 中所有的元素append 到 list后面
    - insert(i, x), 
    - remove(x) -- 移除list 中第一个等于 x 的元素， 如果x 不在队列中，抛出 ValueError,
    - pop([i]), 移除并返回 list 中位置为i的元素，如果不指定i，则移除并返回list 中最后一个元素，note: 使用方括号表示参数是optional的；
    - clear(), 将 list 中的元素全部删除，等价于 del a[:]
    - index(x[,start [, end]])， 注意 start 和 end 用于指定范围，而 x 的值是相对 list 的最左边的元素来算的，而不是start 值
    - count(x), 返回 x 在 list 中出现的次数
    - sort(*, key=None, reverse=False), 注意第一个 * 表示后面的参数是 keyword 参数，即键值对参数
    - reverse(), 
    - copy(): 返回 list 的浅拷贝，等价于 a[:]
    '''
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.reverse()
    fruits.append("watermelon")
    print(fruits)
    print(fruits.pop())
    fruits.insert(5, 'grape')
    animals = fruits.copy()
    animals[1] = 'dog'
    animals.append('cat')
    print(fruits, id(fruits), animals, id(animals))      # animals list 与 fruit list 不同了！

    '''
    stack, queue 的实现
    '''
    # 直接使用 list 实现 stack, list 的尾部为 栈顶
    stack = [1,2,3]
    print(stack.pop())
    stack.append(4)
    print(stack.pop())
    # 由于 list 在队列尾操作的效率高，但是在 队列首部操作的效率较低。
    # 因此在 python 中，使用 collections.deque 来实现高效的队尾、队首增删元素
    queue = deque(['Eric', 'John', 'Michael'])
    queue.append('David')
    print(queue.popleft())      # queue- 从队列首移除元素
    print(queue)                # 输出 ’deque(['John', 'Michael', 'David'])‘

    '''
    list comprehension: 列表推导式
    使用表达式来自动填充list
    '''
    squares = [x**2 for x in range(10)]
    print(squares)
    combine = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]  # 元素还可以是使用括号括起来的元祖 tuple
    print(combine)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    round_pi = [str(round(pi, i)) for i in range(1, 6)]     # 还可以在 推导表达式中使用函数
    print(round_pi)
    # 列表推导式还可以生成多维数组，如下方例子中，实现了矩阵的转置
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    matrix_transposed = [[row[i] for row in matrix] for i in range(4)]
    print(matrix_transposed)
    print(list(zip(*matrix)))       # 上述转置用于演示，实际中，推荐使用 python 的 built-in 函数来处理这些常见数学操作

    '''
    使用下标删除list中的元素 del
    '''
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    del a[0]        # 删除第一个元素
    print(a)
    del a[:2]       # 删除前两个元素
    print(a)
    del a[:]        # 删除 list 中所有的元素
    print(a)

    '''
    tuples: 与 strings 和 lists 类似，tuples 也是一种 sequence 类型
    tuple 是 immutable 的，并且它通常包含多种类型的元素。
    获取 tuple 中元素时，通常使用 index 或者 unpacking 的方法
    '''
    t = 123, 456, 'hello!'  # tuple, 元素之间使用 逗号隔开。
    t1 = (123, 456, 'hello!')   # 推荐声明时 带有圆括号
    print(t1[2])
    print(t1)        # 输出 ‘(123, 456, 'hello!')’ 注意是圆括号
    # t[0] = 1, tuple 是 immutable 的，不允许对其元素进行更改 -- 这一点与 list 不同！！
    empty = ()      # 包含 0 个元素的 tuple
    singleton = 'single',   # 包含 1 个元素的 tuple，注意最后需要添加一个逗号
    x, y, z = t     # 将 tuple 中的元素 unpack 并且分别赋值给 x, y, z. 左侧的元素个数需要与右侧序列中元素的个数相等
    print(y)

    '''
    sets 和 dictionaries
    创建 sets 时，可以使用 set(), 或者 {...}
    dict 中，
        list(d) 可以返回dict 中 key 构成的 list，
        in 关键字，检查元素是否在 dict 的key 集合中，
        sorted(d), 可以将 dict 中元素排序
    '''
    basket = {'apple', 'orange', 'beef', 'banana'}
    basket1 = set('apple')       # 注意，这样添加 set，加入的是 {'a', 'e', 'l', 'p'}
    print(basket, basket1)       # {'orange', 'banana', 'apple', 'beef'} -- set 是无序的
    for x in basket:            # 可以使用 for 循环遍历 set
        print(x)
    tel = {'jack': 4098, 'sap': 4139}      # dict 声明, 可以直接用还括号
    tel1 = dict([('sap', 4139), ('guido', 4127), ('jack', 4098)])  # 还可以用 dict 构造函数创建
    tel2 = dict(sap=2139, guido=1298, jack=2452)        # 创建 dict， 另一种方式
    print(tel)
    tel['sap'] = 1111                   # 使用 key 找到对应 value 并且修改 value
    a = list(tel)               # 获取 key 组成的list
    print(a)
    print('*' * 40)
    print('sap' in tel2)        # 判断是否在 dict 的 key 集合中

    '''
    looping 技术
    - items(), 从 map 中同时取出 key， val
    - enumerate(), 遍历 sequence 时同时获取位号和元素
    - zip(), 同时遍历多个 sequences
    - reversed(), 反向遍历
    - sorted(), 按顺序遍历 序列
    - 此外，不要在遍历时修改序列，可以通过新建一个新的序列来存储修改后的内容
    '''
    animals = {1: 'dog', 2: 'cat', 3: 'cow'}
    for k, v in animals.items():
        print(k, v)
    stationery = ['ruler', 'rubber', 'pen']
    for i, v in enumerate(stationery):  # 分别给出位号和值
        print(i, v)
    print('*' * 40)
    for v1, v2 in zip(list(animals), stationery):   # 同时遍历多个 sequence
        print(animals[v1], v2)
    for i in reversed(range(1, 10, 2)):
        print(i)
    print('*' * 40)
    to_print = [5, 4, 7, 3, 2, 8]
    for i in sorted(to_print):      # 从小到大 排列
        print(i)

    '''
    更多说明：
        python 中逻辑运算符直接用单词表示， 'and'， 'or', 'not'
        支持链式的比较，例如 a < b == c, 先比较 a 与 b， 然后判断 b 与 c 是相等
        在表达式中，如果需要赋值，python 中要求必须使用 ':=' (walrus operator)
    '''