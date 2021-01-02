import export
import printing


TITLE = 0
COPIES_SOLD = 1
RELEASE_YEAR = 2
GENRE = 3


def convert_file_lines_to_list(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    return lines


def get_property_list(lines, property):
    property_list = []
    for line in lines:
        properties = line.split("\t")
        property_list.append(properties[property])
    return property_list


def count_games(file_name):
    lines = convert_file_lines_to_list(file_name)
    return len(lines)


def decide(file_name, year):
    contains = False
    lines = convert_file_lines_to_list(file_name)
    release_years = get_property_list(lines, RELEASE_YEAR)
    for release_year in release_years:
        if int(release_year) == year:
            contains = True
            break
    return contains


def get_latest(file_name):
    latest_year = 0
    latest_game = ''
    lines = convert_file_lines_to_list(file_name)
    release_years = get_property_list(lines, RELEASE_YEAR)
    titles = get_property_list(lines, TITLE)
    for index, release_year in enumerate(release_years):
        if int(release_year) > latest_year:
            latest_year = int(release_year)
            latest_game = titles[index]
    return latest_game


def count_by_genre(file_name, genre):
    count = 0
    lines = convert_file_lines_to_list(file_name)
    genres = get_property_list(lines, GENRE)
    for genre_in_list in genres:
        if genre_in_list == genre:
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    found = False
    lines = convert_file_lines_to_list(file_name)
    titles = get_property_list(lines, TITLE)
    for index, title_in_list in enumerate(titles):
        if title_in_list == title:
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
    lines = convert_file_lines_to_list(file_name)
    titles = get_property_list(lines, TITLE)
    sorted_list_of_titles = quicksort(titles)
    return sorted_list_of_titles


def get_genres(file_name):
    lines = convert_file_lines_to_list(file_name)
    genres = get_property_list(lines, GENRE)
    sorted_list_of_genres = quicksort(genres)
    return sorted_list_of_genres


def when_was_top_sold_fps(file_name):
    lines = convert_file_lines_to_list(file_name)
    genres = get_property_list(lines, GENRE)
    copies_sold = get_property_list(lines, COPIES_SOLD)
    release_years = get_property_list(lines, RELEASE_YEAR)
    top_sold = -1
    release_year = -1
    for index, genre in enumerate(genres):
        if genre == "First-person shooter":
            if float(copies_sold[index]) > top_sold:
                top_sold = float(copies_sold[index])
                release_year = int(release_years[index])
    if release_year == -1:
        print("You entered incorrect genre!!")
        raise ValueError
    else:
        return release_year
    

if __name__ == '__main__':
    print(get_genres("game_stat.txt"))
    print(sort_abc("game_stat.txt"))
    print(when_was_top_sold_fps("game_stat.txt"))