def re(a:int)->int:            #求a的逆元(传入参数为a(int类型),返回值为int类型)
    a_re = 0                   #初始化逆元
    while True:                #依照a * a^-1 mod 26 == 1算出逆元a^-1，为逆元直接返回a_re,不为则让a_re+1再判断
        if a_re * int(a) % 26 == 1:
            break
        else:
            a_re += 1
    return a_re

def decode(de:str,a_re:int,b:int)->str:      #解密函数(传入参数为de(str类型),a(int类型),b(int类型),无返回值)
    res = ''
    for i in de:                        #for循环,以此获得de中的元素进行比较
        if i >= 'A' and i <= 'Z':       #利用D(𝑥)=(𝑎(𝑥-𝑏))𝑚𝑜𝑑 𝑚解密字母 ord()是将字符转成ASCII码,chr()是将ASCII码变回字符
            res = res + chr((a_re * ((ord(i) - 65) - b)) % 26 + 65)
        elif i >= 'a' and i <= 'z':
            res = res + chr((a_re * ((ord(i) - 97) - b)) % 26 + 97)
        else:
            res = res + i
    return res

#主函数 #11 5
#de = input('输入密文:')
#en = input('输入部分明文:')
de = "Diffa Eavfb"     #密文
en = "H"               #部分明文
res = ''
key_a = [1,3,5,7,9,11,15,17,19,21,23,25]
for a in key_a:
    for b in range(0,26):
        res = decode(de[0:len(en)],re(a),b)
        if(res == en):
            print("密钥a为:%d密钥b为:%d"%(a,b))
            res = decode(de, re(a), b)
            print('解密结果为:%s' % res)
