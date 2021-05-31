k=0
for s1 in "БАЛКОН":
    for s2 in "БАЛКОН":
        for s3 in "БАЛКОН":
            for s4 in "БАЛКОН":
                for s5 in "БАЛКОН":
                    s=s1+s2+s3+s4+s5
                    if s.count("Б")>=1:
                        k+=1
print(k)