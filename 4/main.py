# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in

def passports_validator():
    with open('passport.txt') as file:
        data = file.read()
    counter = 0
    for x in data.split('\n\n'):
        if one_password_validator(x):
            counter = counter + 1
    return counter


def one_password_validator(pc):
    parted = pc.split()
    key_value = [x.split(':') for x in parted]
    password_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}
    for x in key_value:
        if x[0] in password_fields:
            password_fields.remove(x[0])
    return len(password_fields.difference({'cid'})) == 0


def main():
    assert 2 == passports_validator()


if __name__ == '__main__':
    main()
