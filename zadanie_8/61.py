k = 0
for s1 in "ЭЮЯ":
    for s2 in "АБВГД":
        for s3 in "АБВГД":
            for s4 in "АБВГД":
                for s5 in "ЭЮЯ":
                    s = s1 + s2 + s3 + s4 + s5
                    k += 1
                    print(k, s)