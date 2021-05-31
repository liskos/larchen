k=0
for s1 in "СИРОП":
    for s2 in "СИРОП":
        for s3 in "СИРОП":
            for s4 in "СИРОП":
                for s5 in "СИРОП":
                    s=s1+s2+s3+s4+s5
                    if s.count("О")== 1 and "СО" in s or "РО" in s or "ПО" in s:
                        k += 1
print(k)