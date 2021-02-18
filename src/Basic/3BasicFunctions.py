if __name__ == '__main__':
    '''
    link: https://docs.python.org/3.8/tutorial/controlflow.html
    def 定义函数 
    类似 java， python 的函数参数也使用值传递 -- 引用类型浅拷贝
    '''
    def fib(n):  # 打印 Fibonacci 数列小于 n 的元素
        """Print a Fibonacci series up to n."""  # document string， 类似 java 的 /**    */
        a, b = 0, 1
        while a < n:
            print(a, end=' ')  # 不用换行
            a, b = b, a + b
        print()


    fib(2000)
    f = fib  # 函数也是一个对象，可以通过赋值传递函数引用
    f(2000)
    print(f(0))  # 如果没有指明返回值，函数返回值默认为 `none`

    ''' 带有返回值的 函数 '''
    def fib2(n):
        """  Return a list containing the Fibonacci series up to n. """
        a, b = 0, 1
        res = []
        while a < n:
            res.append(a)
            a, b = b, a + b
        return res

    print(fib2(200))

    ''' 函数允许可变参数。可以通过给函数参数默认值的方式来实现类似 java 的函数重载 '''
    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            # ok = input(prompt)
            ok = 'y'
            if ok in ('y', 'yes', 'N'):
                return True
            if ok in ('n', 'N', 'no', 'nop'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)


    # 调用上述函数
    print(ask_ok('Do you want to quit?'))  # 仅提供必需的 参数 prompt
    print(ask_ok('Want to overwrite the file?', 2))  # 还提供 retry 参数

    '''
    Warning: 默认值只执行一次，后序执行中会使用上一次的值。对于 mutable 的 默认值，可能会出现每次执行都不相同的情况
    '''
    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))  # [1]
    print(f(2))  # [1, 2]

    '''调用函数时，可以使用 keyword arguments 的形式进行调用， 即 kwarg=value 的形式。如下：'''
    print(ask_ok(retries=2, prompt='Hello'))
    ''' 如果同时有 positional arg 和 keyword arg，必需将 positional arg 放在前面。'''
    print(ask_ok('hello', retries=2))

    ''' 允许使用 *name 的形式接受多个 positional args， 使用 **name， 接收多个键值对形式的 keyword args '''
    def cheese_shop(kind, *args, **kwargs):
        print("-- Do you have any", kind, '?')
        print('-- Sorry, out of', kind, '.')
        for arg in args:
            print(arg)
        print('-' * 40)
        for kw in kwargs:
            print(kw, ":", kwargs[kw])  # 类似 map， 其中 ’kw‘ 是 key， 使用 ’kwargs[kw]‘ 获取 key 对应的 value

    # 调用
    cheese_shop("Limburger", "It's very runny, sir.",
                "It's really runny, sir.",
                shopkeeper="Michael",
                client="John",
                sketch="Cheese Shop Sketch")

    '''
    可以使用 / 和 * 来分隔 position args 和 keywords args
        def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
              -----------    ----------     ----------
                |            |                       |
                |          Positional or keyword     |
                |                                   - Keyword only
                -- Positional only
    '''

    '''
    unpacking args lists, python 可以通过 ‘*’ 将list 或 tuple 中的内容 unpack 出来作为函数的参数
    可以通过 '**' 将 dictionaries 中的元素 unpack 出来作为 keywords 参数
    '''
    print(list(range(1,6)))  # [1, 2, 3, 4, 5]
    args = [1, 6]
    print(list(range(*args)))       # * 将list 中的元素unpack 出来作为参数，执行效果与 `print(list(range(1,6)))` 相同

    def print_kws(**kwargs):
        for kw in kwargs:
            print(kw, kwargs[kw])
    d = {"￥:": "RMB", "$:": "USD", "*": "BitCoin"}
    print_kws(**d)          # 使用 ** 将参数从 dictionaries 中解压出来

    ''' 可以使用 lambda 表达式来表示简短的匿名函数， 如下'''
    def make_increment(n):
        return lambda x: x + n      # lambda 表达式中变量的范围与 nested 函数 类似

    f = make_increment(10)
    print(f(20))        # 输出： 30
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])    # pair 为输入参数， `:` 后面为 输出参数，这里为 `pair[1]`, 就是变成按照字母顺序排序
    print(pairs)

    ''' python 的注释可以插入到函数中 '''
    def f(arg1:'冒号后面是对应参数的注释', arg2) -> str:
        print('Annotations:', f.__annotations__)
        return 'str 是返回值的注释'
    print(f(1,2))

