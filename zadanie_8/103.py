k=0
for s1 in "КУПИХА":
    for s2 in "КУПЧИХА":
        for s3 in "КУПЧИХА":
            for s4 in "КУПЧИХА":
                for s5 in "КУПЧИХА":
                    for s6 in "КУПЧИХА":
                        for s7 in "КУПЧИХА":
                            s=s1+s2+s3+s4+s5+s6 +s7
                            if (len(set(s))==7) and ("ИАУ" not in s):
                                k+=1
print(k)
