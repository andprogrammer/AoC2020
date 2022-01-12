from enum import Enum


class Ship:
    class Direction(Enum):
        N = 0
        S = 1
        E = 2
        W = 3
    n = 0
    s = 0
    e = 0
    w = 0
    curr_dir = Direction.E


def get_splitted_instruction(instruction):
    return instruction[0], int(instruction[1:])


def get_direction(instruction, curr_direction):
    direction, degree = get_splitted_instruction(instruction)[0], get_splitted_instruction(instruction)[1]
    rotate = int(degree / 90) % 4   # handle directions like R90, L270, R180, L360
    if rotate == 0:
        return direction
    if curr_direction == Ship.Direction.E:
        if rotate == 1:
            return Ship.Direction.S if direction == 'R' else Ship.Direction.N
        elif rotate == 2:
            return Ship.Direction.W
        else:   # rotate 3
            return Ship.Direction.N if direction == 'R' else Ship.Direction.S
    elif curr_direction == Ship.Direction.S:
        if rotate == 1:
            return Ship.Direction.W if direction == 'R' else Ship.Direction.E
        elif rotate == 2:
            return Ship.Direction.N
        else:   # rotate 3
            return Ship.Direction.E if direction == 'r' else Ship.Direction.W
    elif curr_direction == Ship.Direction.W:
        if rotate == 1:
            return Ship.Direction.N if direction == 'R' else Ship.Direction.S
        elif rotate == 2:
            return Ship.Direction.E
        else:   # rotate 3
            return Ship.Direction.S if direction == 'R' else Ship.Direction.N
    elif curr_direction == Ship.Direction.N:
        if rotate == 1:
            return Ship.Direction.E if direction == 'R' else Ship.Direction.W
        elif rotate == 2:
            return Ship.Direction.S
        else:   # rotate 3
            return Ship.Direction.W if direction == 'R' else Ship.Direction.E


def handle_instruction(ship, instructions):
    if not instructions:
        return ship.n, ship.s, ship.e, ship.w

    instruction = instructions[0]
    if get_splitted_instruction(instruction)[0] == 'N':
        ship.n += int(get_splitted_instruction(instruction)[1])
    if get_splitted_instruction(instruction)[0] == 'S':
        ship.s += int(get_splitted_instruction(instruction)[1])
    if get_splitted_instruction(instruction)[0] == 'E':
        ship.e += int(get_splitted_instruction(instruction)[1])
    if get_splitted_instruction(instruction)[0] == 'W':
        ship.w += int(get_splitted_instruction(instruction)[1])

    if get_splitted_instruction(instruction)[0] == 'L' or get_splitted_instruction(instruction)[0] == 'R':
        ship.curr_dir = get_direction(instruction, ship.curr_dir)

    if get_splitted_instruction(instruction)[0] == 'F':
        move = get_splitted_instruction(instruction)[1]

        if ship.curr_dir == Ship.Direction.S:
            if ship.n - move < 0:
                ship.s += abs(ship.n - move)
                ship.n = 0
            else:
                ship.n -= move
        elif ship.curr_dir == Ship.Direction.W:
            if ship.e - move < 0:
                ship.w += abs(ship.e - move)
                ship.e = 0
            else:
                ship.e -= move
        elif ship.curr_dir == Ship.Direction.N:
            if ship.s - move < 0:
                ship.n += abs(ship.s - move)
                ship.s = 0
            else:
                ship.s -= move
        else:
            if ship.w - move < 0:
                ship.e += abs(ship.w - move)
                ship.w = 0
            else:
                ship.w -= move
    return handle_instruction(ship, instructions[1:])


def handle_ship():
    with open('instruction') as file:
        data = file.read()
    instructions = []
    for i in data.split('\n'):
        instructions.append(i.replace('\n', ''))

    ship = Ship
    return sum(handle_instruction(ship, instructions))


def main():
    assert 25 == handle_ship()


if __name__ == '__main__':
    main()
