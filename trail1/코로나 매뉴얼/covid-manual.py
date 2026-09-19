# 증상 o 체온 >= 37  : A
# 증상 x 체온 >= 37  : B
# 증상 o 체온 < 37   : C
# 증상 x 체온 < 37   : D

count = 0

a, temp = input().split()

temp = int(temp)

if a == "Y":
    if temp >= 37:
        count = count + 1

b, temp = input().split()
temp = int(temp)

if b == "Y":
    if temp >= 37:
        count = count + 1

c, temp = input().split()
temp = int(temp)

if c == "Y":
    if temp >= 37:
        count = count + 1

if count >= 2:
    print("E")
else:
    print("N")