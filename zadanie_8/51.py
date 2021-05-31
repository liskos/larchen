k=0
for s1 in "КАТЕР":
    for s2 in "КАТЕР":
        for s3 in "КАТЕР":
            for s4 in "КАТЕР":
                for s5 in "КАТЕР":
                    s=s1+s2+s3+s4+s5
                    if s.count("Р")>=2:
                        k+=1
print(k)