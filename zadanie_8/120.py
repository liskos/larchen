k=0
for s1 in "приказ":
    for s2 in "приказ":
        for s3 in "приказ":
            for s4 in "приказ":
                s=s1+s2+s3+s4
                if s.count("а")+s.count("и")<=1:
                    k+=1
print(k)