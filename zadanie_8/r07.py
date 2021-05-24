k=0
for s1 in "ВЕСНА":
    for s2 in "ВЕСНА":
        for s3 in "ВЕСНА":
            s=s1+s2+s3
            if s.count("А")>=1:
                k+=1
print(k)