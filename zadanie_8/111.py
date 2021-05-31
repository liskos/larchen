k=0
for s1 in "асберг":
    for s2 in "айсберг":
        for s3 in "айсберг":
            for s4 in "айсберг":
                for s5 in "айсберг":
                    for s6 in "айсберг":
                        for s7 in "айсберг":
                            s=s1+s2+s3+s4+s5+s6+s7
                            if (len(set(s))==7) and ("йб" not in s) and ("йс" not in s) and ("йр" not in s) and ("йг" not in s):
                                k+=1
print(k)