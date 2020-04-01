# BY TANISHQ GUPTA
# INPUT_FORM dog, deer, deal
# de
l = list(map(str, input().split())); s = input()
k= []
for i in l:
    if i.find(s) == 0:
        k.append(i)
print(*k)