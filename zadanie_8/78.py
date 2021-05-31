k = 0
for s1 in "АИОУЭ":
    for s2 in "АИОУЭ":
        for s3 in "АИОУЭ":
            for s4 in "АИОУЭ":
                s = s1 + s2 + s3 + s4
                k += 1
                print(k, s)