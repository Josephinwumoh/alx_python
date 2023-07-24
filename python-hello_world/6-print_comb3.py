
for p in range(0, 10):
    for w in range(p+1, 10):
        if p >= w:
            continue
        elif p == 8 and w == 9:
            print("{}{}".format(p, w))
        else:
             print("{}{}".format(p, w), end= ", ")

