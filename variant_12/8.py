k = 0
for s1 in "АБВГ":
    for s2 in "АБВГ":
        for s3 in "АБВГ":
            for s4 in "АБВГ":
                s = s1 + s2 + s3 + s4
                if s1 != 'Г':
                    k+=1
print(k)