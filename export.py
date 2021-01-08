import sys
import reports


def write_answer_to_file(answer, file):
    file.write(str(answer) + "\n")


def main():
    try:
        with open(sys.argv[2], "w") as file:
            answer = reports.count_games(sys.argv[1])
            write_answer_to_file(answer, file)
            answer = reports.decide(sys.argv[1], sys.argv[3])
            write_answer_to_file(answer, file)
            answer = reports.get_latest(sys.argv[1])
            write_answer_to_file(answer, file)
            answer = reports.count_by_genre(sys.argv[1], sys.argv[4])
            write_answer_to_file(answer, file)
            answer = reports.get_line_number_by_title(sys.argv[1], sys.argv[5])
            write_answer_to_file(answer, file)
            answer = reports.sort_abc(sys.argv[1])
            write_answer_to_file(answer, file)
            answer = reports.get_genres(sys.argv[1])
            write_answer_to_file(answer, file)
            answer = reports.when_was_top_sold_fps(sys.argv[1])
            write_answer_to_file(answer, file)
    except IOError as e:
        print("[ERROR]: CANNOT WRITE INTO FILE " + str(e) + " !!!")


if __name__ == '__main__':
    main()
