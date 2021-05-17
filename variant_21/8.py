k = 0
for s1 in "КАН":
    for s2 in "КАН":
        for s3 in "КАН":
            for s4 in "КАН":
                for s5 in "КАН":
                    for s6 in "КАН":
                        s=s1+s2+s3+s4+s5+s6
                        if s.count("К")+s.count("Н") >= 3:
                            k += 1
                            print(s)
print(k)