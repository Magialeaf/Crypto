input = "foerlu_ia_ssglue{ir!ykp}" #输入字符串
input = (list(input))
num = len(input)
res = []
key = 4   #字符串换位数
i = 0
j = 0
k = 0
while(i != num):
    if (j >= num):
        k += 1
        j = k
    else:
        res.append(input[j])
        j += key
        i += 1
res = "".join(res)
print(res)