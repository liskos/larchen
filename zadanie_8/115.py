k=0
for s1 in "марта":
    for s2 in "марта":
        for s3 in "марта":
            for s4 in "марта":
                for s5 in "марта":
                        s=s1+s2+s3+s4+s5
                        if "аа" not in s and "мм" not in s  and "рр" not in s  and "тт" not in s:
                            k+=1
print(k)