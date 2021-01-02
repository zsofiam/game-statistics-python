import export
import printing


def count_games(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    return len(lines)


def decide(file_name, year):
    pass


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
    print(count_games("game_stat.txt"))