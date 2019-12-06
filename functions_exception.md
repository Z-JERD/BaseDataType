# 生成式

### List生成式：
    
    1.列表推导+条件判断
        li = [i for i in range(50) if i % 5 == 0]
    2.列表推导+三目运算   
        li = [ i if i % 5 == 0 else 1 for i in range(1,10) ]
    
    3.嵌套for语句
        data = [["jerrd", "jerd"], [12, 13, 14]]
        li = [ value for array in data for value in array]

### Dict生成式：
    1.交换字典的键和值
        a_dict = {"a": 1, "b": 2, "c": 3}

       { value : key  for key, value in a_dict.items() }

    2.大小写Key值合并
        mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

        case = { key.lower() : mcase.get(key.lower(),0) + mcase.get(key.upper(),0) for key in mcase.keys() }

### Set推导式：
    计算列表中每个值的平方，自带去重功能
    s1 = { x**2 for x in [1, -1, 2] }
    
### 生成器推导式
    li = ( i for i in range(50) if i % 5 == 0 )


### 将li转换转换成如下格式
    将li 转换成
        {
            '北京市': [
                        {'name': '北京市', 'area': '东城区'}, 
                        {'name': '北京市', 'area': '西城区'}, 
                        {'name': '北京市', 'area': '朝阳区'}, 
                        {'name': '北京市', 'area': '海淀区'}
                    ], 
            '上海市': [
                        {'name': '上海市', 'area': '浦东新区'}, 
                        {'name': '上海市', 'area': '普陀区'}
                    ]
        }
    
    
    data = {}
    li = [
        {"name": "北京市", "area": "东城区"},
        {"name": "北京市", "area": "西城区"},
        {"name": "北京市", "area": "朝阳区"},
        {"name": "北京市", "area": "海淀区"},
        {"name": "上海市", "area": "浦东新区"},
        {"name": "上海市", "area": "普陀区"},
    ]
    
    for bo in li:
        mbo = data.pop(bo['name'], [])
        mbo.append(bo)
        data[bo['name']] = mbo
    
    

### 将list3中的内容以list4中的内容显示出来
    list3 = [
        {"name": "北京市", "area": "东城区"},
        {"name": "北京市", "area": "西城区"},
        {"name": "北京市", "area": "朝阳区"},
        {"name": "北京市", "area": "海淀区"},
        {"name": "上海市", "area": "浦东新区"},
        {"name": "上海市", "area": "普陀区"},
    ]
    
    list4 = [
        {"name": "北京市", "area_list": ["东城区", "西城区", "朝阳区", "海淀区"]},
        {"name": "上海市", "area_list": ["浦东新区", "普陀区"]},
    ]
    
    result = []
    for message in list3:
        for new_message in result:
            if new_message['name'] == message['name']:
                new_message.setdefault('area',[]).append(message[ 'area'])
                break
        else:
            dic = {}
            dic['name'] = message['name']
            dic[ 'area'] = [message[ 'area']]
            result.append(dic)


# 常用内置函数
    map filter zip 返回的是迭代器   sort对原列表进行排序  sorted 返回的是新的列表

### 1.max 和 min
    1.默认参数key为None
        li = [1, 5, 10, 20]
        print(max(li), min(li)
    
    2.自定义key
        dic={3:20,2:100,5:30}
        1.以Key值比较，取出最大值      max(dic.items(),key=lambda x: x )    #(5, 100)
        2.以Value值比较，取出最大值    max(dic.items(),key=lambda  x : x[1])
        
### 2.zip()拉链方法。可将两个可迭代对象进行匹配
    可以放置多个可迭代对象,以最少的可迭代对象的个数为基准,返回一个迭代器
    1.可迭代对象长度一致
        li=["name","age"]
        li1=["jerd",18]
        print(dict(zip(li,li1)))
        
    2.可迭代对象长度不一致
    
        li=["name","age","hobby"]
        li1=["jerd",18]
        print(dict(zip(li,li1)))
        
    3.多个迭代对象进行匹配时
        li=["name","age","high"]
        li1=["jerd",18,"hobby"]
        li2=["xdd","book","play"]
        print(list(zip(li,li1,li2)))
        
### 3.map(func, *iterables)) 可迭代对象的元素，一个一个传给函数
    1.list(map(lambda x : x**2 ,[1,2,3]))
    2.list(map(lambda x,y:x + y,[1,2,3,7],[4,5,6]))  [5, 7, 9]
    
### 4.filter(function or None, iterable)过滤,取出符合条件的元素
    list(filter(lambda x : x %2==0,[0,1,2,4]))
    
### 5.sorted() 会形成新的列表，排序必须是列表
    li = ['fsdafsa','fddsaf','qqq','fgasjdlg;dsjfg']
    li2 = sorted(li,key=lambda x: len(x)
    li.sort(key=func)
    print(li, li2) 
    
    将dic中的内容以value值进行降序
        dic = {'math':90, 'chinese':99, 'english':66, 'history': 88, 'political':89,}
        new_dic = dict(sorted(dic.items(),key=lambda x : x[1], reverse=True))

    所有排序方法中，sorted的效率是最高的。它使用c代码编写的

### 6.reduce
    reduce()传入的函数 f 必须接收两个参数,reduce()对list的每个元素反复调用函数f，并返回最终结果值。
    Python3中,reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 fucntools 模块里
    from functools import reduce
    例:编写一个f函数，接收x和y，返回x和y的和：
        res = reduce(lambda x, y : x + y, [1, 3, 5, 7, 9])
        等同于：sum([1, 3, 5, 7, 9])
        
        计算过程：
            先计算头两个元素：f(1, 3)，结果为4；
            再把结果和第3个元素计算：f(4, 5)，结果为9；
            再把结果和第4个元素计算：f(9, 7)，结果为16；
            再把结果和第5个元素计算：f(16, 9)，结果为25；
            由于没有更多的元素了，计算结束，返回结果25。
### 
    1.tu1=(('a'),('b')),tu2=(('c'),('d')) 生成列表[{'a':'c'},{'b':'d'}]
        list(map(lambda x, y : {x : y},tu1,tu2))
        
    2.tu1(('a',),('b',)),,tu2=(('c',),('d',)) 生成列表[{'a':'c'},{'b':'d'}]
        list(map(lambda x ,y : {x[0] : y[0]}, tu1, tu2))


# callable()函数用法
    检查一个对象是否是可调用的 对于函数, 方法, lambda 函数式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True

### 1.函数可调用
    def add(x, y):
        return x + y
    
    print(callable(add))            #True

### 2.类和类内的方法可调用, 类的实例不可调用
    class Demo(object):
    
        def get(self):
            return  True

    obj = Demo()
    print(callable(Demo))           #True
    print(callable(Demo.get))       #True
    print(callable(obj.get))        #True
    print(callable(obj))            #False

### 3.lambda表达式是可调用的
    f = lambda x,y : x + y
    print(f(2, 3))
    print(callable(f))              #True

### 4.整数，字符串，列表，元组，字典等等，都是不可调用
    print(callable(2))              #False
    print(callable('python'))       #False
    print(callable([1, 2, 3]))      #False
    print(callable({'a':1, 'b':2})) #False



# isinstance()函数

    判断一个对象是否是一个已知的类型，类似 type()
    语法：
        isinstance(object, classinfo)
        
        如果参数object是classinfo的实例，或者object是classinfo类的子类的一个实例， 返回True
        如果object不是一个给定类型的的对象， 则返回结果总是False

    isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系。
        
        isinstance() 会认为子类是一种父类类型，考虑继承关系
    
    type: 用于查看对象的数据类型
    isinstance：用于判断两个类型是否相同推荐使用 isinstance()。
    
    a = 2
    print(isinstance (a,int))               #True
    print(isinstance (a,str))               #False
    print(isinstance (a,(str,int,list)))    #True


    class A:
        pass
    
    
    class B(A):
        pass
    
    
    print(isinstance(A(), A))               #  True
    print(type(A()) == A )                  #  True
    print(isinstance(B(), A))               #  True
    print(type(B()) == A)                   #  False

## 获取变量名称
    var = "foo"
    现在我们需要得到变量var的名字，即"var"
    
    应用场景：
        name,address,age,gender = "jockfi","北京市", 18,"gentleman"
        我们希望基于它们创建一个字典person。一般可以这样实现：person = {}
            person["name"] = name
            person["address"] = address
            person["age"] = age
            person["gender"] = gender
        不足之处：一是变量的名字出现了重复；二是赋值语句(不管是=赋值还是:赋值)出现了重复。当变量数量越多时，重复情况就越多。
    
    
    import inspect
    
    name,address,age,gender = "jockfi","北京市", 18,"gentleman"
    person = {}
    
    def retrieve_name(var):
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]
    
    for i in [name, address, age, gender]:
        person[retrieve_name(i)[0]] = i
        
# 文件处理
## Python读取文件read() readline() readlines()的区别：
### 1. read()  一次性读取整个文件内容
     f = open(filename,'r')
     f.read()

    read(参数)：
        通过参数指定每次读取的大小长度,这样就避免了因为文件太大读取出问题

    一般小文件我们都采用read()，不确定大小就定个size

### 2.readline() 
    每次读取一行内容。内存不够时使用，一般不太用

### 3.readlines()  
    一次性读取整个文件内容，并按行返回到list
    如果文件太大 会造成MemoyError
    适合读取配置文件

### 4.with open
    with open(file_path, 'rb') as f:
        sha1Obj.update(f.read())

    with open(file_path, 'rb') as f:
        for line in f.readlines():
            print(line)

    在读取小文件时确实不会产生什么异常，但是一旦读取大文件，很容易会产生MemoryError

    with open(file_path, 'rb') as f:  采用每次读取一行的方式
        for line in f:
            print(line)

## 读取大文件：
### 1.分块读取：将大文件分割成若干小文件处理，处理完每个小文件后释放该部分内存。用iter 和 yield来实现
        def read_in_chunks(filePath, chunk_size=1024*1024):
            file_object = open(filePath)
            while True:
                chunk_data = file_object.read(chunk_size)
                if not chunk_data:
                    break
                yield chunk_data

        if __name__ == "__main__":
            filePath = './path/filename'
            for chunk in read_in_chunks(filePath):
                pass

### 2.With open()
        with语句打开和关闭文件，包括抛出一个内部块异常。for line in f文件对象f视为一个迭代器，会自动的采用缓冲IO和内存管理
            with open(file_path, 'r') as f:
                while True:
                    buf = f.read(1024)
                    if buf:
                        sha1Obj.update(buf)
                    else:
                        break

        with open()的优化：
            面对百万行的大型数据使用with open 是没有问题的，但是这里面参数的不同也会导致不同的效率。
            参数为”rb”时的效率是”r”的6倍。由此可知二进制读取依然是最快的模式。
            
# python内存监控工具
## 1. memory_profiler:按每行代码查看内存占用
        pip install -U memory_profiler

        from memory_profiler import profile
        @profile
        def my_func():
            a = [1] * (10 ** 3)
            b = [2] * (2 * 10 ** 2)
            del b
            return a

        if __name__ == '__main__':
            my_func()

## 2.guppy查看占用内存前十位变量
        直接打印出对应各种python类型（list、tuple、dict等）分别创建了多少对象，占用了多少内存
        pip install guppy

        from guppy import hpy
        mem = hpy()
        with open(file_path, 'r') as f:
                while True:
                    buf = f.read(1024)
                    if buf:
                        print(mem.heap())
                        sha1Obj.update(buf)
                    else:
                        break

# 异常处理

    def div(a, b):
        try:
            print(a / b)
    
        except ZeroDivisionError:
            # 发生异常则执行此处代码
            print("Error: b should not be 0 !!")
    
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            # 捕捉到了异常，但是又想重新引发它（传递异常），使用不带参数的raise语句即可
            raise
    
        else:
            # 没有异常则执行此处代码
            print('Run into else only when everything goes well')
    
        finally:
            # 不论是否发生异常，均会执行
            print('Always run into finally block.')

    python标准异常:http://www.runoob.com/python/python-exceptions.html
    
    1.except语句不是必须的，finally语句也不是必须的，但是二者必须要有一个，否则就没有try的意义了。
    
    2.except语句可以有多个，Python会按except语句的顺序依次匹配你指定的异常，如果异常已经处理就不会再进入后面的except语句。
    
    3.except语句可以以元组形式同时指定多个异常，参见实例代码。
    
    4.except语句后面如果不指定异常类型，则默认捕获所有异常
    
    5.如果要捕获异常后要重复抛出，请使用raise，后面不要带任何参数或信息。

    a = {
        'result':{
            'codes':23
        }
    }
    
    def active_throw():
        # 主动抛异常
    
        异常：
            Traceback (most recent call last):
          File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 184, in <module>
            active_throw()
          File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 182, in active_throw
            raise Exception('code值有误')
        Exception: code值有误
    
    
        if  a['result']['codes'] != 22:
            raise Exception('code值有误')

### active_throw()

    import traceback
    def throw_anomaly():
    
        异常：
            Traceback (most recent call last):
              File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 208, in <module>
                throw_anomaly()
              File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 203, in throw_anomaly
                codes = a['result']['code']
            KeyError: 'code'
    
        try:
            codes = a['result']['code']
        except Exception as e:
           raise

    def catch_exceptions():
    
        捕获异常：
            print(e)     'code'
    
        捕获异常后，查看详细的异常信息:
        traceback.format_exc()
              Traceback (most recent call last):
              File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 220, in catch_exceptions
                codes = a['result']['code']
            KeyError: 'code'
        捕获异常后，控制台显示详细的异常信息 traceback.print_exc()
    
    
        try:
            codes = a['result']['code']
        except Exception as e:
            print(e)
            ee = traceback.format_exc()
            #print(ee)
    
            traceback.print_exc()
    
        print('----')

### catch_exceptions()
    实例中某个属性不存在时，调用该属性会抛出异常。使用getattr处理
        class Demo():
            def __init__(self):
                self.name = 'jerd'
    
            def get(self):
                return 66
    
        obj = Demo()
    
            age = obj.age
            Traceback (most recent call last):
              File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 249, in <module>
                age = obj.age
            AttributeError: 'Demo' object has no attribute 'age'
    
        # 1.try捕获异常
        try:
            age = obj.age
        except AttributeError:
            age = 'default'
    
        # 2.getattr
        age1 = getattr(obj, 'age', 'default')
        print(age, age1)
# 参数类型校验
    import inspect
    import datetime

    def check(fn):
        def wrapper(*args,**kwargs):
            sig=inspect.signature(fn)
            params=sig.parameters
            values=list(params.values())
            for i,p in enumerate(args):
                if not isinstance(p,values[i].annotation):
                    assert False,'不符合条件的参数错误'
            for k,v in kwargs.items():
                if not isinstance(v,params[k].annotation):
                    assert False,'不符合条件的参数错误'
            return fn(*args,**kwargs)
        return wrapper
    @check
    def demo(a:int=None,b:bool=None,c:list=None,d:dict=None,e:datetime.datetime=None):
        print("========a:", a)
        print("========b:", b)
        print("========c:", c)
        print("========d:", d)
        print("========e:", e)

    demo(a=99,b=False, c=[1,2,3],d={"key":"test"},e=datetime.datetime.now())
