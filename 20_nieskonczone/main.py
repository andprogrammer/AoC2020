class Tile:
    def __init__(self, top, left, right, down):
        self.top = top
        self.left = left
        self.right = right
        self.down = down
        self.match_top = False
        self.match_left = False
        self.match_right = False
        self.match_down = False

    def __str__(self):
        return self.top + ' ' + self.left + ' ' + self.right + ' ' + self.down


def load_tail():
    with open('tile.txt') as file:
        data = file.read()
    splitted = data.split('\n')
    top = splitted[0]
    down = splitted[-1]
    left = []
    right = []
    for i in splitted:
        left.append(i[0])
        right.append(i[-1])
    print(top)
    print(''.join(left))
    print(''.join(right))
    print(down)


def get_borders(element):
    top = element[0]
    down = element[-1]
    left = []
    right = []
    for i in element:
        left.append(i[0])
        right.append(i[-1])
    # print(top)
    # print(''.join(left))
    # print(''.join(right))
    # print(down)
    return top, ''.join(left), ''.join(right), down


def load_tail_all():
    with open('tile_all.txt') as file:
        data = file.read()
    print(data.split('\n'))
    splitted = []
    insider = []
    for i in data.split('\n'):
        if i != '':
            insider.append(i)
        else:
            splitted.append(insider)
            insider = []
    splitted.append(insider)
    print(splitted)
    tiles = []
    for i in splitted:
        tiles.append(Tile(*get_borders(i)))
    perform(tiles)


def perform(tiles):
    for i in range(len(tiles)):
        t = tiles[i].top
        l = tiles[i].left
        r = tiles[i].right
        d = tiles[i].down
        for j in range(len(tiles)):
            if i == j:
                continue

            if t == tiles[j].top or t[::-1] == tiles[j].top or t == tiles[j].down or t[::-1] == tiles[j].down:
                tiles[i].match_top = True
            elif l == tiles[j].left or l[::-1] == tiles[j].left or l == tiles[j].right or l[::-1] == tiles[j].right:
                tiles[i].match_left = True
            elif r == tiles[j].right or r[::-1] == tiles[j].right or r == tiles[j].left or r[::-1] == tiles[j].right:
                tiles[i].match_right = True
            elif i == 0 and j == 8:
                print(tiles[j].top, tiles[j].left, tiles[j].right, tiles[j].down)
            elif d == tiles[j].down or d[::-1] == tiles[j].down or d == tiles[j].down[::-1] or d == tiles[j].top or d[::-1] == tiles[j].top or d == tiles[j].top[::-1]:
                tiles[i].match_down = True
    for i in tiles:
        print(i.match_top, i.match_left, i.match_right, i.match_down)


def main():
    # load_tail()
    load_tail_all()


if __name__ == '__main__':
    main()
