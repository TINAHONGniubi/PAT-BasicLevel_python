# 害死人不偿命的(3n+1)猜想

n = int(input())
step = 0
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n*3+1) // 2
    step = step + 1
print(step)
