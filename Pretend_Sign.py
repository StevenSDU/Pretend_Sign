import math
import random
from Crypto.Util.number import *
import hashlib

# 计算SHA-256加密
def hash(m):
    return hashlib.sha256(str(m).encode()).hexdigest()

# 求value在Fp域的逆——用于分数求逆
def get_inverse(value, p):
    for k in range(1, p):
        if (k * value) % p == 1:
            return k
    return -1

#简单素数检测
def isPrime(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#求最大公因数
def get_gcd(x, k):
    if k == 0:
        return x
    else:
        return get_gcd(k, x % k)

# 计算P+Q函数
def calculate_p_q(x1, y1, x2, y2, a, b, p):
    flag = 1  # 控制符号位

    # 若P = Q，则k=[(3x1^2+a)/2y1]mod p
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a  # 计算分子
        denominator = 2 * y1  # 计算分母

    # 若P≠Q，则k=(y2-y1)/(x2-x1) mod p
    else:
        member = y2 - y1  # 分子
        denominator = x2 - x1  # 分母
        if member * denominator < 0:
            flag = 0
            member = abs(member)
            denominator = abs(denominator)

    # 将分子和分母化为最简
    gcd_value = get_gcd(member, denominator)
    member = member // gcd_value
    denominator = denominator // gcd_value

    # 求分母的逆元
    inverse_value = get_inverse(denominator, p)
    k = (member * inverse_value)
    if flag == 0:
        k = -k
    k = k % p

    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return [x3, y3]

# 计算nP函数
def calculate_np(p_x, p_y, a, b, p, n):
    tem_x = p_x
    tem_y = p_y
    for k in range(n - 1):
        p_value = calculate_p_q(tem_x, tem_y, p_x, p_y, a, b, p)
        tem_x = p_value[0]
        tem_y = p_value[1]
    # return p_value
    return [tem_x, tem_y]

#随便假设椭圆曲线参数
a=1
b=1
p=23

#ECDSA签名
def Sign(m, n, Gx, Gy, d, k):
    e = hash(m)
    R = calculate_np(Gx,Gy,a,b,p,k)
    r = R[0] % n
    s = (Gcd(k, n) * (e + d * r)) % n
    return r, s

#伪造中本聪签名（表明消息e_的签名为r_和s_）
def PretendSign(n, Gx,Gy , Px, Py):
    u = random.randrange(1, n - 1)
    v = random.randrange(1, n - 1)
    uG = calculate_np(Gx,Gy,a,b,p,u)
    uGx = uG[0]
    uGy = uG[1]
    vP = calculate_np(Px,Py,a,b,p,v)
    vPx = vP[0]
    vPy = vP[1]
    r_=calculate_p_q(uGx, uGy, vPx, vPy, a, b, p)[0]
    v_=get_inverse(v, n)
    s_=(r_*v_)%n
    e_=(r_*u*v)%n
    return [r_,s_,e_]

#重用k导致密钥泄露：
def reuse(r1,s1,m1,r2,s2,m2,n):
    e1=hash(m1)
    e2=hash(m2)
    s1_=get_inverse(s1, n)
    s2_=get_inverse(s2, n)
    re=get_inverse((r1*s1_-r2*s2_), n)
    d=(re*(e2*s2_-e1*s1_))%n
    return d

#泄露k导致密钥泄露：
def leak(r,m,s,k,n):
    r_=get_inverse(r, n)
    e=hash(m)
    d=((s*k-e)*r_)%n
    return d
