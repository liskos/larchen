k = 0
for s1 in "ЕИКНУ":
    for s2 in "ЕИКНУ":
        for s3 in "ЕИКНУ":
            s = s1 + s2 + s3
            k += 1
            print(k, s)