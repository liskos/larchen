k=0
for s1 in "НАДПИС":
    for s2 in "НАДПИСЬ":
        for s3 in "НАДПИСЬ":
            for s4 in "НАДПИСЬ":
                for s5 in "НАДПИСЬ":
                    for s6 in "НАДПИСЬ":
                        for s7 in "НАДПИСЬ":
                            s=s1+s2+s3+s4+s5+s6+s7
                            if (len(set(s))==7) and ("ЬИА" not in s):
                                k+=1
print(k)
