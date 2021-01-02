import export
import printing


TITLE = 0
RELEASE_YEAR = 2
GENRE = 3


def convert_file_lines_to_list(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    return lines


def count_games(file_name):
    lines = convert_file_lines_to_list(file_name)
    return len(lines)


def decide(file_name, year):
    contains = False
    lines = convert_file_lines_to_list(file_name)
    for line in lines:
        properties = line.split("\t")
        if int(properties[RELEASE_YEAR]) == year:
            contains = True
            break
    return contains


def get_latest(file_name):
    latest_year = 0
    latest_game = ''
    lines = convert_file_lines_to_list(file_name)
    for line in lines:
        properties = line.split("\t")
        if int(properties[RELEASE_YEAR]) > latest_year:
            latest_year = int(properties[RELEASE_YEAR])
            latest_game = properties[TITLE]
    return latest_game


def count_by_genre(file_name, genre):
    count = 0
    lines = convert_file_lines_to_list(file_name)
    for line in lines:
        properties = line.split("\t")
        if properties[GENRE] == genre:
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    found = False
    lines = convert_file_lines_to_list(file_name)
    for index, line in enumerate(lines):
        properties = line.split("\t")
        if properties[TITLE] == title:
            found = True
            return index + 1
    if not found:
        print("You entered incorrect title!!")
        raise ValueError


def quicksort(list):
    if not list:
        return []
    return (quicksort([x for x in list[1:] if x < list[0]])
            + [list[0]] +
            quicksort([x for x in list[1:] if x > list[0]]))


def sort_abc(file_name):
    list_of_titles = []
    lines = convert_file_lines_to_list(file_name)
    for line in lines:
        properties = line.split("\t")
        list_of_titles.append(properties[TITLE])
    sorted_list_of_titles = quicksort(list_of_titles)
    return sorted_list_of_titles


def get_genres(file_name):
    list_of_genres = []
    lines = convert_file_lines_to_list(file_name)
    for line in lines:
        properties = line.split("\t")
        list_of_genres.append(properties[GENRE])
    sorted_list_of_genres = quicksort(list_of_genres)
    return sorted_list_of_genres


def when_was_top_sold_fps(file_name):
    pass


if __name__ == '__main__':
    print(get_genres("game_stat.txt"))
    print(sort_abc("game_stat.txt"))