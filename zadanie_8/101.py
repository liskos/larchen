k=0
for s1 in "ШАНЕЛ":
    for s2 in "ШАНЕЛЬ":
        for s3 in "ШАНЕЛЬ":
            for s4 in "ШАНЕЛЬ":
                for s5 in "ШАНЕЛЬ":
                    for s6 in "ШАНЕЛЬ":
                        s=s1+s2+s3+s4+s5+s6
                        if (len(set(s))==6) and ("ЕАЬ" not in s):
                            k+=1
print(k)