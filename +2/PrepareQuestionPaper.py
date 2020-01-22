from random import randint


def get_random():
    return randint(0,1000)


def get_questions(line,chapter):
    line = line[1:line.index(']')]
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
    return  eq < constraint


def prepare(all_questions_of_given_mark,total_questions,constraints):
    questions = []
    q = 0
    while q < total_questions:
        r = get_random() % len(list)
        question = all_questions_of_given_mark[r]
        if can_add_question(question,questions,constraints):
            questions.append(question)
            q = q + 1
    print(questions)

from os import listdir
from os.path import isfile, join
files = [f for f in listdir(".") if isfile(join(".", f)) and not f.endswith(".py")]
master_question_bank = [[],[],[],[],[]]
mark_separation = {'1':0,'2':1,'3':2,'5':3,'10':4}
constraints_5mark ={
        'DiscreteMathematics' : 1,
        'DifferentialEquations': 1,
        'IntegralCalculus': 1
    }
constraints = [{},{},{},constraints_5mark,{}]


for file in files:
    f = open(file,"r")
    for line in f:
        line = line.strip()
        for key in mark_separation:
            if line.endswith(key):
                list = master_question_bank[mark_separation[key]]
                if line.startswith("["):
                    list.extend(get_questions(line,file))
                else:
                    list.append(file + " " +  line[0:line.rindex("-")])
    f.close()
prepare(master_question_bank[3],3,constraints[3])






