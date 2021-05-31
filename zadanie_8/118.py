k=0
for s1 in "аврора":
    for s2 in "аврора":
        for s3 in "аврора":
            for s4 in "аврора":
                for s5 in "аврора":
                    for s6 in "аврора":
                        s=s1+s2+s3+s4+s5+s6
                        if "аа" not in s and "рр" not in s and "оо" not in s and "вв" not in s:
                            k+=1
print(k)