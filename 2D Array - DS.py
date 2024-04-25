def hourglass(a):
    maxsum = float('-inf')  # Initialize the maximum sum to negative infinity

    for i in range(4):
        for j in range(4):
            # Calculate the sum of the current hourglass elements
            current_sum = (
                a[i][j] + a[i][j + 1] + a[i][j + 2] +
                a[i + 1][j + 1] +
                a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2]
            )
            # Update maxsum if the current_sum is greater
            maxsum = max(maxsum, current_sum)

    return maxsum

a = []
for row in range(6):
    ar = list(map(int, input().split()))
    a.append(ar)

res = hourglass(a)
print(res)
