k=0
for s1 in "пескар":
    for s2 in "пескарь":
        for s3 in "пескарь":
            for s4 in "пескарь":
                for s5 in "пескарь":
                    for s6 in "пескарь":
                        for s7 in "пескарь":
                            s=s1+s2+s3+s4+s5+s6+s7
                            if (len(set(s))==7) and ("ье" not in s) and ("ьа" not in s) and ("ьр" not in s):
                                k+=1
print(k)