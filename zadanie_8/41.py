k=0
for s1 in "КРАН":
    for s2 in "КРАН":
        for s3 in "КРАН":
            s=s1+s2+s3
            if s.count("А")>=1:
                k+=1
print(k)