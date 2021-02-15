a = []
for s1 in "ЕЖЗИК":
    for s2 in "ЕЖЗИК":
        for s3 in "ЕЖЗИК":
            s = s1 + s2 + s3
            k = s.count("Ж")+s.count("З")+s.count("К")
            if k == 1:
                a.append(s)
print(a)
print(len(a))
