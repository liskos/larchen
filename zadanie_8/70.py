k = 0
for s1 in "АБВГ":
    for s2 in "АБВ":
        for s3 in "АБВ":
            for s4 in "АБВ":
                for s5 in "АБВГ":
                    s = s1 + s2 + s3 + s4
                    if s.count("Г")<=1:
                        k += 1
print(k)