k = 0
for s1 in "ЗАПИСЬ":
    for s2 in "ЗАПИСЬ":
        for s3 in "ЗАПИСЬ":
            for s4 in "ЗАПИСЬ":
                for s5 in "ЗАПИСЬ":
                    for s6 in "ЗАПИСЬ":
                        s= s1 + s2 + s3 + s4 + s5 + s6
                        if s1 != 'Ь' in s:
                            k+=1
print(k)