k=0
for s1 in "НИЧЯ":
    for s2 in "НИЧЬЯ":
        for s3 in "НИЧЬЯ":
            for s4 in "НИЧЬЯ":
                for s5 in "НИЧЬЯ":
                    s=s1+s2+s3+s4+s5
                    if (len(set(s))==5) and ("ЬИЯ" not in s):
                        k+=1
print(k)