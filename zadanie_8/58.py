k=0
for s1 in "ПИРОГ":
    for s2 in "ПИРОГ":
        for s3 in "ПИРОГ":
            for s4 in "ПИРОГ":
                s=s1+s2+s3+s4
                if s.count("О")==2 and ("ПО" in s or "РО" in s or "ГО" in s):
                    k += 1
print(k)