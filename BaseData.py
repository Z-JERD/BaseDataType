###################基本数据类型###################

"""
不可变数据类型：int bool string tuple 不管内存中有多少个引用，相同的对象只占用一块内存
可变数据类型：list dict set  两个内容完全一样的对象，其地址是不一样的
"""

######################None#########################

"""
None 是 Python 的一个特殊常量。它是一个空值。有着自己的数据类型（NoneType） None 与 False 不同。None 不是 0 。None 不是空字符串。
将 None 与任何非 None 的东西进行比较将总是返回 False
例：
    None == False #False
    None == 0 #False
    None == None #True

在 布尔类型上下文环境中， None 为假值，而 not None 为真值
    1.66 if  None else 77  #77
    2.66 if not None else 77 #66


"""

#####################Int###########################

"""
int：用于计算.取值范围32位和64位
Python 同时支持Integer［整型］和Floating Point［浮点型］数值. 通过是否有小数点来分辨它们。
检测值的类型：type()和isinstance()
    1.type(variate)接收单个变量值
    2.isinstance(variate,type)接收变量值和检测的类型 结果为True或False
    isinstance() 与 type() 区别：
        type不考虑继承关系,isinstance()考虑继承关系
        例1：
            a=2
            print(type(a)) #<class 'int'>
            isinstance (a,(str,int,list)) #True
        例2：继承关系判定
            class A:pass
            class B(A):pass
            isinstance(A(), A)    # returns True
            type(A()) == A        # returns True
            isinstance(B(), A)    # returns True
            type(B()) == A        # returns False

整数和浮点数之间的转换：int---float
    1.通过调用float() 函数，可以显示地将 int 强制转换为 float 
        float(2) #2.0
    2.调用 int() 将 float 强制转换为 int int() 将进行取整
        int(2.5) #2
        
常见数值运算：+ - *  / ** // % += -= *= //=
    1./ 执行浮点除法 返回一个 float 浮点数。 
    2. // 整数除法 如果结果为正数 朝向小数位取整
        当整数除以负数， // 运算符将结果朝着最近的整数“向上”四舍五入
        print(11 // 2，11 // -2)  #5 #-6
        如果分子或者分母是 float 结果为float
         print(11.0 // 2，11 // -2.0) #5.0 #-6.0
    3.** 运算符 计算幂   % 取整除之后的余数
"""

#####################Bool###########################

"""
bool：只有True和False
数据类型之间的转换
    int-->str  str(int)      没条件
    str-->int  int(str)      字符串必须由数字组成
    int-->bool  bool(int)    非0的转换成True 0转换为False
    bool-->int int(bool)     True转换成1  False转换为0
    str-->bool  bool(str)    非空的字符串转换成True 空的字符串转换成False 
    bool-->str  str(bool)    无实际意义
"""

#####################String#########################

"""
str：用引号引起来的都是字符串。存储少量数据，便于操作
1.  str的查找，利用索引，s[0]  s[-1] -1代表最后一个
     利用切片，顾首不顾尾  s[2:5]  s[0:]代表全部 s[0:-1] 从头到倒数第二个
     加步长  s[2:5：2]  如果是反向截取，步长必须是负的 s[5:2：-2] 
2.str的基本操作：原字符串不变  字符串常用的十二个功能
    1.s.captalise()      首字母大写,其他小写
    2.s.swapcase()       大小写翻转
    3.s.title()          非字母隔开的地方，首字母大写，其他小写
    4.s.upper()          全部变大写   
      s.lower()          全部变小写
    5.s.center()         居中，默认为空，可以自当义print(s.center(20，’*‘)) 
    6.s.strip()          默认删除两边空格键，换行符，tab键 
      s.lstrip()         删除左边  
      s.rstrip()         删除右边
      s.strip(“abc”)   删除两边自定义的元素
    7.s.startswith()     判断是否以什么开头，可以切片   print(s.startswith(“al”))
      s.endswith()       判断是否以什么结尾
   8. s.isalum()         判断是否由数字和字母组成
      s.isalpha()        判断是否由字母组成
      s.isdight()        判断是否由数字组成
   9. s.count('a')       统计某个元素的个数
   10.len(s)             统计字符串的长度
   ********
   11. print(s.replace())        替换，replace(old,new) 默认全部替代
                                replace(old,new,num) 自定义替换的个数
   12.print(s.find())            根据元素找索引号，找不到返回-1，只用在字符串中，可切片也可索引查 print(s.find("a",1,5)) 
                                如果有相同的元素，找到第一个的索引就停止，就不再寻找。用循环同时找索引，应用range
     print(s.index())           根据元素找索引号，找不到报错 ValueError，也可用在list和dict，tuple中
   13.print(s.split())          将str转换成list，默认全部分割 设置分割的个数 print(s.split('a'，1)
      print("_".join(s))        将list转换成str
   14. formate
        第一种用法，顺序不可更改
            msg="我叫：{} 我的年龄：{} 我的爱好：{}".formate('jerd',20,'basketball')
        第二种用法，顺序不可更改，可重复用
            msg="我叫：{0} 我的年龄：{1} 我的爱好：{2}".formate('jerd',20,'basketball')
        第三种用法，顺序可更改
            msg="我叫：{name} 我的年龄：{age} 我的爱好：{honny}".formate(name='jerd',age=20,hobby='basketball')

"""

#######################List#########################

"""
list 的增，删，改，查 共10种
lis=[1,2,'abc','a','b']

1.增 三种 insert append extend
    1.insert(2,'ab')        按照索引增加
    2.append("abc")         将元素添加到列表尾部
    3.extend("abc")         参数为可迭代对象,迭代增加

2.删 四种 pop remove clear del
    1. pop(2)               按照索引删除，默认删除最后一个元素。返回值为被删的元素
                            如果索引不存在 报错：IndexError
    2. remove("abc")        指定欲删除的元素
    3. clear()              清空列表
    4. del                  del lis 删除列表
                            del lis[0] 按照索引删除
                            del lis[0:2] 按照切片删除

3.改 
    1.按照索引改             li[1]=[12,13,14]  
    2.按照切片去改           lis[2：5]="jerd"  是迭代修改的
4.查:按照索引,切片查和for循环去查 
    1.用索引，原来是什么类型还是什么类型
    2.用切片查，输出结果为列表
    li=[1,2,"sd",[1,2,3],"sddw"]
    print(li[-1]) #sddw
    print(li[-1:]) #['sddw']
    print(li[0:2])  #[1, 2]
    
常用操作：
    1.len(li)               列表的长度
    2.li.count('a')         统计元素的个数
    3.li.index('a')         找到指定元素的索引
    4."".join(li)           list --> str
    5.li.sort()             对原列表进行排序，默认从小到大
                            li.sort(reverse=True) 从大到小
                            li.sort(key=func) 自定义排序的规则
    6.reverse()             倒序
    7.li1 + li2             列表的合并

list  在循环一个列表时，如果要删除某些或者某类元素，容易出错
    例：li=[1,2,3,4,'a','abc'] #把下标为奇数的元素给删掉
    方法1 利用切片
        del li[1::2]

    方法2 利用新建列表
        [ li[i] for i in range(len(li)) if i % 2 ==0 ]

    方法3 利用倒叙
        for i in range(len(li)-1,0,-1):
            if i % 2 ==1:
                del li[i]



"""

#######################Tuple########################

"""
元组tuple:只读列表，不可更改
和列表的区别就是用()表示即数据可以被查询，但不能被修改，所以，字符串的切片操作同样适用于元组
例：
    tu=(1,2,'c',['a',12,'abc',(1,2)],5,('a',12))
    元组的儿子不可以改变，但孙子可以改变，这个元组中，列表中的元素可以改变

tuple的性质：
    1.tuple   当元组只有一个元素组成并且没有','则该元素是什么数据类型,整体就是什么数据类型.
      tu = ()括号里的元素用逗号隔开时，tu数据类型才为元组
    tu=([1,2,3])     #假如tu1=([1,2,3])tu 和tu1的id也是不一样的。只有int和str有小数据池
    tu1=([1,2,3],)
    print(id(tu),type(tu),id(tu1),type(tu1))  #结果：1355023302728 <class 'list'> 1355021474168 <class 'tuple'>
    a=(1)   b=(1,2)   print(type(a),type(b))  #结果：<class 'int'> <class 'tuple'>
    tu=([1,2,3]) tu可添加元素（tu是列表）tu.append("a")
    tu1=([1,2,3],) tu1不可添加元素，tu1[0]可添加，tu1[0].append("a")
    
元组的好处:
    1.元组的速度比列表更快。使用的内存也更小。如果定义了一系列常量值，而所需做的仅是对它进行遍历，那么请使用元组替代列表。
    2.对不需要改变的数据进行“写保护”将使得代码更加安全。
    3.一些元组可用作字典键,列表永远不能当做字典键使用
        例：a = {(1,"key"):"jerd"})

"""

#######################Dict##########################

"""
字典是python中唯一的映射类型，采用键值对（"k":v)的形式存储数据字典是无序存储的
列表是有序的对象结合，字典是无序的对象集合。
dict中的key值是不可变数据类型，value是任意类型的
在3.5版本之前，字典是无序的，3.6和3.6之后的都是有序的 3.6改进的字典更节省内存

Dict的创建：
    1.  dic = {} 空字典
        dic={"a":1,"b":2}
    2.  dic=dict([("a",1),("b",2)]) #{'a': 1, 'b': 2}
    3.  dic=dict((("a",1),("b",2)))
      
Dict的增，删，改，查  共10种
    1. 增： key值和setdefault
        1. 根据key值去增，key存在就覆盖，不存在就就新建 
            dic[key]=value
        2. setdefault  若key存在就不变，不存在就新建。返回值为value值
            dic.setdefault(key) 默认添加None，{'name': None}
            dic.setdefault(key，value)
    2. 删:pop popitem clear deal
        1. pop  按照索引key值删除，有返回值，返回值为被删除对象的value值
            a = dic.pop(key)  key不存在就会报错 KeyError
            a = dic.pop(key,"此键不存在") 自定义可报错的内容
        2.del   按照key值删除，无返回值
            del dic[key]
        3.clear  清空字典
            dic.clear()
        4.popitem()  随机删除 有返回值，返回值为元祖(key,value)
            b = a.popitem()  

    3. 改:  key值和update
        1.根据key值去改，key存在就覆盖，不存在就就新建 
        2. update 参数为{}
                1.更新新值：
                    dic={'name': 'jerd', 'age': 20, 'sec': 'male'}
                    dic.update({"sex":"man"})
                2.更新已存在的值
                    dic={'name': 'jerd', 'age': 20, 'sec': 'male'}
                    dic.update({"name":"JERD"})
    4.查:  key值和get
        1. 根据key值去查
                print(dic[key])         key值不存在,会报错
        2. print(dic.get('name1'))      #key值不存在，默认结果为None
           print(dic.get('name1',[]))   自定义默认值

        3.  "name1" in dic              判断key值是否存在

Dict的输出
    1.  dic.keys()          输出所有的key值          dict_keys(['name', 'age'])
    2.  dic.values()        输出所有的value值        dict_values(['jere', 18])
    3.  dic.items()         输出键值对               dict_items([('name', 'jere'), ('age', 18)])

    改变其输出形式：
    for i in dic.keys():print(i, dic[i])
    for i in dic.items():print(i[0],i[1])
    for a,b in dic.items():print(a,b)
    
Dict之OrderedDict：
    dict这个数据结构由于hash的特性，是无序的
    collections模块为我们提供了OrderdDict,当你要获取一个有序的字典对象时,可以使用它
    例：
        from collections import OrderedDict
        items = (('f1',1),('f2s',2),('f3',3))
        regular_dict = dict(items)
        ordered_dict = OrderedDict(items)
        
        print(regular_dict) #{'f1': 1, 'f3': 3, 'f4': 4,'f2s': 2,}
        print(ordered_dict) #{'f1': 1, 'f2s': 2, 'f3': 3, 'f4': 4}
        
Dict之defaultdict:
    创建dict时,设置个默认值。当字典中没有的键第一次出现时 自动为其返回默认值
    d=defaultdict(list)     创建字典，默认值为list
    d = defaultdict(int)    默认值为0,用来计数
    例：
        将相同key值得value整合到一起
        s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        from collections import defaultdict
        d=defaultdict(list)
        for k, v in s:
            d[k].append(v)
        使用dict.setdefault()实现相   
        d={}
        for k, v in s:
            d.setdefault(k,[]).append(v)

Dict之fromkeys：
    fromkeys：接收两个参数，第一个参数的值迭代作为key值，第二个参数作为value值。key值指向同一内存地址
    例：
        dic1=dict.fromkeys("abc",[])
        print(dic1)                                         结果：{'a': [], 'b': [], 'c': []}
        print(id(dic1['a']),id(dic1['b']),id(dic1['c']))    结果2856427703304 2856427703304 2856427703304
        dic1['a'].append('jerd')
        print(dic1)                                         结果：{'a': ['jerd'], 'b': ['jerd'], 'c': ['jerd']}
    
Dict之删除键值对：
        在循环一个字典时,如果删除某些键值对,可能会报错
        例：把含有k的键值对给删掉
            dic={"k1":"abc","k2":12,"k3":'a',"name":"jerd"} 
            for i in dic.keys():
                if "k"in i:
                    del dic[i]     #结果会报错  RuntimeError: dictionary changed size during iteration
        正确的做法：
        dic={"k1":"abc","k2":12,"k3":'a',"name":"jerd"}
        li=[]
        li= [ i for i in dic.keys() if "k"in i ]
        for i in li:del dic[i]
Dict之排序：
       dic_key = {3: '能', 2: '吗',  1:'改签',  2:'或', 5:'发站', 6:'变更'}
       dic_value = {'能': 3, '吗': 2, '改签': 1, '或': 2, '发站': 5, '变更': 6}
       例：
            1.将dic_key按照Key值降序
                from collections import OrderedDict
                dic = OrderedDict(sorted(dic_key.items(),key=lambda x : x[0], reverse=True))
            2.将dic_value按照value值降序
               dic = OrderedDict(sorted(dic_value.items(),key=lambda x : x[1], reverse=True))

"""

#######################Set###########################

"""
集合:
     1, 他是无序的,是不重复的.利用集合去重
     2, 他里面的元素必须是可哈希的. int str bool ()但是它本身是不可哈希的.
     3, 集合不能更改里面的元素.
     4, 集合可以求交集,并集,差集,反交集等.
     使用场景:  对列表进行去重处理
        例：
            li=[1,2,2,2,5]
            li=list(set(li))    #[1, 2, 5]

集合的创建，增，删，查看共9种
    1.集合的创建：{value,value....} 和set()
        建立一个空集合： a_set = set()
                        a_set = {} 默认是字典类型
        1.  set1 = set({1,2,'barry'})  
        2.  set2={1,2,3}               
        里面的元素必须是可哈希的,无序的
        例：
            set1={'abc',1,2,"a",[1,2,3]}  #会报错。列表是可变的
    2.集合的增：add 和update 
        set1={'abc',1,2,"a"}
        1.  set1.add(15)        add()方法接受单个参数，并将该值添加到集合中。
                                如果添加一个集合中已存在的值，会默认是一条空操作，不会发生任何事情
        2.  set1.update("abc")  update()方法接受可迭代对象,迭代添加 {1, 2, 'c', 'abc', 15, 'a', 'b'}
        
        如果update接收的是dict 会怎么样？
            a_set.update({"name":"jerry","age":18}) #{'name', 'age'} 将key值添加到集合中
    3.集合的删 discard pop remove clear del
        1.discard()     接受单个参数，并从集合中删除该值。如果删除的值不在set中，会默认是一条空操作，不做任何操作
        2.remove()      接受单个参数，如果删除的值不在集合中，remove()会引发KeyError
        3.pop()         无参数，集合是无序的，从集合中随机删除一个值，并返回该值.如果对空集合使用pop 会引发KeyError
        4.clear()       清空集合中所有的值
        5.del           删除集合

Set交集，并集，反交集，差集，子集，超集
set1={1,2,"abc",'c',5}
set2={1,2,"ab",'c','a'}
    
    1. 集合的交集 & intersection
        set3=set1 & set2
        set1.intersection(set2)             {1, 2, 'c'}
        
    2. 集合的并集 |  union
        set3=set1 | set2  
        set1.union(set2)                    {1, 2, 5, 'abc', 'c', 'ab', 'a'}
    
    3.反交集 ^ symmetric_difference
        set1^ set2                     
        set1.symmetric_difference(set2)     {'ab', 5, 'abc', 'a'}

    4.差集   -  difference
        set1 - set2                         {5, 'abc'}
        set2 - set1                         {'a', 'ab'}
        set1.difference(set2)               {5, 'abc'}
    5.子集issubset和超集issuperset 
        用来判断 结果为True和false
        set1 < set2                         True
        set1.issubset(set2)                 True
        set2.issuperset(set1)               True
    6.frozenset不可变集合，让集合变成不可变类型
        set1={1,2,"abc",'c',5}
        s = frozenset(set1)
        print(s,type(s))          #frozenset({1, 2, 'c', 5, 'abc'}) <class 'frozenset'>
"""


#####################数据类型之间的转换################

"""
1.str和list之间的转换
    str -->list(用 split）  list --->str(用join）
    例：
        1.split和list强转
            a='alsrtew'
            print(a.split("r"))   #结果:['als', 'tew']
            a='alsrtew'            直接用list转换，是迭代转换的
            print(list(a))         #结果:['a', 'l', 's', 'r', 't', 'e', 'w']
        2.join：李列表中的元素必须均为str
            a=["abc","anxss",'2']  
            b="".join(a)
            print(b)              #结果: abcanxss2  列表中的元素类型必须均为字符串否则会报错
            a=["abc","anxss",2]   #报错
2.元组和list的转换
    tu=("a","abc",12)
    a=list(tu)    #结果:['a', 'abc', 12]
    li=["a","abc",12]
    a=tuple(li)   #结果:('a', 'abc', 12)
3.list和set的转换
    list ----> set
        li=[1,2,4,8]
        li=set(li)
        print(li)  #{8, 1, 2, 4} 是无序的
    set ----> list
        set1={8, 1, 2, 4}
        set1=list(set1)
        print(set1)  #[8, 1, 2, 4]
4.list和dict
    dict ---> list
        dic={"k1":"abc","k2":12,"k3":'a',"name":"jerd"}
        print(list(dic.keys())    ['k1', 'k2', 'k3', 'name']
        print(list(dic.items()))    #[('k1', 'abc'), ('k2', 12), ('k3', 'a'), ('name', 'jerd')]
    list---> dict
        dic=dict([("a",1),("b",2)])
        print(dic)    #{'a': 1, 'b': 2}
5.tuple和dict
    dict ---> tuple
        dic={"k1":"abc","k2":12,"k3":'a',"name":"jerd"}
        print(tuple(dic.keys())    ('k1', 'k2', 'k3', 'name')
        print(tuple(dic.items()))    #(('k1', 'abc'), ('k2', 12), ('k3', 'a'), ('name', 'jerd'))
    tuple---> dict
        dic=dict((("a",1),("b",2)))
        print(dic)    #{'a': 1, 'b': 2}
"""


