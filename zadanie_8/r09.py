k=0
for s1 in "ВУАЛ":
    for s2 in "ВУАЛЬ":
        for s3 in "ВУАЛЬ":
            for s4 in "ВУАЛЬ":
                for s5 in "ВУАЛЬ":
                    s=s1+s2+s3+s4+s5
                    if (len(set(s))==5) and ("ЬУ" not in s) and ("ЬА" not in s):
                        k+=1
print(k)