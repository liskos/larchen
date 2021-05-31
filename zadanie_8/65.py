k = 0
for s1 in "АБВГДЯ":
    for s2 in "АБВГД":
        for s3 in "АБВГД":
            for s4 in "АБВГДЯ":
                for s5 in "АБВГДЯ":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("Я")==1:
                        k += 1
print(k)