def get_status(i, j, arr):
    if not arr or i < 0 or i >= len(arr[0]) or j < 0 or j >= len(arr):
        return -1
    return arr[i][j]


def get_adjacent(i, j, arr):
    c = 0
    c = get_counter(arr, c, i - 1, j - 1)
    c = get_counter(arr, c, i - 1, j)
    c = get_counter(arr, c, i - 1, j + 1)
    c = get_counter(arr, c, i, j - 1)
    c = get_counter(arr, c, i, j + 1)
    c = get_counter(arr, c, i + 1, j - 1)
    c = get_counter(arr, c, i + 1, j)
    c = get_counter(arr, c, i + 1, j + 1)
    return c


def get_counter(arr, c, i, j):
    if get_status(i, j, arr) != -1:
        c += 1 if get_status(i, j, arr) == '#' else 0
    return c


def seats():
    with open('seats') as file:
        data = file.read()
    s = []
    for i in data.split():
        s.append(i)
    copy = [row[:] for row in s]
    c = 0
    status = True
    while status:
        for i in range(len(s)):
            for j in range(len(s[0])):
                if s[i][j] == 'L':
                    if get_adjacent(i, j, s) == 0:
                        status = False
                        copy[i] = copy[i][:j] + '#' + copy[i][j + 1:]
                elif s[i][j] == '#':
                    if get_adjacent(i, j, s) >= 4:
                        status = False
                        copy[i] = copy[i][:j] + 'L' + copy[i][j + 1:]
        # print('Print seats')
        # for i in copy:
        #     print(i)
        c += 1
        if not status:
            status = True
            s = [row[:] for row in copy]
        else:
            status = False
    return c


def main():
    assert 6 == seats()


if __name__ == '__main__':
    main()
