from random import shuffle
from string import ascii_uppercase


def get_teams(players, number):
    rez = ''
    digits = '123456789'
    names = [i for i in ascii_uppercase + digits]
    for x in ascii_uppercase:
        for y in digits:
            names.append(f'{x}{y}')

    lst = []
    doubles = set([i for i in players if players.count(i) != 1])
    print('-' * 10)
    if len(doubles) == 0:
        print("Дубликатов нет")
    else:
        print(f"Дубликаты: {doubles}")
    players = set(players)

    for person in players:
        if len(person) != 0:
            lst.append(person.split()[0])

    if len(lst) % number != 0:
        if number == 1:
            rez += f'Кол-во участников должно быть кратно {number}му'
        elif number in [2, 3, 4]:
            rez += f'Кол-во участников должно быть кратно {number}м'
        else:
            rez += f'Кол-во участников должно быть кратно {number}ти'
        return rez

    print(f"Всего участников: {len(players)}")
    print(f"Всего команд: {len(players) // number}")

    shuffle(lst)

    for i in range(0, len(lst), number):
        rez += f'TEAM {names[i // number]}\n'
        rez += ' '.join(lst[i:i + number]) + '\n' * 2
    return rez


def get_net(teams):
    rez = ''
    shuffle(teams)

    for i in range(0, len(teams), 2):
        rez += f'{teams[i]} 🆚 {teams[i + 1]}' + '\n' * 2

    return rez


def delete_numeration(players):
    rez = ''
    for player in players:
        player = player.split()[-1]
        rez += player + '\n'
    return rez


def add_numeration(players):
    ind = 0
    rez = ''
    for player in players:
        ind += 1
        rez += f'{ind}. {player}' + '\n'
    return rez
