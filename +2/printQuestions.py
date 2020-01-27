from question_paper_reader import *
from data_file_utils import *


def print_all_questions_of(mark):
    mark_map = {'1': 0, '2': 1, '3': 2, '5': 3, '10': 4}
    files = find_files()
    for file in files:
        f = open("./data/"+file,"r")
        for line in f:
            line = line.strip()
            if line.endswith(str(mark)):
                    if line.startswith("["):
                        print(get_questions(line,file))
                    else:
                        print(file + " " +  line[0:line.rindex("-")])
        f.close()


print_all_questions_of(1)






