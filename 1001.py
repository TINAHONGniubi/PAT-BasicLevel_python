# 1001 害死人不偿命的(3n+1)猜想：给定的任一不超过 1000 的正整数 n，简单地数一下，需要多少步（砍几下）才能得到 n=1？

n = int(input())
step = 0
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n*3+1) // 2
    step = step + 1
print(step)
