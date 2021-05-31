k=0
for s1 in "КРОТ":
    for s2 in "КРОТ":
        for s3 in "КРОТ":
            for s4 in "КРОТ":
                for s5 in "КРОТ":
                    for s6 in "КРОТ":
                        s=s1+s2+s3+s4+s5+s6
                        if s.count("О")==1:
                            k+=1
print(k)