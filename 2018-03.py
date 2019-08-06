import re

motif_regex = re.compile('#(\d+)\s+@\s(\d+),(\d+):\s+(\d+)x(\d+)')

with open('2018-03.input', 'r') as f:
    fabric = {}
    for line in f:
        matches = motif_regex.match(line)

        start_x, start_y, len_x, len_y = matches.group(2, 3, 4, 5)

        for x in range(int(start_x), int(start_x) + int(len_x)):
            for y in range(int(start_y), int(start_y) + int(len_y)):
                fabric['{}:{}'.format(x, y)] = fabric.get('{}:{}'.format(x, y), 0) + 1

    #def moreThanJuan

    print "First part : " + repr(len(filter(lambda coord: coord >= 2, fabric.values())))

