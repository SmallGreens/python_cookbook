# 虚拟环境 Virtual Environments

为解决 Python 各种支持库对于不同 python 版本的需求，python 提供一种称为 虚拟环境 的方案。
就是在一个文件夹中构建一个相对独立的环境，将所需的合适版本的python 以及相关库文件都放置在该文件夹中，
 构成一个相对独立的运行环境， 从而不需要在系统层面配置解决python不同版本冲突的问题。

用于创建管理 虚拟环境的 module 为 `venv`，需要创建虚拟环境时，切换到对应文件夹，执行:

> `>>>`python3 -m venv name-env

执行完毕后，会生成一个 `name-env` 的文件夹，其中会包含对应版本的 python 解释器，标准库 等。
生成 虚拟环境后，可以通过 `activate.bat`等脚本激活该虚拟环境。 
激活后，就可以启动该虚拟环境的 python 命令行工具。

# 使用 pip 进行包管理

在 python 中，可以使用 pip 程序 安装、升级、删除 python 包。使用 pip 进行包安装时，pip 默认会从 
<https://pypi.org/> 中寻找对应名字的包进行安装。 

## 常用指令

安装：

> `>>> pip install package-name`  (不带版本号，默认安装最新版本)
> 
> `>>> pip install package-name==x.x.x`  (== 后加版本号)
> 
> `>>> pip install --upgrade package-name`   (升级至最新版本)
>
> `>>> pip uninstall package-name`  (卸载)

相关信息显示：

> `>>> pip show package-name`  (显示包的相关信息)
>  
> `>>> pip list`  (显示所有已经安装的包, 'package-name (x.x.x)')
> 
> `>>> pip freeze > requirements.txt` 
> (将当前环境中安装了的包输出到文件中，显示格式为：'package-name==x.x.x', 
> 此外，系统中默认带的包不会输出到文件中)
> 
> `>>> pip install -r requirements.txt`  (上一步中输出的依赖包文件可以通过该指令安装)

更多 pip options 参考: <https://docs.python.org/3.8/installing/index.html#installing-index>

# 其他资源

python 语言细节介绍：<https://docs.python.org/3.8/reference/index.html#reference-index>

python 标准库的详细介绍：<https://docs.python.org/3.8/library/index.html#library-index>

