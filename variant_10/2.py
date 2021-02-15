for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = (not x or not y) and not(y == z) and not w
                if f:
                    print(z, y, x, w, "|", int(f))
