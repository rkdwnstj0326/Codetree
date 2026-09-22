arr = []

for _ in range(4):
    row = list(map(int, input().split()))

    arr.append(row)

# print(arr)
 
for r in range(4):
    total = 0
    for c in range(4):
        total = total + arr[r][c]

    
    print(total)