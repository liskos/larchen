k=0
for s1 in "КОМБАН":
    for s2 in "КОМБАЙН":
        for s3 in "КОМБАЙН":
            for s4 in "КОМБАЙН":
                for s5 in "КОМБАЙН":
                    for s6 in "КОМБАЙН":
                        for s7 in "КОМБАЙН":
                            s=s1+s2+s3+s4+s5+s6+s7
                            if (len(set(s))==7) and ("АЙ" not in s):
                                k+=1
print(k)