from random import randint
from os import listdir

from question_paper_reader import *
from total_reader import *
from constraint_reader import *

def get_random():
    return randint(0,1000)

def can_add_question(question,questions,constraints):
    chapter = question.split()[0]
    eq = 0
    for q in questions:
        if q.split()[0] == chapter:
            eq = eq + 1
    constraint = constraints[chapter]
    return eq < constraint


def prepare(mark,all_questions_of_given_mark,total,constraints):
    selected_questions = []
    #print(mark, len(all_questions_of_given_mark))
    failed = []
    p = 0
    while len(selected_questions) < total:
        r = get_random() % len(all_questions_of_given_mark)
        question = all_questions_of_given_mark[r]
        if can_add_question(question,selected_questions,constraints):
            selected_questions.append(question)
            all_questions_of_given_mark.remove(question)
        else:
            failed.append(question)
        p = p + 1
        if p == 1000:
            print("Problem in mark " , mark)
            print("All Questions ",all_questions_of_given_mark)
            print("Selected questions ",selected_questions)
            print("Chosen and Rejected questions",failed)
            break
    print(mark,len(selected_questions),selected_questions)


def create_random_question_paper():
    mark_map = {'1': 0, '2': 1, '3': 2, '5': 3, '10': 4}
    files = find_files()
    totals = read_total_questions()
    constraints = prepare_constraints(mark_map)
    master_question_bank = [[], [], [], [], []]
    for file in files:
        f = open("./data/"+file,"r")
        for line in f:
            line = line.strip()
            for key in mark_map:
                if line.endswith(key):
                    questions = master_question_bank[mark_map[key]]
                    if line.startswith("["):
                        questions.extend(get_questions(line,file))
                    else:
                        questions.append(file + " " +  line[0:line.rindex("-")])
        f.close()
    prepare_and_print(mark_map, master_question_bank, totals, constraints)


def prepare_and_print(mark_separation,master_question_bank,totals,constraints):
    for mark in mark_separation.keys():
        n = mark_separation.get(mark)
        constraint = constraints[n]
        prepare(mark, master_question_bank[n], totals[n], constraint)


def find_files():
    return [f for f in listdir("./data/") if not f.endswith(".data")]


create_random_question_paper()






