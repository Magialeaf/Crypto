#雷池加密，自定义偏移量（ascii码）的数值。
def caesar(text):
    for i in range(len(text)):
        y=-1-i#偏移规律（设置偏移量）
        print("{}".format(chr(ord(text[i])+y)),end='')#此处的 +y 可根据题目要求设置

caesar('gndk rlqhmtkwwp}z')#输入要解密的文本
