m="sdu"
m1="scu"
#生成元G
G=[2,7]
#生成元的阶
n=13
k=3
d=7
Gx=G[0]
Gy=G[1]
P=calculate_np(Gx, Gy, a, b, p, k)
Px=P[0]
Py=P[1]

print("进行ECDSA签名----------------")
r,s=Sign(m, n, Gx, Gy, d, k)
print("签名r为：",r)
print("签名s为：",s)

print("伪造签名---------------------")
r1,s1,e1=PretendSign(n, Gx,Gy , Px, Py)
print("消息",e1,"的签名为：","r1:",r1,",e1:",s1,"\n")

print("泄露k导致密钥泄露-------------")
d1=leak(r,m,s,k,n)
if d1==d:
    print("泄露k的值为：",k)
    print("验证成功，反推密钥的值为：",d,"\n")
else:
    print("验证失败。")

print("重用k导致密钥泄露-------------")
r_,s_=Sign(m1, n, Gx, Gy, d, k)
d2=reuse(r,s,m,r_,s_,m1,n)
if d2==d:
    print("重用k的值为：",k)
    print("验证成功，反推密钥的值为：",d,"\n")
else:
    print("验证失败。")
