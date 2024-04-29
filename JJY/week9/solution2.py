def solution(arr, k):
    n = len(arr)
    m = len(arr[0])

    for _ in range(k):
        if n == 1 and m == 1:
            break

        if n >= m:
            if m > 1:
                arr = [[max(arr[i][j], arr[i][j+1]) for j in range(0, m-1, 2)] for i in range(n)]
            m = (m) // 2
        else:
            if n > 1:
                arr = [[min(arr[i][j], arr[i+1][j]) for j in range(m)] for i in range(0, n-1, 2)]
            n = (n) // 2

    return arr