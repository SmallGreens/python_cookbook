import doctest
import glob
import os
import random
import statistics
import sys
from datetime import date
from timeit import Timer
from urllib.request import urlopen

if __name__ == '__main__':
    '''
    通用操作：
        dir('module 名') -- 返回该 module 中的所有函数
        help('module 名')  -- 返回该 module 的帮助信息
        
    操作系统接口- os
        使用方法：import os -- note: 不要用 from os import *， 因为这样， os.open() 会覆盖原来的内置函数 open()
        常用方法：
            os.getcwd() # 获取当前路径
            os.chdir() # 更换当前目录
            os.system()  # 相当于在 cmd 中执行指令
    
    文件操作、文件夹管理 - shutil
        import shutil
        常用方法：
            shutil.copyfile(A, B)  -- 复制 A 文件为 B
            shutil.move(A, B)  -- 将内容从 A 处复制到 B 处
    
    文件通配符 -glob
        glob 模块提供使用 通配符查询文件的函数， glob.glob('*.py')
    
    程序执行参数获取：sys 和 argparse module
    
    错误重定向及程序终止时的输出：sys.stdin, sys.stdout, sys.stderr.  
    
    正则表达式： re module
        re.findall('reg exp', 'string ...')  # 从string 中找出所有满足前面正则表达式的内容 

    '''
    print(os.getcwd())
    print(glob.glob('*.py'))
    print(sys.argv)  # 程序执行参数：包括运行的函数名，以及函数参数。 -- 更复杂的参数获取及解析： argparse module

    '''
    数学 math module
        math.cos(math.pi / 4) -- 0.707, math.log(1024, 2) -- 10.0
        
    random module: 
        random.choice([xx, xx, xx]) # 从list中随机选择一个
        random。sample()   # 随机取样
        random.randrange(6)   # 随机返回一个 range(6) 包含的整数
        
    statistics module:
        提供统计相关的函数。
        statistics.mean(list)  # 返回平均值
        
    与数学相关的内容，更多的参考 SciPy 项目： <https://scipy.org>
    '''

    print(random.sample(range(100), 10))   # 随机采样，0-100 之间随机返回10个数，without 重复
    data = [8, 3, 4, 6, 0, 2, 1, 7, 9, 5]
    print(statistics.mean(data))   # 求均值，输出 4.5

    '''
    网络相关
        urllib.request: 从 URL 中 retrieve 数据
        smtplib: 邮件发送相关
    '''
    with urlopen('https://www.baidu.com/') as response:
        for line in response:
            line = line.decode('utf-8')  # Decoding the binary data to text.
            # if 'href' in line:  # 获取页面中所有的链接
                # print(line)

    '''
    日期和时间模块 datetime module
        %m - 月份； %d -日；%y: 年；-- 都以2位显示
        %b, 英文缩写月份； % Y-- 4位显示年份；%A: 星期几；%B: 英文月份全称。
    '''
    # from datetime import date
    now = date.today()
    print(now)   # 2021-02-16
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    birthday = date(1988, 12, 25)
    age = now - birthday
    print(age.days)

    '''
    计时器判断程序执行时间：
        from timeit import Timer -- 短语句
        profile, pstats module，为长段语句计时
    '''
    a = Timer('t = a; a = b; b = t', 'a = 1; b = 2').timeit()
    b = Timer('a, b = b, a', 'a = 1; b = 2').timeit()
    print('传统交换两数耗时：', a)
    print('使用元组自动拆包装包特性交换两个数，耗时： ', b)

    '''
    测试：
        doctest module: 可以将块代码的测试写在 函数定义处的注释中，执行时 'doctest.testmod()' -- 自动调用doctest 中的测试代码
        unittest module: 单元测试
    '''
    def average(values):
        """
        >>> print(average([5, 8, 10, 1]))
        6.0
        """
        return sum(values) / len(values) + 1

    doctest.testmod()  # 如果测试正确。没有返回。如果测试结果错误

    '''
    **********************************************************************
    File "xxx/Python_cookbook/src/Basic/StandardLib1.py", line 105, in __main__.average
    Failed example:
        print(average([5, 8, 10, 1]))
    Expected:
        6.0
    Got:
        7.0
    **********************************************************************
    1 items had failures:
       1 of   1 in __main__.average
    ***Test Failed*** 1 failures.
    
    Process finished with exit code 0
    '''
