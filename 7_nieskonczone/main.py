LIGHT_RED = 'light_red'
DARK_ORANGE = 'dark_orange'
BRIGHT_WHITE = 'bright_white'
MUTED_YELLOW = 'muted_yellow'
SHINY_GOLD = 'shiny_gold'
DARK_OLIVE = 'dark_olive'
VIBRANT_PLUM = 'vibrant_plum'
FADED_BLUE = 'faded_blue'
DOTTED_BLACK = 'dotted_black'


def build_rules():
    return {LIGHT_RED: [BRIGHT_WHITE, MUTED_YELLOW, MUTED_YELLOW],
            DARK_ORANGE:
                [BRIGHT_WHITE, BRIGHT_WHITE, BRIGHT_WHITE, MUTED_YELLOW, MUTED_YELLOW, MUTED_YELLOW,
                 MUTED_YELLOW],
            BRIGHT_WHITE: [SHINY_GOLD],
            MUTED_YELLOW:
                [SHINY_GOLD, SHINY_GOLD, FADED_BLUE, FADED_BLUE, FADED_BLUE, FADED_BLUE, FADED_BLUE,
                 FADED_BLUE, FADED_BLUE, FADED_BLUE,
                 FADED_BLUE],
            SHINY_GOLD: [DARK_OLIVE, VIBRANT_PLUM, VIBRANT_PLUM],
            DARK_OLIVE:
                [FADED_BLUE, FADED_BLUE, FADED_BLUE, DOTTED_BLACK, DOTTED_BLACK, DOTTED_BLACK, DOTTED_BLACK],
            VIBRANT_PLUM:
                [FADED_BLUE, FADED_BLUE, FADED_BLUE, FADED_BLUE, FADED_BLUE, DOTTED_BLACK, DOTTED_BLACK,
                 DOTTED_BLACK, DOTTED_BLACK, DOTTED_BLACK, DOTTED_BLACK],
            FADED_BLUE: None,
            DOTTED_BLACK: None}


def f(wanted):
    visited = []
    queue = []
    for i in build_rules()[LIGHT_RED]:
        queue.append(i)

    counts = 0
    while queue:
        s = queue.pop(0)
        if build_rules()[s]:
            for x in build_rules()[s]:
                if s not in visited:
                    queue.append(x)
                    visited.append(x)
        if s == wanted:
            counts = counts + 1
    return counts


def check_if_bag_contain(wanted, bags):
    for k, v in bags.items():
        for bag in v:
            d = {}
            if build_rules().get(bag) is not None:
                for x in build_rules().get(bag):
                    if bag in d:
                        d[bag].append(x)
                    else:
                        d[bag] = [x]
            if wanted == bag:
                return 1
            return check_if_bag_contain(wanted, d)
        return 0
    return 0


def main():
    print(f(SHINY_GOLD))
    # print(check_if_bag_contain(SHINY_GOLD, build_rules()))


if __name__ == '__main__':
    main()
