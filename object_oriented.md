# Python中下划线的使用
    python中下划线主要使用于以下场景
    1. 表示没用的变量
    2. 表示私有变量
    3. 前后双下划线————类的魔术方法


## 表示没用的变量
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


## 表示私有变量

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

### 实例不能直接调用私有属性
    print(obj.__pwd)                         # AttributeError: 'Demo' object has no attribute '__pwd'
    obj.__sleep()                            # AttributeError: 'Demo' object has no attribute '__sleep'

### 在类中调用
    obj.run()


# 类的魔术方法
### 1.__enter__ 和 __exit__
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
            
#### 1.普通对象调用
        obj = Demo("jerd", "jerd@1346677")
        name, pwd = obj.run()
        print(name, pwd)
        
        result:
            Go in here, execute __init__
            Go in here, execute __run__
            jerd jerd@1346677
#### 2.使用with调用
        with  Demo("jerd", "jerd@1346677") as obj:
            name, pwd = obj.run()
            print(name, pwd)
        
        result:
            Go in here, execute __init__
            Go in here, execute __enter__
            Go in here, execute __run__
            jerd jerd@1346677
            Go in here, execute __exit__
    
#### 3.制造错误
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

### 2.__new__ __init__ __call__
    
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

### 3.__str__ __repr__  __len__ 
            
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

### 4.__del__
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

#### 1.Python解释器释放实例对象的时候，调用该对象的__del__方法
        obj = Demo("jerd", "jerd@1346677")
        print('----------')

        result:
            Go in here, execute __init__
            ----------
            The python interpreter begins to recycle objects: jerd
#### 2.当使用del 把内存的所有应用删除，立刻调用__del__方法
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

#### 3.
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
#### 4.
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

####5.
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

### 5.__getattr__ __setasttr__  __getitem__ __setitem__

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
#### attr 操作
        s = Student()
        print(s.hobby)              # basket
        print(s.name)               # __getattr__方法被调用 name is not exits ---
        s.age = 11                  # __setattr__方法被调用
        print(s.age)                # 11

#### item 操作
        print(s['age'])            # __getitem__方法被调用 11
        #print(s['hobby'])         # __getitem__方法被调用  KeyError: 'hobby'
        print(s['sex'])            # __getitem__方法被调用 woman

        s['age'] = 12              # __setitem__方法被调用
        print(s['age'])            #__getitem__方法被调用 12
    
    

# property classmethod staticmethod
    1.property(属性方法)：           将一个方法伪装成属性。在使用用对象属性的方式调用,只能对象调用
    2.classmethod（类方法):          将一个普通方法装饰为一个类方法.操作只能和类中的静态变量相关
    3.staticmethod（静态方法):       将一个方法装饰成普通函数。在类中装饰一个不需要self参数 也不需要cls参数的函数

    class Circle:
    
        discount = 0.8
        def __init__(self, r):
            self.r = r
    
        @property
        def area(self):
            print('-- property --')
            return self.r ** 2
    
        @classmethod
        def change_discount(cls, new_discount):
            print('-- classmethod --')
            cls.discount = new_discount
            cls.r = new_discount * 10
        @staticmethod
        def get(a, b, c):
            print('-- staticmethod --')
            return a, b, c


### 属性方法：只有实例对象能调用
    c = Circle(5)
    print(c.area)                             # -- property --  25
### 类方法
    1.被装饰之后,方法默认接收一个 类 作为参数
    2.之后所有的操作都只能和类中的静态变量相关 而不应该和对象相关
    3.类和对象都可以直接调用类方法

    类调用
        print(Circle.discount)                    # 0.8
        Circle.change_discount(0.9)               # -- classmethod --
        print(Circle.discount)                    # 0.9
    对象调用
        c = Circle(10)
        print(c.discount, c.r)                      #0.8 10
        c.change_discount(0.9)                      # -- classmethod --
        print(c.discount, c.r)                      # 0.9 10
        print(Circle.r)                             #9.0

### 静态方法:类和对象都可以直接调用
    类调用
        print(Circle.get(5, 10, 15))                  #-- staticmethod -- (5, 10, 15)
    对象调用
        print(Circle(10).get(20,20,20))               #-- staticmethod --  (20, 20, 20)


### @property 方法来实现 setter 和 getter
    1.不应该在某属性的 getter 方法里面修改其他属性的值
    2.如果访问对象的某个属性时，需要表现出特殊的行为，那就用 @property 来定义这种行为
    3.@property 方法需要执行得迅速一些，缓慢或复杂的工作，应该放在普通的方法里面。

    class Demo(object):
        def __init__(self,):
            self.__voltage = 0

        @property
        def voltage(self):
            print("-----")
            return self.__voltage

        @voltage.setter
        def voltage(self,voltage):
            print("======")
            self.__voltage = voltage

    obj = Demo()
    print(obj.voltage)

    result:
        -----
        0

    # 设置 voltage 属性时，将会执行名为 voltage 的 setter 方法
    obj.voltage = 10
    print(obj.voltage)

    result:
        ======
        -----
        10



# 反射：hasattr() getattr() 

    hasattr  判断某一个 变量 是否能够.调用一个名字,返回True或者False
    getattr  直接获取一个变量中的名字的值
    
    
    
    class Goods:
        discount = 0.8
        def __init__(self,name,price):
            self.name = name
            self.price = price
        def post(self):
            return "这是post请求"
        @property
        def get(self):
            return "这是属性方法"
        @classmethod
        def change_discount(cls,new_dis):
            cls.discount = new_dis
            return "这是类方法"
        @staticmethod
        def login(a, b, c):
            return "这是个静态方法"

### hasattr
    print(hasattr(Goods, "discount"))       True
    print(hasattr(Goods, "post"))           True
    print(hasattr(Goods, "login"))          True
    print(hasattr(Goods, "show"))           False

    值=getattr（类名,字符串类型的属性名） 如果第二个参数是不存在的属性名则会报错
        getattr(Goods, "discount")           #0.8
        #getattr(Goods, "show")             #AttributeError: type object 'Goods' has no attribute 'show'
        getattr(Goods, "show", None)        自定义值，如果不存在就返回默认值 None


### 1.反射类中的名字
    getattr(类名,'类属性')
    getattr(类名,'类方法名')()
    getattr(类名,'静态方法名')()
    getattr(类名,'对象方法名')(self)
    
    1.反射类属性
        ret=getattr(Goods,"discount")
        print(ret)                      #   0.8
    
    2.反射类方法
        ret=getattr(Goods,"change_discount")
        ret = getattr(Goods, "change_discount")
        print(ret)      # <bound method Goods.change_discount of <class '__main__.Goods'>> 
        print(ret(10))  # 这是类方法
        
    3.反射静态方法   
        ret=getattr(Goods,"login")
        print(ret(1,2,3)) #这是个静态方法 
    
    4.反射对象方法，参数为类名或者类的对象
        ret=getattr(Goods,"post")
        print(ret(Goods))           #这是post请求
        obj=Goods("jerd",20)
        print(ret(obj))             #这是post请求

### 2.反射对象中的名字
    getattr(对象名,'类属性')
    getattr(对象名,'对象属性')
    getattr(对象名,'对象方法名')()
    getattr(对象名,'属性方法名')
    getattr(对象名,'类方法名')()
    getattr(对象名,'静态方法名')()
    
    obj=Goods("jerd",20)
    
    1.反射类属性
        ret=getattr(obj,"discount")     #ret=obj.discount
        print(ret) # 0.8
    
    2.反射对象属性
        ret=getattr(obj,"name")         #ret=obj.name
        print(ret) #jerd
    
    3.反射对象方法
        ret=getattr(obj,"post")         #ret=obj.post
        print(ret())                    #这是post请求
    
    4.反射属性方法
         ret=getattr(obj,"get")         #ret=obj.get
         print(ret)                     #这是属性方法
    
    5.反射类方法
        ret=getattr(obj,"change_discount")  #ret=obj.change_discount
        print(ret(2))                       #这是类方法
    
    6.反射静态方法
        ret=getattr(obj,"login")                #ret=obj.login
        print(ret(1,2,3))                       #这是个静态方法

### 3.模块中反射
    import 模块名
    getattr(模块名,'模块中的变量')
    getattr(模块名,'模块中的函数')()
    getattr(模块名,'模块中的类名')
    
### 4.反射当前模块中的名字
    import sys
    getattr(sys.modules[__name__],'变量')
    getattr(sys.modules[__name__],'函数')()
    getattr(sys.modules[__name__],'类名')
    
    Demo = getattr(sys.modules[__name__],"Goods")
    Demo("jerd",20).get()


# __name__ 和 __main__ 

    使用sys.modules["__main__"]时，如果在另一个文件中导入了当前文件，执行另一个文件会显示另一个文件名的名字
    使用sys.modules[__name__]时， 在另一个文件中会显示当前文件的名字
    
    practice.py
        import sys
        count=0
        sum=100
        def post():
            return "这是post请求"
        class A():
            def get(self):
                print("这是practice文件")
        print(sys.modules["__main__"])
    
    practice1.py
        
        import practice
        import sys
        count=1
        class A():
            def get(self):
                print("这是practice1文件")
                
### 测试           
    1.执行practice.py  
        <module '__main__' from 'E:/lianxi/practice.py'>
    2.执行practice1.py 
        <module '__main__' from 'E:/lianxi/practice1.py'> 显示当前文件名
    3.将practice.py中print(sys.modules["__main__"])换成print(sys.modules[__name__])
        执行practice.py  #<module '__main__' from 'E:/lianxi/practice.py'>
        执行practice1.py #<module 'practice' from 'E:\\lianxi\\practice.py'> #显示导入的文件名
    4.
        执行practice.py：
            print(getattr(sys.modules['__main__'],"count")) #0
            print(getattr(sys.modules[__name__],"count"))  #0
        执行practice1.py
            若practice.py中为 print(getattr(sys.modules[__name__],"count")) 则显示1
            若practice.py中为 print(getattr(sys.modules['__main__'],"count")) 则显示：
                AttributeError: module '__main__' has no attribute 'count'
            原因是count定义在了import practice之后，将count定义在import practice前面 结果为1
    
    if __name__ == '__main__': 的作用
        让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行
        相当于程序的入口，某个文件被导入时候，如果用了这个if就可以避免没被封装的语句被执行


# Python描述符 (descriptor)

## 属性：__dict__
    作用：字典类型，存放本对象的属性，key(键)即为属性名，value(值)即为属性的值，形式为{attr_key : attr_value}

        对象属性的访问顺序：
        
        ①.实例属性
        
        ②.类属性
        
        ③.父类属性
        
        ④.__getattr__()方法

    class Goods:
        discount = 0.8
        _total = 100
        __remain = 100
    
        def __init__(self,name,price,purchase_price):
            self.name = name
            self.price = price
            self.__purchase_price = purchase_price
        def __account(self):
            return "这是私有方法 内部访问"
        def _deal(self):
            return "这是私有方法 内部/外部访问"
        def post(self):
            return "这是post请求"
        @property
        def get(self):
            return "这是属性方法"
        @classmethod
        def change_discount(cls,new_dis):
            cls.discount = new_dis
            return "这是类方法"
        @staticmethod
        def login(a, b, c):
            return "这是个静态方法"
        
### 当前类有的属性：
    print(Goods.__dict__)  
    {
        '__module__': '__main__',
        'discount': 0.8,
        '_total': 100,
        '_Goods__remain': 100,
        '__init__': < function Goods.__init__ at 0x00000000021C8A60 > ,
        '_Goods__account': < function Goods.__account at 0x00000000021C8B70 > ,
        '_deal': < function Goods._deal at 0x00000000021C8AE8 > ,
        'post': < function Goods.post at 0x00000000021C8BF8 > ,
        'get': < property object at 0x0000000000419598 > ,
        'change_discount': < classmethod object at 0x00000000021C79B0 > ,
        'login': < staticmethod object at 0x00000000021C79E8 > ,
        '__dict__': < attribute '__dict__' of 'Goods'objects > ,
        '__weakref__': < attribute '__weakref__' of 'Goods' objects > ,
        '__doc__': None
    }
    
### 实例对象有的属性：
    obj = Goods("phone", 800, 500)
    print(obj.__dict__)
    
    {
        'name': 'phone',
        'price': 800,
        '_Goods__purchase_price': 500
    }
    
### 类的属性和实例的属性互补干涉：
    1.更改实例obj的属性discount，只是新增了该属性，并不影响类Test的属性cls_val
        obj.discount = 0.7 
        print(obj.__dict__)
        
        {
            'name': 'phone',
            'price': 800,
            '_Goods__purchase_price': 500,
            'discount': 0.7
        }
    
    
    2.更改了类Goods的属性discount的值，由于事先增加了实例obj的discount属性，因此不会改变实例的discount值
        Goods.discount = 0.9
        print(Goods.__dict__)
        print(obj.__dict__)
        
        {'__module__': '__main__', 'discount': 0.9  .....} 
        {'name': 'phone', 'price': 800, '_Goods__purchase_price': 500, 'discount': 0.7}


## 描述符：
    某个类，只要是内部定义了方法 __get__, __set__, __delete__ 中的一个或多个，就可以称为描述符    
    
### 1.数据描述符:定义的描述符有__get__和__set__2个方法
        class RevealAccess(object):
    
            def __init__(self, initval=None, name='var'):
                print('__ revealAccess__ init')
                self.val = initval
                self.name = name
        
        
            def __get__(self, obj, objtype):
                print("__get__...")
                print('name = ', self.name)
                print('=' * 40, "\n")
                return self.val
        
            def __set__(self, obj, val):
                print("__set__...")
                print('name = ', self.name)
                self.val = val
                
        1.# 描述符的对象定义为类属性
            class MyClass(object):
                x = RevealAccess(10, 'jerd')
                y = 5
            
            print(MyClass.x)
            
            result:
                __ revealAccess__ init
                __get__...
                name =  jerd
                ======================================== 
                10
                
                内部执行流程：
                    解析器发现x是一个描述符的话，其实在内部是通过type.__getattribute__()，它能把MyClass.x转换为MyClass.__dict__[“x”].__get__(None,MyClass)来访问。
                    
                    描述符作为属性访问是被自动调用的。
                    对于类属性描述符对象，使用type.__getattribute__，它能把Class.x转换成Class.__dict__[‘x’].__get__(None, Class)。
                    对于实例属性描述符对象，使用object.__getattribute__，它能把object.x转换为type(object).__dict__[‘x’].__get__(object, type(object))
                    最好定义描述符对象为类属性
                    
        2.# 描述符定义成对象属性
            class MyClass(object):
                x = RevealAccess(10, 'jerd')
                def __init__(self):
                    print("---MyClass init ----")
                    self.y = RevealAccess(11, 'zhao')
        
            test = MyClass()
            print(test.y)
        
            result:
                __ revealAccess__ init
                ---MyClass init ----
                __ revealAccess__ init
                <__main__.RevealAccess object at 0x0000000001E97A20>
                
                当访问一个实例描述符对象时，object.__getattribute__会将test.y转换为type(test).__dict__[‘y’].__get__(test,type(test))。
                而MyClass类中没有“y”属性，所以无法访调用到_get__方法，但这个实例对象仍然是一个描述符对象
        3.# 当定义的类属性描述符对象和实例属性有相同的名字时
        class MyClass(object):
            x = RevealAccess(10, 'zhao')
            def __init__(self, x):
                print("---MyClass init ----")
                self.x = x

        test = MyClass(100)
        print(test.x)
        
        result:
            __ revealAccess__ init
            ---MyClass init ----
            __set__...
            name =  zhao
            __get__...
            name =  zhao
            ======================================== 
            100
        
            test = MyClass(100)
            print(test.__dict__)
            print(MyClass.__dict__)
            
            当python发现实例对象的字典中有与定义的描述符有相同名字的对象时，描述符优先，会覆盖掉实例属性。python会改写默认的行为，去调用描述符的方法来代替
            实例对象的字典中根本就没有x对象，即使我们在类中定义了self.x。而类的字典中则有x描述符对象。这主要就是因为描述符优先
    
### 2.非数据描述符不会覆盖掉实例属性。而且优先级比实例属性低
        class RevealAccess(object):
        
                def __init__(self, initval=None, name='var'):
                    print('__ revealAccess__ init:',name)
                    self.val = initval
                    self.name = name
            
            
                def __get__(self, obj, objtype):
                    print("__get__...")
                    print('name = ', self.name)
                    print('=' * 40, "\n")
                    return self.val

        

        class MyClass(object):
            x = RevealAccess(10, 'zhao')
            def __init__(self, x):
                print("---MyClass init ----")
                self.x = x
        
        test = MyClass(100)
        print(test.x)
        print("------------------------------")
        print(test.__dict__)
        print("===============================")
        print(MyClass.__dict__)
        print("-------------------++++++++++++")
        print(MyClass.x)
        
        result:
            __ revealAccess__ init: zhao
            ---MyClass init ----
            100
            ------------------------------
            {'x': 100}
            ===============================
            {'__module__': '__main__', 'x': <__main__.RevealAccess object at 0x00000000028F7438>,....}
            -------------------++++++++++++
            __get__...
            name =  zhao
            ======================================== 
            10












