k=0
for s1 in "КАТЕР":
    for s2 in "КАТЕР":
        for s3 in "КАТЕР":
            for s4 in "КАТЕР":
                s=s1+s2+s3+s4
                if s.count("Р")>=2:
                    k+=1
print(k)