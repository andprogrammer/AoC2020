# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

def password_validator(left, letter, data):
    return data.count(letter) >= left


# First solution
def get_num_of_valid_passwords(data):
    valid_passwords = 0
    for k, v in data.items():
        if password_validator(k[0], k[2], v):
            valid_passwords = valid_passwords + 1
    return valid_passwords


# Second solution
def get_num_of_valid_passwords_v2(data):
    return [True for k, v in data.items() if password_validator(k[0], k[2], v)].count(True)


def main():
    data = {(1, 3, 'a'): 'abcde', (1, 3, 'b'): 'cdefg', (2, 9, 'c'): 'ccccccccc'}
    assert 2 == get_num_of_valid_passwords(data)
    assert 2 == get_num_of_valid_passwords_v2(data)


if __name__ == '__main__':
    main()
