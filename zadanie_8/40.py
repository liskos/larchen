k=0
for s1 in "ABC":
    for s2 in "ABC":
        for s3 in "ABCX":
            for s4 in "ABC":
                for s5 in "X":
                    s=s1+s2+s3+s4+s5
                    k+=1
print(k)