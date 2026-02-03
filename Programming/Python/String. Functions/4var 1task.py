n = int(input())
correct_list = []

for i in range(n):
    a = input()
    correct_list.append(a)


m = int(input())
l = []

for i in range(m):
    a = input()
    l.append(a)

print(correct_list)
print(l)
cnt = 0
d = {}

for i in range(len(correct_list)):
    for j in range(len(l)):
        if len(correct_list[i]) != len(l[j]):
            pass
        else:
            for g in range(len(correct_list[i])):
                if correct_list[i][g] != l[j][g]:
                    cnt += 1
            if cnt == 1:
                if correct_list[i] in d:
                    d[correct_list[i]] = d[correct_list[i]] + 1
                else:
                    d[correct_list[i]] = 1
            else:
                if correct_list[i] not in d:
                    d[correct_list[i]] = 0
            cnt = 0

for i in d:
    print(d[i], end=' ')



