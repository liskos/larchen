k=0
for s1 in "КЛОУН":
    for s2 in "КЛОУН":
        for s3 in "КЛОУН":
            for s4 in "КЛОУН":
                s=s1+s2+s3+s4
                if s.count("У")>=1:
                    k+=1
print(k)