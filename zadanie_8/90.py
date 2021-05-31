k=0
for s1 in "КРО":
    for s2 in "КРОЙ":
        for s3 in "КРОЙ":
            for s4 in "КРОЙ":
                s=s1+s2+s3+s4
                if (len(set(s))==4) and ("ОЙ" not in s):
                        k+=1
print(k)