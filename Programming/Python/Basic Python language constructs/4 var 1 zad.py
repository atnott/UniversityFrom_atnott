a = int(input())
b = int(input())

l = []

for i in range(a, b+1):
    if i%3==0:
        l.append(i)

print(sum(l)/len(l))
