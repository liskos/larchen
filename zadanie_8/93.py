k=0
for s1 in "ПАЩИК":
    for s2 in "ПАЙЩИК":
        for s3 in "ПАЙЩИК":
            for s4 in "ПАЙЩИК":
                for s5 in "ПАЙЩИК":
                    for s6 in "ПАЙЩИК":
                        s=s1+s2+s3+s4+s5+s6
                        if (len(set(s))==6) and ("ИА" not in s):
                            k+=1
print(k)