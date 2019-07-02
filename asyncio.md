# 定义协程 async 和 生成器
    import asyncio
    from collections.abc import Coroutine,Iterable, Iterator, Generator
    
    
    async def hello(name):
        print('Hello,',name)
    
    @asyncio.coroutine
    def demo():
        '''
        只要在一个生成器函数头部用上 @asyncio.coroutine 装饰器
        就能将这个函数对象，【标记】为协程对象。注意这里是【标记】，划重点。
        实际上，它的本质还是一个生成器。
        标记后，它实际上已经可以当成协程使用。
        '''
        # 异步调用asyncio.sleep(1):
        yield from asyncio.sleep(1)
    
    if __name__ == "__main__":
        coroutine = hello("World")
        print(isinstance(coroutine, Coroutine))
    
        demo_coroutine = demo()
        print(isinstance(demo_coroutine, Generator))
        print(isinstance(demo_coroutine, Coroutine))
        

# asyncio的基本概念
    async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield
    coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
    event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类
    future 对象： 它和task上没有本质的区别

## 协程完整的工作流程：
        定义/创建协程对象
        将协程转为task任务
        定义事件循环对象容器
        将task任务扔进事件循环对象中触发
        
        import asyncio

        async def hello(name):
            print('Hello,', name)
        
        # 定义协程对象
        coroutine = hello("World")
        
        # 定义事件循环对象容器
        loop = asyncio.get_event_loop()
        
        # 将协程转为task任务
        # task = asyncio.ensure_future(coroutine)    # future对象
        task = loop.create_task(coroutine)           # task对象
        
        # 将task任务扔进事件循环对象中并触发
        loop.run_until_complete(task)
        

## await与yield对比:
    ### 区别：
        1. await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。（都能实现暂停的效果），但是功能上却不兼容。
           就是不能在生成器中使用await，也不能在async 定义的协程中使用yield。

        2.yield from 后面可接 可迭代对象，也可接future对象/协程对象；
          await 后面必须要接 future对象/协程对象
    ### asyncio.sleep(n)
    asyncio自带的工具函数，他可以模拟IO阻塞，他返回的是一个协程对象。
    from asyncio.futures import Future
    from asyncio.tasks import  Task

    func = asyncio.sleep(2)
    print(isinstance(func,Generator))           #True
    print(isinstance(func,Future))              #False

    ### 验证
        # await 接协程
        async def hello_1(name):
            await  asyncio.sleep(2)
            print("Hello,",name)

        # await 接Future对象
        async def hello_2(name):
            await asyncio.ensure_future(asyncio.sleep(2))

        # yield from 接协程
        def hello_3(name):
            yield from asyncio.sleep(2)

        # yield from  接Future对象

        def hello_4(name):
            yield from asyncio.ensure_future(asyncio.sleep(2))

    ### 绑定回调函数:
        异步IO的实现原理，就是在IO高的地方挂起，等IO结束后，再继续执行。在绝大部分时候，需要依赖IO的返回值的，这就要用到回调了。
            async def hello_1(x):
                await  asyncio.sleep(2)
                return "暂停了{time}秒".format(time=x)
    
            def callback(future):
                print('这里是回调函数，获取返回结果是：', future.result())
    
            coroutine = hello_1(2)
            loop = asyncio.get_event_loop()
            task = asyncio.ensure_future(coroutine)
    
            # 1.添加回调函数
            task.add_done_callback(callback)
            loop.run_until_complete(task)
    
            # 2.task.result() 可以取得返回结果
            # print("返回结果是：{time}".format(time=task.result()))


# 协程中的并发:
    asyncio实现并发，就需要多个协程来完成任务，每当有任务阻塞的时候就await，然后其他协程继续工作

## 多个协程注册到事件循环中 asyncio.wait() 和 asyncio.gather()
        async def hello(x):
        print("Waiting: ",x)
        await  asyncio.sleep(2)
        return "暂停了{time}秒".format(time=x)

        # 创建多个协程
        coroutine_1 = hello(2)
        coroutine_2 = hello(5)
        coroutine_3 = hello(8)

        loop = asyncio.get_event_loop()
        # 将协程转成任务,并转成list
        tasks = [
            asyncio.ensure_future(coroutine_1),
            asyncio.ensure_future(coroutine_2),
            asyncio.ensure_future(coroutine_3),

        ]

        # 协程注册到事件循环中 asyncio.wait() 和 asyncio.gather()
        #loop.run_until_complete(asyncio.wait(tasks))
        loop.run_until_complete(asyncio.gather(*tasks))

        # 查看结果
        for task in tasks:
            print('task result is:',task.result())

## 协程中的嵌套：一个协程中await了另外一个协程
        async def hello(x):
            print("Waiting: ",x)
            await  asyncio.sleep(2)
            return "暂停了{time}秒".format(time=x)


        async def main():
            # 创建三个协程对象
            # 创建多个协程
            coroutine_1 = hello(2)
            coroutine_2 = hello(5)
            coroutine_3 = hello(8)

            # 将协程转为task，并组成list
            tasks = [
                asyncio.ensure_future(coroutine_1),
                asyncio.ensure_future(coroutine_2),
                asyncio.ensure_future(coroutine_3),

            ]

            # 【重点】：await 一个task列表（协程）
            # dones：表示已经完成的任务
            # pendings：表示未完成的任务
            dones, pendings = await asyncio.wait(tasks)

            for task in dones:
                print('Task result: ', task.result())

        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    ## 协程中的状态
        Pending：创建future，还未执行
        Running：事件循环正在调用执行任务
        Done：任务执行完毕
        Cancelled：Task被取消后的状态

#  动态添加协程
    在asyncio中将协程态添加到事件循环中的

### 1.主线程是同步的
    import time
    import asyncio
    from queue import Queue
    from threading import Thread
    
    def start_loop(loop):
        # 一个在后台永远运行的事件循环
        asyncio.set_event_loop(loop)
        loop.run_forever()
    
    def do_sleep(x, queue, msg=""):
        time.sleep(x)
        queue.put(msg)
    
    queue = Queue()
    
    new_loop = asyncio.new_event_loop()
    
    # 定义一个线程，并传入一个事件循环对象
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    
    print(time.ctime())
    
    # 动态添加两个协程，在主线程是同步的
    new_loop.call_soon_threadsafe(do_sleep, 6, queue, "第一个")
    new_loop.call_soon_threadsafe(do_sleep, 3, queue, "第二个")
    
    while True:
        msg = queue.get()
        print("{} 协程运行完..".format(msg))
        print(time.ctime())
    
    由于是同步的，所以总共耗时6+3=9秒.
    
    
### 2.主线程是异步的
    import time
    import asyncio
    from queue import Queue
    from threading import Thread
    
    def start_loop(loop):
        # 一个在后台永远运行的事件循环
        asyncio.set_event_loop(loop)
        loop.run_forever()
    
    async def do_sleep(x, queue, msg=""):
        await asyncio.sleep(x)
        queue.put(msg)
    
    queue = Queue()
    
    new_loop = asyncio.new_event_loop()
    
    # 定义一个线程，并传入一个事件循环对象
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    
    print(time.ctime())
    
    # 动态添加两个协程，在主线程是异步的
    asyncio.run_coroutine_threadsafe(do_sleep(6, queue, "第一个"), new_loop)
    asyncio.run_coroutine_threadsafe(do_sleep(3, queue, "第二个"), new_loop)
    
    while True:
        msg = queue.get()
        print("{} 协程运行完..".format(msg))
        print(time.ctime())
        
    总共耗时max(6, 3)=6秒
    
  
  
### 3.asyncio.get_event_loop()和asyncio.new_event_loop()的区别
    new_event_loop()是创建一个eventloop对象，而set_event_loop(eventloop对象)是将eventloop对象指定为当前线程的eventloop，一个线程内只允许运行一个eventloop，
    意味着不能有两个eventloop交替运行。这两者一般搭配使用，用于给非主线程创建eventloop。
    如果是主线程，则只需要get_event_loop就可以了，也就是说，我们想运用协程，首先要生成一个loop对象，然后loop.run_xxx()就可以运行协程了，
    而如何创建这个loop,对于主线程是loop=get_event_loop().对于其他线程需要首先loop=new_event_loop(),然后set_event_loop(loop)
    
    import threading
    import asyncio
    
    
    def thread_loop_task(loop):
    
        # 为子线程设置自己的事件循环
        asyncio.set_event_loop(loop)
    
        async def work_2():
            while True:
                print('work_2 on loop:%s' % id(loop))
                await asyncio.sleep(2)
    
        async def work_4():
            while True:
                print('work_4 on loop:%s' % id(loop))
                await asyncio.sleep(4)
    
        future = asyncio.gather(work_2(), work_4())
        loop.run_until_complete(future)
    
    
    if __name__ == '__main__':
    
        # 创建一个事件循环thread_loop
        thread_loop = asyncio.new_event_loop()
    
        # 将thread_loop作为参数传递给子线程
        t = threading.Thread(target=thread_loop_task, args=(thread_loop,))
        t.daemon = True
        t.start()
    
        main_loop = asyncio.get_event_loop()
    
    
        async def main_work():
            while True:
                print('main on loop:%s' % id(main_loop))
                await asyncio.sleep(4)
    
    
        main_loop.run_until_complete(main_work())
        

### 4.利用redis实现动态添加任务

    import time
    import redis
    import asyncio
    from queue import Queue
    from threading import Thread
    
    def start_loop(loop):
        # 一个在后台永远运行的事件循环
        asyncio.set_event_loop(loop)
        loop.run_forever()
    
    async def do_sleep(x, queue):
        print("=================")
        await asyncio.sleep(x)
        queue.put("ok")
    
    def get_redis():
        #未添加decode_responses，从redis中取出的数据为bytes类型
        connection_pool = redis.ConnectionPool(host='10.110.1.111', db=0,decode_responses=True)
        return redis.Redis(connection_pool=connection_pool)
    
    def consumer():
        while True:
            task = rcon.rpop("queue")
            if not task:
                print("+++++++++++++++")
                time.sleep(1)
                continue
            print("---------:",int(task))
            asyncio.run_coroutine_threadsafe(do_sleep(int(task), queue), new_loop)
    
    
    if __name__ == '__main__':
        print(time.ctime())
        new_loop = asyncio.new_event_loop()
    
        # 定义一个线程，运行一个事件循环对象，用于实时接收新任务
        loop_thread = Thread(target=start_loop, args=(new_loop,))
        loop_thread.setDaemon(True)
        loop_thread.start()
        # 创建redis连接
        rcon = get_redis()
    
        queue = Queue()
    
        # 子线程：用于消费队列消息，并实时往事件对象容器中添加新任务
        consumer_thread = Thread(target=consumer)
        consumer_thread.setDaemon(True)
        consumer_thread.start()
    
        while True:
            msg = queue.get()
            print("协程运行完..",)
            print("当前时间：", time.ctime())
    
    在Redis，分别发起了5s，3s，1s的任务。这三个任务，确实是并发执行的，1s的任务最先结束，三个任务完成总耗时5s
    
    


    
 
 
