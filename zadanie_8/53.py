k=0
for s1 in "МУХА":
    for s2 in "МУХА":
        for s3 in "МУХА":
            for s4 in "МУХА":
                for s5 in "МУХА":
                    s=s1+s2+s3+s4+s5
                    if s.count("У")>=1 and s.count("У")<=3:
                        k+=1
print(k)