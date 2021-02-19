import builtins

import ModulesExample
if __name__ == '__main__':
    '''
    link: https://docs.python.org/3.8/tutorial/modules.html
    
    modules: 模块，模组的意思。-- 在 python 中，其实就是一个文件，提供一些可供复用的代码。
    module 中定义的内容可以被 imported 到其他 modules 中。
    使用 import 导入 modules
    使用 ‘modules_name.modules_fcn()’ 调用 modules 中的函数
        这样调用的原因是，modules 中的变量、函数名是属于 modules 自己的变量域的（private symbol table）
        也可以通过 'from ModulesExample import fcn', 将modules 的函数名，变量名导入，从而可以直接在当前函数中使用
        或者使用 'from ModulesExample import *' 导入所有的函数变量名(note: 以下划线开头的 名字不会被导入，例如 '_x')
        'import xxx as aaa' 将 xxx modules 导入并给一个别名
    注意：modules 在每次编译过程中只会导入一次，如果想在执行过程中再次导入，'importlib.reload()'
    '''
    ModulesExample.fcn()

    '''
    modules 中
        - `__name__` 为当前 modules 的名字，也就是 modules 的文件名
    '''
    print(ModulesExample.__name__)

    '''
    modules 的搜寻过程：
        - 首先在 built-in modules 中查找；
        - 如果 不在 built-in modules 中，在 'sys.path' 指定的路径中查找
    modules编译机制：
        为了加速 modules 加载，python 会将 编译完成的 modules 在 __pycache__ 文件夹中进行缓存。
        python 会通过检查修改时间来决定是否要重写compile modules（note: 对于没有源码的 module，python不会检查是否需要更新 cache）
    标准 modules：
        python 提供了一些标准的内置module，来提供对系统的基础操作的控制。
        一个值得注意的 module 是： 'sys', 可以使用 'sys.ps1, sys.ps2' 修改python 命令行的 提示符(default is '>>>')
    dir() 函数
        可以查询这个 module 定义了哪些变量，函数。-- 看下面例子
    '''
    print(dir(ModulesExample))
    # 输出：['__builtins__', '__cached__', '__doc__', '__file__',
    # '__loader__', '__name__', '__package__', '__spec__', 'fcn']
    print(dir())    # dir() 不带参数，返回当前所在 module 定义的变量、函数名
    print(dir(builtins))    # dir(builtins) 返回所有 built-in 函数和变量的名字 -- 需要 import builtins

    '''
    包- packages
        在 python 中，包是一系列 modules 的集合。设包名为 A， ’A.B‘ 调用包 A 中的 module B
        对于不同包中的module，即使重名也没有问题。
    
    tutorial 中举了一个 声音处理包的例子。
        假设我们需要写一个声音处理的程序，由于声音文件的格式很多，还可以添加各种声音效果，我们可以按照下面的方法构建我们的声音处理包。
        __init__.py 文件的作用是告诉 python 其所在的文件夹为一个 package，该文件常常可以为空，也可以放置一些用于初始化包的代码
        在 import 时，可以 import 一个单独的 module：
            'import sound.effects.echo'， 调用时需要： 'sound.effects.echo.fcn()'
            'from sound.effects import echo' 调用时更简单一些： echo.fcn() 即可
        
    sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
              
    需要注意的是表达 "from sound.effects import *"：
        默认的，它不会将 sound.effects 包中的所有 modules 都 import 进来，而只是 import 属于对应 package 的变量等（通常定义在 
          __init__.py 中）
        若想通过上述表达式 导入 modules，需要在 __init__.py 中将要导入的 modules 名赋值给 ‘__all__’，例如：
          __all__ = ['echo', 'surround', 'reverse']
    推荐使用 'from package import specific_submodule' 的方式导入具体的 module（除非有名字冲突，可以再多导入一个包名）
    import 时也可以使用相对路径：
        例如在 effects 包中的 surround.py module 中，想导入 echo module，以及 filters package 中的 equalizer modules，可以使用：
            from .. import echo
            from ..filters import equalizer  
    '''

