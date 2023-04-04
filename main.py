import math

k = 5
arr = []

for i in range(1, k+1):
    arr.append(math.sin(i))

posit_count = 0
negat_count = 0

for num in arr:
    if num>0:
        posit_count+=1
    elif num<0:
        negat_count+=1

print(posit_count)
print(negat_count)