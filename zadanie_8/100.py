k=0
for s1 in "ПАНЕЛ":
    for s2 in "ПАНЕЛЬ":
        for s3 in "ПАНЕЛЬ":
            for s4 in "ПАНЕЛЬ":
                for s5 in "ПАНЕЛЬ":
                    for s6 in "ПАНЕЛЬ":
                        s=s1+s2+s3+s4+s5+s6
                        if (len(set(s))==6) and ("ЕАП" not in s):
                            k+=1
print(k)