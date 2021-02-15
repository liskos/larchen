k = 0
for x in range(1016,7938):
    if x%3==0 and x%7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 !=0:
        k+=1
        print(x)
print(k)
