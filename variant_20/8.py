k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    for s6 in "01234567":
                        for s7 in "01234567":
                            s = s1+s2+s3+s4+s5+s6+s7
                            if len(set(s)) == 7 and (int(s1)%2 != int(s2)%2) and (int(s2)%2 != int(s3)%2) and (int(s3)%2 != int(s4)%2) and (int(s4)%2 != int(s5)%2) and (int(s5)%2 != int(s6)%2)  and (int(s6)%2 != int(s7)%2):
                                k += 1
print(k)
