k=0
for s1 in "abcd":
    for s2 in "abcd":
        for s3 in "abcd":
                s=s1+s2+s3
                if ( ("ad" in s) or ("da" in s) ) and ("bc" not in s) and ("cb" not in s):
                    k+=1
                    print(k,s)