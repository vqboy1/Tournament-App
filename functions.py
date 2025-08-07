from random import shuffle
from string import ascii_uppercase
from itertools import combinations
digits = '123456789'
names = [i for i in ascii_uppercase + digits]
for x in ascii_uppercase:
    for y in digits:
        names.append(f'{x}{y}')


def groups_into_matches(a):
    try:
        a = [i for i in a.split('\n') if len(i) != 0 and i != '⸻']
        all_teams = [i.split(':', 1)[0] for i in a if 'Группа' not in i and 'GROUP' not in i]
        group_names = [i for i in a if 'Группа' in i or 'GROUP' in i]
        group_count = len(a) - len(all_teams)
        teams_in_group = len(all_teams) // group_count
        lst = []
        inner_lst = []
        rez = ''
        for i in range(0, len(all_teams), teams_in_group):
            rez += group_names[i // teams_in_group] + '\n' * 2
            for j in range(teams_in_group):
                inner_lst.append(all_teams[i + j])
            pairs = combinations(inner_lst, 2)
            for pair in pairs:
                rez += f'{pair[0]} VS {pair[1]}' + '\n' * 2
            rez += '⸻' + '\n'
            lst.append(inner_lst)
            inner_lst = []
        return rez
    except ZeroDivisionError:
        return 'Произошла ошибка. Вы точно ввели группы?'


def get_teams(players, number) -> str:
    rez = ''

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


def get_net(teams) -> str:
    rez = ''
    shuffle(teams)
    if len(teams) == 0:
        return 'Введите команды слева'
    if len(teams) % 2 != 0:
        return 'Должно быть четное количество команд!'
    for i in range(0, len(teams), 2):
        rez += f'{teams[i]} 🆚 {teams[i + 1]}' + '\n' * 2

    return rez


def get_groups(teams, number) -> str:
    rez = ''
    shuffle(teams)
    ost = len(teams) % number
    if len(teams) < number:
        return 'Недостаточное количество команд.'
    if ost != 0:
        return f'Недостаточное количество команд. Уберите {ost} команд или добавьте {number - ost}.'
    for i in range(0, len(teams), number):
        rez += '⸻' + '\n' * 2
        rez += f'GROUP {names[i]}' + '\n'
        rez += '\n'.join(teams[i:i+number]) + '\n' * 2

    return rez


def delete_numeration(players) -> str:
    rez = ''
    for player in players:
        player = player.split()[-1]
        rez += player + '\n'
    return rez


def add_numeration(players) -> str:
    ind = 0
    rez = ''
    for player in players:
        ind += 1
        rez += f'{ind}. {player}' + '\n'
    return rez


def get_style_properties(theme: str) -> str:
    with open(f"styles/{theme}.txt", "r") as style_file:
        return style_file.read()


def save_style(text):
    with open(f"styles/current-style.txt", "w") as file:
        return file.write(text)


def get_style() -> str:
    with open(f"styles/current-style.txt", "r") as file:
        return file.read()
