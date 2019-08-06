def idps(data, search, offset=0):
    if len(data) == 0:
        return -1
    pos = max(0, len(data) // 2)
    if data[pos] < search:
        return idps(data[pos + 1:], search, pos+offset+1)
    elif data[pos] > search:
        return idps(data[:pos], search, offset)
    else:
        return pos + offset


assert idps([], 1) == -1
assert idps([2], 2) == 0
assert idps([2], 1) == -1
assert idps([2], 3) == -1
assert idps([2, 4], 2) == 0
assert idps([2, 4], 4) == 1
assert idps([2, 4], 1) == -1
assert idps([2, 4], 3) == -1
assert idps([2, 4], 5) == -1
assert idps([0, 1, 16, 17], 5) == -1
assert idps([2, 3, 5, 10, 16, 17], 2) == 0
assert idps([2, 3, 5, 10, 16, 17], 3) == 1
assert idps([2, 3, 5, 10, 16, 17], 5) == 2
assert idps([2, 3, 5, 10, 16, 17], 10) == 3
assert idps([2, 3, 5, 10, 16, 17], 16) == 4
assert idps([2, 3, 5, 10, 16, 17], 17) == 5
assert idps([2, 3, 5, 10, 16, 17], 1) == -1
assert idps([2, 3, 5, 10, 16, 17], 18) == -1
assert idps([2, 3, 5, 10, 16, 17], 4) == -1

ints = range(1000)
for i in ints:
    assert idps(ints, i) == i
