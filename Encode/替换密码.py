put = "lf5{ag024c483549d7fd@@1}"  #输入
dict = {1:2,2:1,3:5,4:6,5:4,6:3}  #替换密钥
res = ""

log = 0 #第几轮
k = 6 #长度

for i in range(len(put)):
    log = i // k
    n = log * k
    res = res + put[n + dict[i + 1 - n] - 1]

print(res)

