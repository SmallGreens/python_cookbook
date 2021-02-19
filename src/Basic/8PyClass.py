if __name__ == '__main__':
    '''
    link: https://docs.python.org/3.8/tutorial/classes.html
    
    python 的继承与 其他面向对象语言的语言类似。
        python 支持多继承；
        python 子类 可以 override 它父类的任意方法
    namespace：名称空间，也就是变量名，或方法名的作用域， 由于 python 脚本语言的特点，作用域概念比较复杂
        - global 作用域：module 文件中最外层声明的变量具有 global 作用域；
        - local 作用域，一般是在函数中，类中的变量，作用域仅在对应的函数、类，故称为 局部作用域；

    通常使用 'xx.属性名' 来指出特定对象/ module 中的属性值。
    
    python引用变量的顺序： 当前作用域局部变量 -> 外层作用域变量 -> 当前模块（module）中的全局变量 -> python内置变量
    
    global 关键字：用于在局部作用域中使用全局变量 -- global 一般指在 module 中定义的变量、函数
    nonlocal：用于在局部作用域中使用 外层变量 -- 非全局变量。参考下面的例子：
    
    python 类：
        - 声明方式： 'class ClassName(BaseClassName): '   -- 也可以没有 base class，直接：'class ClassName: '
        - 变量：在 class 中直接声明的变量属于 class，属于类的实例对象的变量需要用 'self.varName' 的形式；
        - 迭代器：当使用 for 循环迭代对象时，会调用该对象的类的 '__iter__()' 方法， 
          该方法会返回一个带有 '__next__()' 方法的迭代器来遍历对象
        - yield 生成器的使用。
         
    '''
    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam  # 指定该 spam 为外层函数中的 spam 变量
            spam = "nonlocal spam"

        def do_global():
            global spam     # 指定该 spam 为 全局的 spam 变量
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)

    g_count = 0

    def global_test1():
        try:
            gcount += 1   # 在函数中使用与 global 变量具有相同名称的变量， python 会默认认为该变量为局部变量。故而这里会引发 异常
        except NameError as err:
            print('nameError:', err)

    global_test1()

    def global_test2():
        global g_count    # 先使用 global 关键字对该变量进行声明，才能在 局部 作用域 中对该变量进行修改
        g_count += 1
        print(g_count)
    global_test2()      # 输出 1

    def global_test3():
        print(g_count)  # 如果局部函数中，不修改 global 变量，则不需要声明可以直接使用
    global_test3()  # 输出 1 （因为在 global_test2() 函数中进行了修改）

    '''
    python 中类的作用域为局部作用域。当 class 的定义完成时，一个该 class 的对象就会同时创建。
    class 对象支持两种操作：属性引用 和 实例化
    '''
    print('*' * 40)

    class TestClass:
        """A simple class example."""
        def __init__(self, real_part, im_part):
            print('create the new instance of the class')
            self.data = []
            self.r = real_part
            self.i = im_part

        i = 123

        def f(self):
            return 'hello class'

    # 属性引用，使用 '.' 来用类名引用类中的函数或者变量
    print(TestClass.i)
    print(TestClass.f)  # 输出： <function TestClass.f at 0x00000xxxxxxxxx>
    print(TestClass.f(TestClass(1,2)))      # f(self) 如果直接使用类名调用的话，需要传入一个该函数的实例
    print(TestClass.__doc__)    # 获取 类的 doc 内容，输出：A simple class example.

    print('*' * 40)
    # 实例化 -- 获取一个该类的新实例
    x = TestClass(3, 5)     # 会调用 '__init__(self)' 函数对该实例进行初始化
    print(x.r, x.i)

    # 一般的，我们称 类中的函数（function）为 方法（method）
    print(x.f())    # 输出： hello class ==> 等价于调用 TestClass.f(x)
    xf = x.f        # 可以将该方法复制给一个变量（实际上方法也是一个 object）。
    print(xf())

    '''
    class 中的变量的使用需要注意，在 类中直接声明的变量类似于 java 中的 静态变量，是所有类的实例共享的。
    如果需要属于 类实例的变量，使用 self.xxxx 来指定该变量
    '''

    class Dog:
        kind = 'canine'     # 被所有类的实例共享的变量

        def __init__(self, name):
            self.name = name
            self.tricks = []    # 属于类的实例的变量在 init 函数中声明

        def add_trick(self, trick):
            self.tricks.append(trick)

    d1 = Dog('Fibo')
    d2 = Dog('Buddy')
    d1.add_trick('roll over')
    d2.add_trick('play dead')
    print(d1.tricks)

    '''
    python 中的继承为： class DerivedClassName(BaseClassName) 被继承的类称为 baseClass
        - 当 子类的对象构建完成时，父类会被记录下来。当 调用子类对象的 某 attributes 时，如果子类中不含有该 attribute，则会去父类中寻找
        - 调用方法亦类似，先调用子类中的方法，如果没有，则沿继承链依次寻找
        - 在 子类中重写方法时，可以使用 'BaseClassName.methodname(self, arguments)' 的形式调用父类的方法
        
    python 中两个内置函数与继承有关：
        - isinstance() 检查实例的类型。`isinstance(obj, int)` 仅当 obj.__class__ 为 int 或者为 int 的子类时，才返回 true
        - issubclass(), 来检查类之间的继承关系。`issubclass(class1, class2)`
        
    python 支持多继承
        class DerivedClassName(Base1, Base2, Base3)
        多继承的方法、属性搜索顺序为从左往右， 深度优先遍历。
        实际搜索继承对象的顺序会更复杂一些，参考: https://www.python.org/download/releases/2.3/mro/
        
    私有变量
        在 python 中，不存在仅能在类内部能够获取的变量。但通常 规定 使用单下划线开头的变量或者方法仅用于 类内部。e.g. _spam
    '''

    '''
    迭代器(iterators): 设计可迭代的类之前，我们先了解一下 for 循环的原理。
        实际上，for xx in xx 语句，会调用对象的 __iter__() 方法，这个函数会返回一个迭代器对象，定义有一个 __next__() 函数，
        可以依次获取元素，当对象中的元素输出完毕时，__next__() 函数 raise 一个 StopIteration 异常，告诉 for 循环终止循环。
    因此，如果想让类可以进行迭代，可以在类中添加 '__next__()' 函数以及 '__iter__()' 函数，如下：
    '''
    class Reverse:
        """Iterator for looping over a sequence backwards."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

    rev = Reverse('spam')
    for char in rev:
        print(char, end=' ')    # 输出： m a p s
    print('\n' + '*' * 40)
    '''
    生成器（generator）
        使用生成器也可以方便的实现 for 循环。generator 使用 yield 代替 return，每次 调用 next() 函数时，generator 会从上次 yield 
        返回的地方恢复并继续执行;
        使用 generator 后，__iter__(), __next__() 会自动生成，并且每次调用 next() 函数，返回前的状态都会自动保存。因此代码更加简洁；
        
    '''
    def reverse(data):
        for index in range(len(data) - 1, -1, -1):
            yield data[index]

    for char in reverse('spam'):
        print(char, end=' ')