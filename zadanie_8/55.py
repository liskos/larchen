k=0
for s1 in "ЖИРАФ":
    for s2 in "ЖИРАФ":
        for s3 in "ЖИРАФ":
            for s4 in "ЖИРАФ":
                for s5 in "ЖИРАФ":
                    for s6 in "ЖИРАФ":
                        s=s1+s2+s3+s4+s5+s6
                        if s.count("А") >= 1 and s.count("А") <= 4:
                            k += 1
print(k)