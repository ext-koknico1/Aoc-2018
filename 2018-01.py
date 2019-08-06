result = 0

with open('2018-01.input', 'r') as f:
    for line in f:
        result += int(line)

print 'Part One :' + repr(result)
assert result == 531

result = 0
repeated_frequency = None
frequencies = {}
while True:
    with open('2018-01.input', 'r') as f:
        for line in f:
            result += int(line)
            if frequencies.get(result, None) is not None:
                repeated_frequency = result
                break
            else:
                frequencies[result] = True
    if repeated_frequency is not None:
        break

print "Part 2 : " + repr(repeated_frequency)
assert repeated_frequency == 76787