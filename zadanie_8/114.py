a = []
for s1 in "абак":
    for s2 in "абак":
        for s3 in "абак":
            for s4 in "абак":
                s=s1+s2+s3+s4
                if "аа" not in s and (len(set(s))==3) and s.count("а")==2:
                    a.append(s)

print(len(set(a)))