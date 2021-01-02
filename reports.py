import export
import printing


RELEASE_YEAR = 2


def count_games(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    return len(lines)


def decide(file_name, year):
    contains = False
    file = open(file_name)
    lines = file.readlines()
    file.close()
    for line in lines:
        properties = line.split("\t")
        if int(properties[RELEASE_YEAR]) == year:
            contains = True
            break
    return contains


def get_latest(file_name):
    pass


def count_by_genre(file_name, genre):
    pass


def get_line_number_by_title(file_name, title):
    pass


def sort_abc(file_name):
    pass


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass


if __name__ == '__main__':
    print(decide("game_stat.txt", 1984))