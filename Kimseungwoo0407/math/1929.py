# 소수 구하기

n, m = map(int,input().split())

for i in range(n,m+1):
    is_prime = True
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        print(i)