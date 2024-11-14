# 1003 我要通过！：只要读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。
# 得到“答案正确”的条件是：
# 字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
# 任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
# 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。


n = int(input())

for _ in range(n):
    s = input()

# 是否符合条件1或条件2

    if s == "PAT":
        print("YES")
        continue

    # P和T各只有一个
    if set(s).issubset({'P', 'A', 'T'}) and s.count('P') == 1 and s.count('T') == 1:
        p_index = s.find('P')
        t_index = s.find('T')
        
        a = s[:p_index]
        b = s[p_index + 1:t_index]
        c = s[t_index + 1:]
        
        #P在T之前，且abc分别多长，且都为A
        if p_index < t_index and t_index - p_index >= 1 and (set(a) <= {'A'}) and (set(b) <= {'A'}) and (set(c) <= {'A'}):
            a_len = len(a)
            b_len = len(b)
            c_len = len(c)

            if c_len == a_len * b_len and b_len >= 1:
                print ("YES")
                continue

    print("NO")
