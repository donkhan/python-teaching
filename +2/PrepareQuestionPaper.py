from random import randint
from os import listdir


def get_random():
    return randint(0,1000)


def get_example_questions(line,chapter):
    q = []
    tokens = line.split("-")
    s = int(tokens[0][2:])
    e = int(tokens[1][2:])
    for i in range(s,e+1):
        question = chapter + " Example " + str(i)
        q.append(question)
    return q


def get_questions(line,chapter):
    line = line[1:line.index(']')]
    if line.startswith("Ex"):
        return get_example_questions(line,chapter)
    q = []
    s = line[:line.index('-')]
    e = line[line.index('-')+1:]
    ex = s[:s.rindex('.')]
    start = int(s.split(".")[2])
    end = int(e.split(".")[2])
    for i in range(start,end+1):
        question = chapter + " " + ex + "." + str(i)
        q.append(question)
    return q


def can_add_question(question,questions,constraints):
    chapter = question.split()[0]
    eq = 0
    for q in questions:
        if q.split()[0] == chapter:
            eq = eq + 1
    constraint = constraints[chapter]
    return eq < constraint


def prepare(mark,all_questions_of_given_mark,total,constraints):
    #print(total,all_questions_of_given_mark)
    selected_questions = []
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
            print("Choosen and Rejected questions",failed)
            break
    print(mark,selected_questions)


def prepare_constraints():
    constraints = [{},{},{},{},{}]
    f = open("data/constraints.data","r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        print(line)
        tokens = line.split("=")
        no = int(tokens[1])
        tokens = tokens[0].split("-")
        chapter = tokens[0]
        mark = tokens[1]
        constraint = constraints[mark_separation[mark]]
        constraint[chapter] = no
    return constraints


def create_random_question_paper():
    find_files()
    read_total_questions()
    constraints = prepare_constraints()
    for file in files:
        f = open("./data/"+file,"r")
        for line in f:
            line = line.strip()
            for key in mark_separation:
                if line.endswith(key):
                    questions = master_question_bank[mark_separation[key]]
                    if line.startswith("["):
                        questions.extend(get_questions(line,file))
                    else:
                        questions.append(file + " " +  line[0:line.rindex("-")])
        f.close()

    for mark in mark_separation.keys():
        n = mark_separation.get(mark)
        constraint = constraints[n]
        prepare(mark, master_question_bank[n], totals[n], constraint)


def find_files():
    global files
    files = [f for f in listdir("./data/") if not f.endswith(".data")]


def read_total_questions():
    f = open("data/total_questions.data", "r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        totals.append(int(line))

files = []
master_question_bank = [[],[],[],[],[]]
mark_separation = {'1':0,'2':1,'3':2,'5':3,'10':4}
totals = []


create_random_question_paper()






