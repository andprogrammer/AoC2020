import math


def get_position(row_code, start_index, stop_index, starting_partition_name):
    if len(row_code) == 1:
        return start_index if row_code[0] == starting_partition_name else stop_index
    letter = row_code[0]
    difference = math.ceil((stop_index - start_index) / 2)
    if letter == starting_partition_name:
        stop_index = stop_index - difference
    else:
        start_index = start_index + difference
    return get_position(row_code[1:], start_index, stop_index, starting_partition_name)


def get_seat_number(code):
    row_code = code[0:7]
    column_code = code[7:10]
    row = get_position(row_code, 0, 127, 'F')
    column = get_position(column_code, 0, 7, 'L')
    return row * 8 + column


def main():
    assert 357 == get_seat_number('FBFBBFFRLR')
    assert 567 == get_seat_number('BFFFBBFRRR')
    assert 119 == get_seat_number('FFFBBBFRRR')
    assert 820 == get_seat_number('BBFFBBFRLL')


if __name__ == '__main__':
    main()
