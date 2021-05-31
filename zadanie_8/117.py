k=0
for s1 in "кабала":
    for s2 in "кабала":
        for s3 in "кабала":
            for s4 in "кабала":
                for s5 in "кабала":
                    for s6 in "кабала":
                        s=s1+s2+s3+s4+s5+s6
                        if "аа" not in s and "кк" not in s and "бб" not in s  and "лл" not in s:
                            k+=1
print(k)