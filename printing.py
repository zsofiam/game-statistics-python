import sys
import reports

FILE_NAME = "game_stat.txt"


def process_questions(question):
    pass


def main():
    while True:
        question = input("Please ask a question!")
        if question == "How many games are in the file?":
            answer = reports.count_games(FILE_NAME)
            print(answer)
        elif question == "Is there a game from a given year?":
            year = input("Which year?")
            answer = reports.decide(FILE_NAME, year)
            print(answer)
        elif question == "Which is the latest game?":
            answer = reports.get_latest(FILE_NAME)
            print(answer)
        elif question == "How many games are in the file by genre?":
            genre = input("Provide a genre:")
            answer = reports.count_by_genre(FILE_NAME, genre)
            print(answer)
        elif question == "What is the line number of a given title?":
            title = input("Provide a title:")
            answer = reports.get_line_number_by_title(FILE_NAME, title)
            print(answer)
        elif question == "Can you give me the alphabetically ordered list of the titles?":
            print("Yes, sure.")
            answer = reports.sort_abc(FILE_NAME)
            print(answer)
        elif question == "Which genres occur in the data file?":
            answer = reports.get_genres(FILE_NAME)
            print(answer)
        elif question == "What is the release year of the top sold first-person shooter game?":
            answer = reports.when_was_top_sold_fps(FILE_NAME)
            print(answer)   


if __name__ == '__main__':
    main()

