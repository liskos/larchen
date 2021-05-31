k=0
for s1 in "вентил":
    for s2 in "вентиль":
        for s3 in "вентиль":
            for s4 in "вентиль":
                for s5 in "вентиль":
                    for s6 in "вентиль":
                        for s7 in "вентиль":
                            s=s1+s2+s3+s4+s5+s6+s7
                            if (len(set(s))==7) and ("еьи" not in s) and ("иье" not in s):
                                k+=1
print(k)