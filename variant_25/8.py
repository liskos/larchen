k = 0
for s1 in "ежзи":
    for s2 in "ежзи":
        for s3 in "ежзи":
            for s4 in "ежзи":
                s = s1 + s2 + s3 + s4
                if s.count("е")+s.count("и")==1:
                    k+=1
print(k)
