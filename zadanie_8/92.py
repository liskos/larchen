k=0
for s1 in "МАНК":
    for s2 in "МАНОК":
        for s3 in "МАНОК":
            for s4 in "МАНОК":
                for s5 in "МАНОК":
                    s=s1+s2+s3+s4+s5
                    if (len(set(s))==5) and ("АО" not in s):
                        k+=1
print(k)