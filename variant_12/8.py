k = 0
for s1 in "АБВГ":
    for s2 in "АБВГ":
        for s3 in "АБВГ":
            s = s1 + s2 + s3
            k += 1
            print(k, s)