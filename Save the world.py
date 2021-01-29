n,m = [int(x) for x in input().split()]
key = input()
a = input().split()
flag = 0
for i in a:
    if (i in key) and i[0] == key[0] :
        flag = 1
        print("Yes")
        break

if flag == 0:
    print("No")

