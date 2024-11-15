# 1002 写出这个数: 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

#string
n = input()

#累加
sum = 0
for i in n:
    sum += int(i)

int2chinese = {
    0:"ling",
    1:"yi",
    2:"er",
    3:"san",
    4:"si",
    5:"wu",
    6:"liu",
    7:"qi",
    8:"ba",
    9:"jiu",
}

#转换为string
sum_str = str(sum)

pinyin_result = []

for i in sum_str:
    pinyin_result.append(int2chinese[int(i)])

print(" ".join(pinyin_result))  
