k=0
for s1 in "КРАНТ":
    for s2 in "КРАНТ":
        for s3 in "КРАНТ":
            for s4 in "КРАНТ":
                for s5 in "КРАНТ":
                    s=s1+s2+s3+s4+s5
                    if s.count("К")==2:
                        k+=1
print(k)