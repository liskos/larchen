k = 0
for s1 in "АВДПРА":
    for s2 in "АВДПРА":
        for s3 in "АВДПРА":
            for s4 in "АВДПРА":
                s= s1 + s2 + s3 + s4
                if "А" in s :
                    k+=1
                    break
print(k)