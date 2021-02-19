import sys

if __name__ == '__main__':
    '''
    link: https://docs.python.org/3.8/tutorial/errors.html
    python 中有两种报错情况，一种是语法错误，一种是 exceptions。这里重点对 exceptions 相关的内容进行介绍。  
        built-in Exceptions：在 python 中有一些 built-in 的Exceptions 例如 被零除(ZeroDivisionError); 命名错误(NameError)等
        可以自定义 Exception
    python 使用 try ... except 语句来处理异常：
        else： 当try 中没有任何异常发生时，执行 else 中的内容；
        raise： 类似 java 中的 throw 关键字，用于异常的抛出，将异常交由外围的 caller 处理
        finally：无论 try 中是否有异常发生，都会执行 finally 语句中的内容 
    try, except, else 等的顺序：try--> except X--> except--> else--> finally
    '''
    # python 中处理 exception 得 方案：
    # 下面的函数让用户输入一个数字，如果用户没有输出和规格的内容，则不断重复让用户输入，直到获得数字输入为止
    while True:
        try:
            x = int(input('Please enter a number: '))  # 如果发生异常，则跳转到 except 子句中，并且对所抛出的exception 进行判断
            break
        except ValueError:  # 如果上面的exception 是 valueError 则执行下面的语句
            print('The input is invalid, please try again!')
    # except 后面可以跟多个 exception 例如： except (RuntimeError, TypeError, NameError)
    # 最后一个 except 可以为 空，serve as a wildcard.
    try:
        f = open('file.txt')
        s = f.readline()
        i = int(s.strip())
        print(i)
    except OSError as err:
        print('OS error: {0}'.format(err))
    except ValueError:
        print('Convert data to int failed.')
    except:  # 使用不指定具体 exception 的子句时，需要小心，可能会将程序运行中的 error 掩盖掉。慎用！！
        print('Unexpected error!: ', sys.exc_info()[0])
        raise  # 重新 raise exception，允许调用者处理
    # else 语句，当 try 语句中没有任何异常发生时，执行 else 中的内容
    for arg in sys.argv[1:]:  # 这里没有执行。。
        try:
            f = open(arg, 'r')
        except OSError:
            print('can\'t open ', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()
    # 用户也可以自定义 exception. 在定义的时候以 'Exception' 为基类 进行拓展。e.g.
    # class Error(Exception):

    # finally 语句，用于文件的关闭等 无论程序是否发生异常都必须执行的task
    try:
        # raise KeyboardInterrupt
        print('hehe')
    finally:
        print('Goodbye!')
    '''
    关于 finally 语句的一些细节讨论：
        - 如果 try 子句中发生了 exception，并且这个 exception 没有被 except 子句处理，exception 会在 finally 子句执行完毕后被 raise
        - 如果 except 和 else 子句中发生了 exception， 则该 exception 会在 finally 子句执行完毕后被 raise
        - 如果 try 语句中有 break, continue, return，则 finally 子句会在上述语句返回前执行（execute just prior to ...）
        - 如果 finally 子句中有 return 语句，则最终的 return 值是 finally 子句中的，而不是 try 子句中的 return 值
    
    python 中 else 语句的作用：
        ref: https://stackoverflow.com/questions/855759/python-try-else
        上述参考中，指出，else 基本上没什么用。。 
        一个特殊的用处是，如果待执行的操作中，可能发生多次 error，但是最后一次error 我们不想捕获，则可以把它放置到 else 中。
        -- 参考下面的例子
    '''


    class MyError(Exception):
        def __init__(self, error_info):
            super().__init__(self)  # 初始化父类
            self.error_info = error_info

        def __str__(self):
            return self.error_info


    try:
        print('test1')
        x = int(input("please input a number: "))
        if x > 5:
            raise MyError("too large number")
    except ValueError:
        print('convert to int failed.')
    except myError as e:
        print(e)
    else:
        x = int(input("please input a number: "))   # 这里不想被 catch error
        print(x)
