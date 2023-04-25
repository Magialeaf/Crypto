put = "21 33 1 22 3 44 54 5 1 35 54 3 35 41 52 13"  #输入数字

lst = put.split(" ")

dic ={1:"A",11:"B",12:"C",13:"D",2:"E",21:"F",22:"G",23:"H"
     ,3:"I",31:"J",32:"K",33:"L",34:"M",35:"N"
     ,4:"O",41:"P",42:"Q",43:"R",44:"S",45:"T"
     ,5:"U",51:"V",52:"W",53:"X",54:"Y",55:"Z"}

res = []

for i in lst:
    i = int(i)
    if i in dic.keys():
        res.append(dic[i])

res =  "".join(res)

print(res)