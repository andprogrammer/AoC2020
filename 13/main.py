def get_shift(timestamp, service):
    return service - (timestamp % service)


def get_earliest_shuttle():
    with open('note.txt') as file:
        timestamp = int(file.readline())
        data = file.read()
    services = [int(i) for i in data.split(',') if i != 'x']
    service, shift = 9999, 9999
    for i in services:
        if get_shift(timestamp, i) < shift:
            service = i
            shift = get_shift(timestamp, i)
    return service * shift


def main():
    assert 295 == get_earliest_shuttle()


if __name__ == '__main__':
    main()
