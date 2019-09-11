# datetime模块
    datetime库定义了5个类:
        date类：表示日期的类
        time类：表示时间的类
        datetime类：表示时间日期的类
        timedelta类：表示两个datetime对象的差值；
        tzinfo类：表示时区的相关信息

    from datetime import date, time, datetime

### 1.date
    1. 创建自定义日期 个位数的月和日前面不要加0
        day = date(2019, 4, 15)
    2. 获取本地时间
        day = date.today()
    3. 日期属性
        day.year                        年
        day.month                       月
        day.day                         日
        day.weekday()                   获取星期几 获取星期几，0-6代表周一到周天
        day.isoweekday()                获取星期几，1-7代表周一到周天

### 2.timedelta 对时间进行运算操作
    interval = timedelta(days=7)         七天的时间间隔
    计算一周后的日期：
        future_day = day + interval

    计算两个时间的相隔天数：
        bday = date(2001, 1, 30)
        tday = date.today()
        interval = tday - bday

### 3.datetime.time
    now_time = time(10, 21, 29,19999)
    时间属性：
        print(now_time.hour)
        print(now_time.minute)
        print(now_time.second)
        print(now_time.microsecond)

### 4.datetime.datetime
    自定义时间日期：
        dt = datetime(2016, 7, 26, 12, 30, 45, 100000)
    获取当前时间日期
        dt = datetime.now()

    属性：
        dt.date()
        dt.time()

### 5.strptime 和strftime
    strptime() : 输入的日期和时间是字符串，要处理日期和时间，str转换为datetime
        dt = '2019-4-2 10:01:34'
        cday = datetime.strptime(dt, '%Y-%m-%d %X')
        print(cday, type(cday), type(dt))

    strftime() : 后台提取到datetime对象后，要把它格式化为字符串显示给用户
        day = datetime.now()
        str_day = day.strftime('%Y-%m-%d %X')
        print(type(day), str_day, type(str_day))

### 6.timestamp转换UTC时间和本地时间
    from datetime import datetime
    t = 1429417200.0
    print(datetime.fromtimestamp(t)) # 本地时间
    2015-04-19 12:20:00
    print(datetime.utcfromtimestamp(t)) # UTC时间
    2015-04-19 04:20:00


# time模块

    1.时间有三种表示方式：
        1.1时间戳(给计算机看的）                            1970年1月1日之后的秒，即：time.time()

        1.2格式化的字符串(人能够看懂的时间)                 2016-12-12 10:10，  即：time.strftime('%Y-%m-%d')

        1.3结构化时间(操作时间的)                           元组   即：time.localtime()
                                                            共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)

    时间戳-->结构化时间
        time.gmtime(时间戳)                                 UTC时间，与英国伦敦当地时间一致
        time.localtime(时间戳)                              当地时间 不写参数默认当前时间的时间戳

    结构化时间-->时间戳　
        time.mktime(结构化时间)
        time_tuple = time.localtime(1500000000)
        time.mktime(time_tuple)

    结构化时间-->字符串时间
        time.strftime("格式定义","结构化时间")               结构化时间参数若不传，则默认当前时间
        例：
            time.strftime("%Y-%m-%d",time.localtime(1500000000))

            time.strftime("%Y-%m-%d %X")                      2019-04_02 10:24:25 <class 'str'>

    字符串时间-->结构化时间
        time.strptime(时间字符串,字符串对应格式)
        例：
            time.strptime("2017-03-16","%Y-%m-%d")              <class 'time.struct_time'>

            time.strptime("07/24/2017","%m/%d/%Y")


    time.time()         返回当前时间的时间戳
    time.sleep(0.3)     休眠


# 获取当前日期前后N天或N月的日期

    import datetime
    import calendar
    
    class TimeInterval(object):
        
        def __init__(self):
            """转换为字符串格式"""
            # self.year = datetime.datetime.now().strftime('%Y')
            # self.month = datetime.datetime.now().strftime('%m')
            # self.day = datetime.datetime.now().strftime('%d')
            self.year = datetime.date(2019, 5, 31).strftime('%Y')
            self.month = datetime.date(2019, 5, 31).strftime('%m')
            self.day = datetime.date(2019, 5, 31).strftime('%d')
            self.hour = datetime.datetime.now().strftime('%H')
            self.min = datetime.datetime.now().strftime('%M')
            self.sec = datetime.datetime.now().strftime('%S')
    
        def get_days_of_month(self,year, month):
            '''
            get days of month
            calender.monthrange()计算每个月的天数,返回一个元祖(0,31),此为2018年1月,第一个参数代表当月第一天是星期几,第二个参数代表是这个月的天数
            '''
            return calendar.monthrange(year, month)[1]
    
        def addzero(self,n):
            '''
                用0左补齐成两位数
                add 0 before 0-9  return 01-09
            '''
            nabs = abs(int(n))
            if nabs < 10:
                return "0" + str(nabs)
            else:
                return nabs
    ~~~~
        def get_year_and_month(self,n=0):
            '''
            get the year,month,days from today
            befor or after n months
            '''
            thisyear = int(self.year)
            thismon = int(self.month)
            totalmon = thismon + n
            if n >= 0:
                if totalmon <= 12:
                    # 计算totalmon月的总天数
                    days = str(self.get_days_of_month(thisyear, totalmon))
                    # 月份用0左补齐成两位数
                    totalmon = self.addzero(totalmon)
                    return self.year, totalmon, days
                else:
                    # //取整除,返回商的整数部分,也就是一年
                    i = totalmon // 12
                    # %取模:返回除法的余数
                    j = totalmon % 12
                    if j == 0:
                        i -= 1
                        j = 12
                    thisyear += i
                    days = str(self.get_days_of_month(thisyear, j))
                    j = self.addzero(j)
                    return str(thisyear), str(j), days
            else:
                if totalmon > 0 and totalmon < 12:
                    days = str(self.get_days_of_month(thisyear, totalmon))
                    totalmon = self.addzero(totalmon)
                    return self.year, totalmon, days
                else:
                    i = totalmon // 12
                    j = totalmon % 12
                    if j == 0:
                        i -= 1
                        j = 12
                    thisyear += i
                    days = str(self.get_days_of_month(thisyear, j))
                    j = self.addzero(j)
                    return str(thisyear), str(j), days
    
        def get_day_of_day(self,n=0):
            """计算N天之前/之后的日期"""
            if n < 0:
                n = abs(n)
                return datetime.date.today() - datetime.timedelta(days=n)
            else:
                return datetime.date.today() + datetime.timedelta(days=n)
    
        def get_today_month(self,n=0):
            '''
            获取当前日期前后N月的日期
            if n > 0 获取当前日期前N月的日期
            if n < 0 获取当前日期后N月的日期
            date format = "YYYY-MM-DD"
            '''
            (y, m, d) = self.get_year_and_month(n)
            arr = (y, m, d)
            if int(self.day) < int(d):
                arr = (y, m, self.day)
            return "-".join("%s" % i for i in arr)
    
    
    
    if __name__ == "__main__":
        time_obj = TimeInterval()
        print('11 days after today is:', time_obj.get_day_of_day(11))
        print('11 days before today is:', time_obj.get_day_of_day(-11))
        print('10 months after today is:', time_obj.get_today_month(10))
        print('5 months before today is:', time_obj.get_today_month(-5))




# 提取文本中的金额
    import re
    Regx = re.compile("(([1-9]\\d*[\\d]*\\.?\\d*)|(0\\.[0-9]+))")
    term = "获取这个数字:12.02,测试金额"
    i = re.search(Regx,term)
    if i != None:
        print(i.group())
    
# 提取特定结构中的金额 如提取被@@包含的金额
    Regx = re.compile("@@(([1-9]\\d*[\\d]*\\.?\\d*)|(0\\.[0-9]+))@@")
    term = "获取这个数字:@@12@@,测试金额"
    i = re.search(Regx,term)
    if i != None:
        print(i.group())            # @@12.02@@
        print(i.group(1))           # 12.02
        
# 校验手机号/座机 身份证号
    pip install id-validator

    from id_validator import validator
    id_code = "422825199507064436"
    # 校验身份证是否合法
    is_enabled = validator.is_valid(id_code)
    # 身份证的详细信息
    code_info = validator.get_info(id_code)
    # 生成假身份数据
    temporary_code = validator.fake_id(True, '成都市武侯区', '19950706', 1)
    # 15位转18位
    new_code = validator.upgrade_id('610104620927690')


    cinema_info = {}
    if cinema_info.get("phone"):
        assert re.match("^1[3-9][0-9]{9}$", cinema_info["phone"]) or \
               re.match("^0[0-9]{2,3}[-| ]{0,2}[0-9]{7,8}$", cinema_info["phone"]) or \
               re.match("^0[0-9]{2,3}[-| ]{0,2}[0-9]{7,8}[-| ]{1,2}[0-9]{1,5}$",
                        cinema_info["phone"]), '院线联系电话格式不正确，只能为手机号码或带区号座机号码！'

    if cinema_info.get("fax"):
        assert re.match("^0[0-9]{2,3}[-| ]{0,2}[0-9]{7,8}$", cinema_info["fax"]), '院线传真不正确，只能为带区号座机号码！'

    if cinema_info.get("email"):
        assert re.match("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", cinema_info["email"]), '院线电子邮箱格式不正确，请重新填写！'

    # 校验硬盘接收编码和联系方式
    if cinema_info.get("post_code"):
        assert re.match("^[0-9]{6}$", cinema_info["post_code"]), '邮政编码格式不正确，请重新填写！'
        
# string
    import string

    # 列举数字 0 - 9
    ret = string.digits

    # 列举小写字母
    ret  = string.ascii_lowercase
    #  列举大写字母
    ret = string.ascii_uppercase
    # 打印所有的大小写字母
    ret = string.ascii_letters

    # 列举所有标点符号
    ret = string.punctuation

    # 列举所有空白符
    ret = string.whitespace

    # 打印十六进制的字符
    ret = string.hexdigits
    print(ret)
