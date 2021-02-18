if __name__ == '__main__':
    '''
    link: https://docs.python.org/3.8/tutorial/controlflow.html
    python 中的流程控制语句：
        - if: if- elif -else 。 
        - for: for xx in xx, range() 场合 for 配合使用，规定一个范围， e.g. for i in range(10) 。 
        - while。
        - 与 for 和 while 搭配使用的 else：当 for 和 while 正常结束时，会执行 else 语句，而若 for 和 while 被 break 结束，
        则不会执行else中语句。
           
    '''

    # if 语句的使用
    x = 10
    # x = int(input("please input a integer: "))
    if x < 0:
        print('Negative')
    elif x == 0:    # "elif" is short for "else if"
        print('zero')
    else:
        print('Positive')

    # for语句
    words = ['Dog', 'Cat', 'Mouse']
    for w in words:
        print(w, len(w))
    # 如果在循环时需要修改 序列中的元素，建议在 序列的 copy 上进行 for 循环
    for w in words.copy():
        if w == 'Dog':
            words.remove(w)
    print(words)   # 遍历列表时删除元素

    # range() 函数，产生一连串的连续的数字
    for i in range(5, 10):
        print(i)
    for i in range(len(words)):
        print(i, words[i])      # 配合使用 range 和 len 函数，使用位号进行遍历
    print(list(enumerate(words)))  # 或者可以使用 enumerate 函数， 输出：[(0, 'Cat'), (1, 'Mouse')]
    # 需要注意的是，如果直接 print(range(0,10)), 会输出 `range(0,10)`
    print(range(0,10))  # 这是因为 range 本质上不是一个 list，它是这样一个对象，当你遍历它时永远可以返回下一个值
    a = sum(range(0, 10))       # 对于迭代求和的 sum 函数，可以直接传入 range()
    print('Summation of 0 to 10 is: ', a)
    print(list(range(4)))

    # break 和 continue，和 else 子句.
    # 在 python 中， else 可以还可以和 for 及 while 结合使用，当 for 或 while 正常结束时，会执行 else 中语句，
    # 而当 while 和 for 被 break 结束时，不会执行 else 中的内容。
    # 与 for 和 while 结合使用时， else 更像是 try 语句 -- 如果 将 break 看做是异常的话。
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:  # 如果 n 不能被小于它的任何数整除，说明 n 是个 prime number
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is prime number.')

    # pass 语句，不执行任何内容。用于系统中需要一个语句，但是并不需要执行内容的情况。例如：
    # while True:
        # pass