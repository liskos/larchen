k=0
for s1 in "КОМАР":
    for s2 in "КОМАР":
        for s3 in "КОМАР":
            for s4 in "КОМАР":
                s=s1+s2+s3+s4
                if s.count("А")<=3:
                    k+=1
print(k)