k=0
for s1 in "КАЛИ":
    for s2 in "КАЛИЙ":
        for s3 in "КАЛИЙ":
            for s4 in "КАЛИЙ":
                for s5 in "КАЛИЙ":
                    s=s1+s2+s3+s4+s5
                    if (len(set(s))==5) and ("ИА" not in s):
                        k+=1
print(k)