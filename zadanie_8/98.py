k=0
for s1 in "ГЕЛИ":
    for s2 in "ГЕЛИЙ":
        for s3 in "ГЕЛИЙ":
            for s4 in "ГЕЛИЙ":
                for s5 in "ГЕЛИЙ":
                    s=s1+s2+s3+s4+s5
                    if (len(set(s))==5) and ("ИЕЙ" not in s):
                        k+=1
print(k)