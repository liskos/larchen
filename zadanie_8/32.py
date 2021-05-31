k=0
for s1 in "abed":
    for s2 in "abed":
        for s3 in "abed":
                s=s1+s2+s3
                if "ad" in s or "da" in s:
                    k+=1
print(k,s)