import math
import rsa
import random

config = {}


class RSAInt(object):
    """
        mode: develop
        recvpath: /data/recvtemp/
        stopath: /data/hxsto/
        ndcpath: /data/ndc/
        shaslat: YpuDSaoGf40u22Rs
        rsakey:
            p: 3367900313
            q: 5463458053
            n: 1534346956685563
            e: 107899477698547
            d: 190792854759163

    """

    @staticmethod
    def encrypt(a):

        return pow(a, config['rsakey']['d'], config['rsakey']['n'])

    @staticmethod
    def decrypt(b):
        return pow(b, config['rsakey']['e'], config['rsakey']['n'])

    @classmethod
    def encrypt_b36(cls, a):
        return cls.encrypt(a)
        # return mpz(cls.encrypt(a)).digits(36) # 转成字符串

    @classmethod
    def decrypt_b36(cls, b):
        return cls.decrypt(b)
        # return cls.decrypt(int(b, 36)) # 转成十进制


class RsaPublicPrivate(object):
    """通过rsa模块实现rsa加密"""
    @staticmethod
    def create_keys():
        """
        生成公钥和私钥
        :return:
        """
        (pubkey, privkey) = rsa.newkeys(1024)
        pub = pubkey.save_pkcs1()
        with open('public.pem', 'wb+')as f:
            f.write(pub)

        pri = privkey.save_pkcs1()
        with open('private.pem', 'wb+')as f:
            f.write(pri)

    @staticmethod
    def encrypt(original_text):
        """用公钥加密"""
        with open('public.pem', 'rb') as publickfile:
            p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)
        crypt_text = rsa.encrypt(original_text, pubkey)
        return crypt_text

    @staticmethod
    def decrypt(crypt_text):
        """用私钥解密"""
        with open('private.pem', 'rb') as privatefile:
            p = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(p)
        lase_text = rsa.decrypt(crypt_text, privkey).decode()  # 注意，这里如果结果是bytes类型，就需要进行decode()转化为str

        return lase_text


RSA_debug = False
if RSA_debug:
    original_content = 'have a good time'.encode('utf8')
    crypt_text = RsaPublicPrivate().encrypt(original_content)
    lase_text = RsaPublicPrivate().decrypt(crypt_text)


# class DetectionPrime(object):
#     """检测是否为素数"""
#     @classmethod
#     def detection_num(cls, num_p: int = None, num_q: int = None):
#         """检测是否为素数"""
#         if math.sqrt(num_p) < 2:
#             return True
#         for i in range(2, num_p):
#             if num_p % i == 0:
#                 return False
#
#         if num_q:
#             if math.sqrt(num_q) < 2:
#                 return True
#
#             for i in range(2, num_q):
#                 if num_q % i == 0:
#                     return False
#
#         return True
#
#
# class ComputePublicPrivate(object):
#     """计算公共模数N 公钥E 和 私钥D
#          p: 3367900313
#          q: 5463458053
#     """
#     def __init__(self, prime_p, prime_q):
#         self.P = prime_p
#         self.Q = prime_q
#
#     @classmethod
#     def generate_prime_number(cls):
#         """生成素数 P, Q"""
#         prime_list = []
#         for num in range(2, 2000):
#             x = DetectionPrime.detection_num(num_p=num)
#             prime_list.append(num) if x else None
#         p, q = random.choice(prime_list), random.choice(prime_list)
#
#         return cls(p, q)
#
#     def gcd(self, a, b):
#         if b == 0:
#             return a
#         else:
#             return self.gcd(b, a % b)
#
#     def find_e(self, s):
#         """找出与（p-1）*(q-1)互质的数e"""
#         while True:
#             e = random.choice(range(100000000))
#             x = self.gcd(e, s)
#             if x == 1:  # 如果最大公约数为1，则退出循环返回e
#                 break
#         return e
#
#     @staticmethod
#     def find_d(e, s):
#         for d in range(10000000000):  # 随机太难找，就按顺序找到d,range里的数字随意
#             x = (e * d) % s
#             if x == 1:
#                 return d
#
#     def compute_value(self, detection=False):
#         """计算N E D的值"""
#         num_p, num_q = self.P, self.Q
#         if detection:
#             res = DetectionPrime.detection_num(num_p=num_p, num_q=num_q)
#             if not res:
#                 return False
#         n = num_p * num_q
#         s = (num_p - 1) * (num_q - 1)
#         e = self.find_e(s)
#         d = self.find_d(e, s)
#
#         config['rsakey'] = {
#                 'n': n,
#                 'e': e,
#                 'd': d
#             }
#
#         print("公钥:   n=", n, "  e=", e)
#         print("私钥:   n=", n, "  d=", d)
#
#
# if __name__ == '__main__':
#     p = 3367900313
#     q = 5463458053
#     # 自动生成p q
#     # ret = ComputePublicPrivate.generate_prime_number().compute_value()
#     # 指定p q
#     ret = ComputePublicPrivate(p, q).compute_value(False)
#     # 加密
#     uid = 235
#     res = RSAInt.encrypt_b36(uid)
#     print("加密后的值是：", res)
#     # 解密
#     deres = RSAInt.decrypt_b36(res)
#     print("解密后的值是：", deres)






def rabinMiller(num):
    s = num - 1
    t = 0
    while s%2 == 0:
        s //= 2
        t += 1
    for trials in range(5):
        a = random.randrange(2,num-1)
        v = pow(a,s,num)
        if v!=1:
            i = 0
            while v!=(num-1):
                if i == t-1:
                    return False
                else:
                    i += 1
                    v = (v**2)%num
    return True

def isPrime(num):
    if num<2:
        return False
    lowPrimes = [
                    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                    449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                    587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                    853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                    991, 997
    ]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if num % prime==0:
            return False

    return rabinMiller(num)

def generateLargePrime(keysize=1024):
    while True:
        num = random.randrange(2**(keysize-1),2**keysize)

        if isPrime(num):
            return num

def gcd(a, b):
# Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b
def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1
    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime
    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
def generateRSAkey(keySize=1024):
    p = generateLargePrime(keySize)
    q = generateLargePrime(keySize)
    print(p)
    print("=========================")
    print(q)
    n = p * q

    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
    d = findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print(publicKey)
    print(privateKey)

# generateRSAkey()







