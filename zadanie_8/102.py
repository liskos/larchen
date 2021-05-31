k=0
for s1 in "НИГРЛ":
    for s2 in "НИГРОЛ":
        for s3 in "НИГРОЛ":
            for s4 in "НИГРОЛ":
                for s5 in "НИГРОЛ":
                    for s6 in "НИГРОЛ":
                        s=s1+s2+s3+s4+s5+s6
                        if (len(set(s))==6) and ("ОИГ" not in s):
                            k+=1
print(k)
