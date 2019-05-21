#################################Python中下划线的使用############################
"""
python中下划线主要使用于以下场景
1. 表示没用的变量
2. 表示私有变量
3. 前后双下划线————类的魔术方法
"""

###################################表示没用的变量################################
"""
两个元素，如果只需要用一个元素，另一个元素最好用_表示，说明这个元素不会被使用，增加代码可读性

例1：
    如果只使用索引,元素不使用,正常是这样:
        l = ['a', 'b', 'c']
        for i, j in enumerate(l):print(i)
    j不使用最好不要命名为j,而是用_代替:
        for i, _ in enumerate(l):print(i)
例2：
    a = [1, 2, 3, 4]
    _, *b, _ = a
    print(b)         # [2, 3]

例3：
    a, _ = 'abc,mn'.split(',')
    print(a)         # abc
"""

###################################表示私有变量###################################
"""
在类中带有_或者__前缀的函数（属性也是）是私有的，最好只在类中其他函数里面调用，不要让实例直接调用。
_与__的差别在于，_前缀的最好不要调用，但是想调用也没什么问题，而__前缀的则不能调用。

class Demo(object):

    def __init__(self, name, phone,pwd):
        self.name = name
        self._phone = phone
        self.__pwd = pwd

    def _walk(self):
        print("walking test")

    def __sleep(self):
        print("sleeping test")

    def run(self):
        print("name is {name} phone is {phone}, pwd is {pwd}".format(name=self.name, phone=self._phone, pwd=self.__pwd))
        self._walk()
        self.__sleep()

obj = Demo("jerd", 1346677, "jerd@1346677")
print(obj.name, obj._phone)             # jerd 1346677

obj._walk()           # walking test

# 实例不能直接调用私有属性
    print(obj.__pwd)                         # AttributeError: 'Demo' object has no attribute '__pwd'
    obj.__sleep()                            # AttributeError: 'Demo' object has no attribute '__sleep'

# 在类中调用
    obj.run()
"""

###################################类的魔术方法###################################
"""
1.__enter__ 和 __exit__
    用于上下文管理 和with联合使用
    __enter__():在使用with语句时调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定
    __exit__():会话管理器在代码块执行完成后调用，在with语句完成时，对象销毁之前调用

    class Demo(object):

        def __init__(self, name, pwd):
            print("Go in here, execute __init__")
            self.name = name
            self.__pwd = pwd
    
        def run(self):
            print("Go in here, execute __run__")
    
            return self.name, self.__pwd
    
        def __enter__(self):
            '''
                使用with语句是调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定
            '''
            print("Go in here, execute __enter__")
            return self
    
        def __exit__(self, exc_type, exc_val, exc_tb):
            '''
                在上下文管理中运行的代码如果报错，会将三个值自动传入__exit__方法中，分别为 异常的类型，异常的值，异常的追踪栈
            '''
            print("Go in here, execute __exit__")
            if exc_type:
                print(exc_type, exc_val,)
            return None
            
    # 1.普通对象调用
        obj = Demo("jerd", "jerd@1346677")
        name, pwd = obj.run()
        print(name, pwd)
        
        result:
            Go in here, execute __init__
            Go in here, execute __run__
            jerd jerd@1346677
    # 2.使用with调用
        with  Demo("jerd", "jerd@1346677") as obj:
            name, pwd = obj.run()
            print(name, pwd)
        
        result:
            Go in here, execute __init__
            Go in here, execute __enter__
            Go in here, execute __run__
            jerd jerd@1346677
            Go in here, execute __exit__
    
    # 3.制造错误
        with  Demo("jerd", "jerd@1346677") as obj:
        name, pwd = obj.run()
        print(name, pwd)
        # 制造错误
        data = [1, 2, 3]
        data[4]
        
        result:
            Go in here, execute __init__
            Go in here, execute __enter__
            Go in here, execute __run__
            jerd jerd@1346677
            Go in here, execute __exit__
            <class 'IndexError'> list index out of range

2.__new__ __init__ __call__
    
    __new__创造一个对象。即实例化时为什么能实例化出来一个对象
    __init__ 用于定义实例属性
    __call__ 输入 实例() 或者 类()() 触发 只有定义了这个，实例才可以像函数一样执行
    实例化的实质：先执行__new__方法 创造出一个对象 然后把创造出来的对象传递给__init__方法
    
    class Demo(object):

        def __init__(self, name, pwd):
            print("Go in here, execute __init__")
            self.name = name
            self.__pwd = pwd
    
        def __new__(cls, *args, **kwargs):
            print("Go in here, execute __new__")
            return object.__new__(cls)
    
        def __call__(self, *args, **kwargs):
            print("Go in here, execute __call__")
            print(args)


    obj = Demo("jerd", "jerd@1346677")
    obj("this is a demo")
    
    result:
        Go in here, execute __new__
        Go in here, execute __init__
        Go in here, execute __call__
        ('this is a demo',)

3.__str__ __repr__  __len__ 
            
    __str__ print实例时打印出来的内容  返回值必须是字符串,否则抛出异常
    __repr__ 直接输出实例名打印出来的内容 返回值必须是字符串,否则抛出异常
    __len__ 定义 len(实例) 返回的内容
    
    __str__  和 __repr__的区别：
    1.__repr__是__str__的备胎。在不存在__str__的情况下会自动调用__repr__
    2.__str__ 的返回结果可读性强。也就是说，__str__ 的意义是得到便于人们阅读的信息
      __repr__ 的返回结果应更准确。怎么说，__repr__ 存在的目的在于调试，便于开发者使用。
      
    例：
        import datetime
        today = datetime.date.today()
        print(str(today))                       # 2019-05-21
        print(repr(today))                      # datetime.date(2019, 5, 21)
    
    
    class Demo(object):

        def __init__(self, name, pwd):
            print("Go in here, execute __init__")
            self.name = name
            self.__pwd = pwd
    
        def __str__(self):
            print("Go in here, execute __str__")
            return self.name
    
        def __repr__(self):
            print("Go in here, execute __repr__")
            return self.__pwd
    
    
        def __len__(self):
            '''定义len函数返回的结果'''
            print("Go in here, execute __len__")
            return len(self.name)
    
    obj = Demo("jerd", "jerd@1346677")
    print(obj)
    # 未定义 __str__时 返回的结果是：
        Go in here, execute __init__
        <__main__.Demo object at 0x000001E5D7E5FE80>
    
    #定义__str__ 时 返回的结果是：
        Go in here, execute __init__
        Go in here, execute __str__
        jerd

4.__del__
    当删除一个对象时，Python解释器也会默认调用一个方法，这个方法为__del__()方法
    不管是手动调用del还是由Python自动回收都会触发__del__方法执行

    当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，那么此时只会让这个引用计数减1，即变为2，
    当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

    del xxx 不会主动调用__del__方法，只有引用计数 == 0时，__del__()才会被执行，并且定义了__del_()的实例无法
    被Python的循环垃圾收集器收集，所以尽量不要自定义__del__()。一般情况下，__del__() 不会破坏垃圾处理器。

    class Demo(object):

        def __init__(self, name, pwd):
            print("Go in here, execute __init__")
            self.name = name
            self.__pwd = pwd

        def __del__(self):
            print('The python interpreter begins to recycle objects: %s'%self.name)

    #1.Python解释器释放实例对象的时候，调用该对象的__del__方法
        obj = Demo("jerd", "jerd@1346677")
        print('----------')

        result:
            Go in here, execute __init__
            ----------
            The python interpreter begins to recycle objects: jerd
    # 2.当使用del 把内存的所有应用删除，立刻调用__del__方法
        obj = Demo("jerd", "jerd@1346677")
        obj_1 = obj

        del obj
        del obj_1
        print('-----------------------')

        result:
             把内存中所有的引用都删除了 才执行__del__
            Go in here, execute __init__
            The python interpreter begins to recycle objects: jerd
            -----------------------

    # 3.
        obj = Demo("jerd", "jerd@1346677")
        obj_1 = obj

        del obj
        print("=====")
        del obj_1
        print('-----------------------')

        result:
            Go in here, execute __init__
            =====
            The python interpreter begins to recycle objects: jerd
            -----------------------
    # 4.
        obj = Demo("jerd", "jerd@1346677")
        obj_1 = Demo("zhao", "zhao@1346677")
        del obj
        print("=====")
        del obj_1
        print('-----------------------')

        result:
            Go in here, execute __init__
            Go in here, execute __init__
            The python interpreter begins to recycle objects: jerd
            =====
            The python interpreter begins to recycle objects: zhao

    #5.
        class Animal(object):

            def __init__(self, name):
                print('__init__方法被调用')
                self.__name = name
            # 析构方法
            # 当对象被删除时，会自动被调用
            def __del__(self):
                print("__del__方法被调用")
                print("%s对象马上被干掉了..."%self.__name)
        # 创建对象
        dog = Animal("金毛")
        # 删除对象
        del dog
        cat = Animal("波斯猫")
        cat2 = cat
        cat3 = cat
        print("---马上 删除cat对象")
        del cat
        print("---马上 删除cat2对象")
        del cat2
        print("---马上 删除cat3对象")
        del cat3
        print("=============")

    result:
            __init__方法被调用
            __del__方法被调用
            金毛对象马上被干掉了...
            __init__方法被调用
            ---马上 删除cat对象
            ---马上 删除cat2对象
            ---马上 删除cat3对象
            __del__方法被调用
            波斯猫对象马上被干掉了...
            =============

5.__getattr__ __setasttr__  __getitem__ __setitem__

    __getattr__ 调用的属性不存在时，会执行getattr
    __setattr__ 当试图对象的item特性赋值的时候将会被调用

    __item__系列 操作a['name']这种形式 先进行初始化，然后执行__getitem__
     __getitem__ 调用属性会执行__getitem__

    class Demo():

        def run(self):
            print("=====")

        def __init__(self,name):
            print('__init__方法被调用')
            self.name=name

        def __getattr__(self,item):
            print('__getattr__方法被调用')
            return item


    # 未定义__getattr__  __getitem__方法
        obj = Demo("jerd")
        print(obj.age)     #AttributeError: 'Demo' object has no attribute 'age'

    # 定义__grtattr__方法
        __init__方法被调用
        __getattr__方法被调用
        age

    class Student:

        hobby = "basket"
        def __init__(self):
            print('__init__方法被调用')
            self.sex = "woman"
        def __getattr__(self, item):
            print('__getattr__方法被调用')
            return item + ' is not exits ---'

        def __setattr__(self, key, value):
            print('__setattr__方法被调用')
            self.__dict__[key] = value

        def __getitem__(self, item):
            print('__getitem__方法被调用')
            return self.__dict__[item]

        def __setitem__(self, key, value):
            print('__setitem__方法被调用')
            self.__dict__[key] = value
    # attr 操作
        s = Student()
        print(s.hobby)              # basket
        print(s.name)               # __getattr__方法被调用 name is not exits ---
        s.age = 11                  # __setattr__方法被调用
        print(s.age)                # 11

    # item 操作
        print(s['age'])            # __getitem__方法被调用 11
        #print(s['hobby'])         # __getitem__方法被调用  KeyError: 'hobby'
        print(s['sex'])            # __getitem__方法被调用 woman

        s['age'] = 12              # __setitem__方法被调用
        print(s['age'])            #__getitem__方法被调用 12
    
    
"""













