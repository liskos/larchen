k=0
for s1 in "аджика":
    for s2 in "аджика":
        for s3 in "аджика":
            for s4 in "аджика":
                for s5 in "аджика":
                    for s6 in "аджика":
                        s=s1+s2+s3+s4+s5+s6
                        if "аа" not in s and "дд" not in s and "жж" not in s  and "ии" not in s and "кк" not in s:
                            k+=1
print(k)