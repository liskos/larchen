k=0
for s1 in "ABC":
    for s2 in "ABC":
        for s3 in "ABC":
            for s4 in "ABC":
                for s5 in "abcX":
                    s=s1+s2+s3+s4+s5
                    k+=1
print(k)