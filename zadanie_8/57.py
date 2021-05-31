k=0
for s1 in "ПИРОГ":
    for s2 in "ПИРОГ":
        for s3 in "ПИРОГ":
            for s4 in "ПИРОГ":
                for s5 in "ПИРОГ":
                    for s6 in "ПИРОГ":
                        s=s1+s2+s3+s4+s5+s6
                        if s.count("Р")== 1 and ("РИ" in s or "РО" in s):
                            k += 1
print(k)