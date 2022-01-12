def get_parsed_input(file):
    d = {}
    with open(file) as f:
        mask = f.readline()[7:].strip()
        for line in f:
            start = line.find('[') + 1
            end = line.find(']')
            mem_address = line[start:end]
            value = int(line.split('=')[1].strip())
            d[mem_address] = value
    return mask, d


def get_binary(n):
    out = []
    while n:
        out.insert(0, n & 1)
        n = n // 2
    return out


def get_binary2(n):
    if not n:
        return []
    return get_binary2(n // 2) + [n & 1]


def get_extended(l, expected_size):
    return (expected_size - len(l)) * [0] + l


def get_decimal(l, i):
    if not l:
        return 0
    return l[-1] * (2 ** i) + get_decimal(l[:-1], i + 1)


def get_masked(n, mask):
    bits = get_binary2(n)
    extended_bits = get_extended(bits, 36)
    splitted_mask = [x for x in mask]
    output = []
    for x, y in zip(extended_bits, splitted_mask):
        if y == 'X':
            output.append(int(x))
        elif y == '0':
            output.append(0)
        else:
            output.append(1)
    return output


def apply_mask(mem, mask):
    output = {}
    for k, v in mem.items():
        output[k] = get_decimal(get_masked(v, mask), 0)
    return sum(output.values())


def main():
    out = get_parsed_input('mask.txt')
    assert 165 == apply_mask(out[1], out[0])


if __name__ == '__main__':
    main()
