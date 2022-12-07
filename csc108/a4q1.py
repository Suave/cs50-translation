a = input().split(" ")

min = 10**9

for idx, x in enumerate(a):
    if idx == len(a)-1:
        break
    
    difficulty = abs(int(x) - int(a[idx+1]))
    if min > difficulty:
        min = difficulty

print("smallest is", min)