def solve(data):
    c = 0
    for line in data:
        digits = line[0].split(" ")
        output = line[1].split(" ")

        dm = {}
        segment = {}
        char = {
            'a': [],
            'b': [],
            'c': [],
            'd': [],
            'e': [],
            'f': [],
            'g': [],
        }
        # find easy digits, map segment occurrences in digits
        for d in digits:
            if len(d) == 2:
                dm['1'] = sorted(d)
            elif len(d) == 3:
                dm['7'] = sorted(d)
            elif len(d) == 4:
                dm['4'] = sorted(d)
            elif len(d) == 7:
                dm['8'] = sorted(d)
            for x in d:
                char[x].append(d)

        # map segments
        for k, v in char.items():
            if len(v) == 6:
                segment[k] = 2
                segment[2] = k
            elif len(v) == 4:
                segment[k] = 5
                segment[5] = k
            elif len(v) == 9:
                segment[k] = 6
                segment[6] = k
            elif len(v) == 8:
                if k not in dm['1']:
                    segment[k] = 1
                    segment[1] = k
                else:
                    segment[k] = 3
                    segment[3] = k
            elif len(v) == 7:
                if k in dm['4']:
                    segment[k] = 4
                    segment[4] = k
                else:
                    segment[k] = 7
                    segment[7] = k
        # find hard digits
        for d in digits:
            if len(d) == 5:
                if segment[2] in d:
                    dm['5'] = sorted(d)
                elif segment[5] in d:
                    dm['2'] = sorted(d)
                else:
                    dm['3'] = sorted(d)
            elif len(d) == 6:
                if segment[3] not in d:
                    dm['6'] = sorted(d)
                elif segment[4] not in d:
                    dm['0'] = sorted(d)
                elif segment[5] not in d:
                    dm['9'] = sorted(d)
        out = []
        for d in output:
            for k, v in dm.items():
                if ''.join(sorted(d)) == ''.join(v):
                    out.append(k)
        c += int(''.join(out))
    return c


with open('data') as f:
    data = [x.split(" | ") for x in f.read().split("\n")]
    print(solve(data))
