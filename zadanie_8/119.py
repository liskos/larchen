k=0
for s1 in "магистр":
    for s2 in "магистр":
        for s3 in "магистр":
            for s4 in "магистр":
                for s5 in "магистр":
                        s=s1+s2+s3+s4+s5
                        if s.count("а")+s.count("и")==1:
                            k+=1
print(k)