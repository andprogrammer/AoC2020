def get_accumulator_recursion(index, instructions, visited, accumulator):   # function with recursion
    if index < len(instructions):
        if index not in visited:
            visited.append(index)
            k = instructions[index].split(' ')[0]
            v = instructions[index].split(' ')[1]
            if k == 'acc':
                accumulator += int(v) if str(v[0]) == '-' else int(v[1:])
                index += 1
            elif k == 'nop':
                index += 1
            elif k == 'jmp':
                index += int(v) if str(v[0]) == '-' else int(v[1:])
            return get_accumulator_recursion(index, instructions, visited, accumulator)
        else:
            return accumulator
    else:
        return


def get_accumulator():
    with open('boot_code') as file:
        data = file.read()
    instructions = data.split('\n')
    visited = []
    accumulator = 0
    index = 0

    # return get_accumulator_recursion(index, instructions, visited, accumulator)
    while True:
        if index < len(instructions):
            if index not in visited:
                visited.append(index)
                k = instructions[index].split(' ')[0]
                v = instructions[index].split(' ')[1]
                if k == 'acc':
                    accumulator += int(v) if str(v[0]) == '-' else int(v[1:])
                    index += 1
                elif k == 'nop':
                    index += 1
                elif k == 'jmp':
                    index += int(v) if str(v[0]) == '-' else int(v[1:])
            else:
                return accumulator
        else:
            break


def main():
    assert 5 == get_accumulator()


if __name__ == '__main__':
    main()
