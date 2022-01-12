def get_number_of_yes():
    with open('answers') as file:
        data = file.read()
    answers = []
    for answer in data.split('\n\n'):
        answers.append(answer.replace('\n', ''))
    counts = 0
    for answer in answers:
        temp = set()
        for x in answer:
            temp.add(x)
        counts = counts + len(temp)
    return counts


def main():
    11 == get_number_of_yes()


if __name__ == '__main__':
    main()
