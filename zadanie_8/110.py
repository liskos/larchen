k=0
for s1 in "рулка":
    for s2 in "рулька":
        for s3 in "рулька":
            for s4 in "рулька":
                for s5 in "рулька":
                    for s6 in "рулька":
                        s=s1+s2+s3+s4+s5+s6
                        if (len(set(s))==6) and ("уь" not in s) and ("аь" not in s):
                            k+=1
print(k)