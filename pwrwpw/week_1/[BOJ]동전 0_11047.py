# 시간복잡도 : NlogN

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0

for coin in coins:
    if k >= coin:
        cnt += k // coin
        k %= coin
        if k <= 0:
            break
print(cnt)
