def optimize(n, s, updates):
    li = [0] * n

    for update in updates:
        a, b, k = update
        li[a - 1] += k
        if b < n:
            li[b] -= k

    max_value = 0
    current_sum = 0

    for value in li:
        current_sum += value
        if current_sum > max_value:
            max_value = current_sum

    return max_value


n, s = map(int, input().split())
updates = [tuple(map(int, input().split())) for _ in range(s)]

result = optimize(n, s, updates)
print(result)
