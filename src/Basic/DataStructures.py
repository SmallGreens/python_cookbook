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

    # tmp: stop at 5.1.1 Using Lists as Stacks
