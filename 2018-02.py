count_2 = 0
count_3 = 0
result = None

def counter(s):
    counts = []
    for letter in s:
        counts.append(s.count(letter))
    return any((c == 2 for c in counts)), any((c == 3 for c in counts))


with open('2018-02.input', 'r') as f:
    for line in f:
        data = counter(line)
        if data[0]:
            count_2 += 1
        if data[1]:
            count_3 += 1

result = count_2*count_3
print "Part 1 : " + repr(result)
assert result == 5681

result = None

studied_strings = []
with open('2018-02.input', 'r') as f:
    for line in f:
        if len(studied_strings) == 0:
            studied_strings.append(line)
        else:
            for studied_string in studied_strings:
                diff, pos, first_diff = 0, 0, 0
                for twins in zip(studied_string, line):
                    if twins[0] != twins[1]:
                        diff += 1
                        if diff > 1:
                            break
                        first_diff = pos
                    pos += 1
                if diff == 1:
                    result = list(line)
                    result.pop(first_diff)
                    result = ''.join(result).replace('\n', '')
                    break
        if result is not None:
            break
        else:
            studied_strings.append(line)

print "Part 2 : " + repr(result)
assert result == 'uqyoeizfvmbistpkgnocjtwld'
