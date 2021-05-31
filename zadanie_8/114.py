k=0
for s1 in "абак":
    for s2 in "абак":
        for s3 in "абак":
            for s4 in "абак":
                s=s1+s2+s3+s4
                if "аа" not in s and "бб" not in s and "кк" not in s:
                    k+=1
print(k)