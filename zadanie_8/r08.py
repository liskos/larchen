k=0
for s1 in "УЛЕ":
    for s2 in "УЛЕЙ":
        for s3 in "УЛЕЙ":
            for s4 in "УЛЕЙ":
                s=s1+s2+s3+s4
                if ("ЕУ" not in s) and (len(set(s))==4):
                    k+=1
print(k)