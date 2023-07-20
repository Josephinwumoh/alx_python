#!/usr/bin/python3
for p in range(0, 9):
    for w in range(1, 10):
        if p >= w:
            continue
        elif p == 8 and w == 9:
            print("{}{}".format(p, w))
        else:
             print("{}{}".format(p, w), end= ",")


        