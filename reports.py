
# Report functions


def count_games(file_name):
    file = open(file_name)
    num_lines = sum(1 for game in file)
    file.close()
    return(int(num_lines))


def decide(file_name, year):
    with open(file_name) as file:
        games = file.read().splitlines()
        for game in games:
            game_attributes = game.split('\t')
            if str(year) == game_attributes[2]:
                return True
    return False


def get_latest(file_name):
    file = open(file_name)
    games = [game.split('\t') for game in file.readlines()]
    year = 0
    for game in games:
        if int(game[2]) > int(year):
            year = game[2]
            name = game[0]
    file.close()
    return name


def count_by_genre(file_name, genre):
    file = open(file_name)
    piece = 0
    for game in file:
        if genre in game:
            piece += 1
    file.close()
    return piece


def get_line_number_by_title(file_name, title):
    with open(file_name) as file:
        for num, game in enumerate(file, 1):
            if (title + '\t') in game:
                return num
    raise ValueError('Could not find {} in {}'.format(title, file_name))
