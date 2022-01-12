# 1721
# 979
# 366
# 299
# 675
# 1456

def two_numbers(data, expNumber):
    if not data:
        return 0
    data.sort()
    b = 0
    e = len(data) - 1
    while b != e:
        if data[b] + data[e] == expNumber:
            return data[b] * data[e]
        if data[b] + data[e] < expNumber:
            b = b + 1
        else:
            e = e - 1
    return 0


def main():
    numbers = [1721, 979, 366, 299, 675, 1456]
    assert two_numbers(numbers, 2020) == 514579


if __name__ == '__main__':
    main()
