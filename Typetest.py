import time

lst = []
lst2 = []
scr = []
for _ in range(int(input())):
    name = input()
    score = float(input())

    lst2.append(name)
    lst2.append(score)
    lst.append(lst2)
    lst2 = []
start = time.time()
for i in range(len(lst)):
    scr.append((lst[i][1]))
for k in range(scr.count(min(scr))):
    scr.remove(min(scr))
lst.sort()
for j in range(len(lst)):
    if str(min(scr)) == str(lst[j][1]):
        print(lst[j][0])

stop = time.time()

print(stop-start)