k = 0
for s1 in "АБВГДЯ":
    for s2 in "АБВДЕ":
        for s3 in "АБВДЕ":
            for s4 in "АБВГДЕ":
                s = s1 + s2 + s3 + s4
                if s.count("Е")==1:
                    k += 1
print(k)