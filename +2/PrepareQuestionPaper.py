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


def prepare(mark,all_questions_of_given_mark,total_questions,constraints):
    #print(all_questions_of_given_mark,total_questions,constraints)
    questions = []
    q = 0
    while q < total_questions:
        r = get_random() % len(all_questions_of_given_mark)
        question = all_questions_of_given_mark[r]
        if can_add_question(question,questions,constraints):
            questions.append(question)
            q = q + 1
    print(mark , " Mark Questions - ",questions)

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

constraints_1mark ={
        'DiscreteMathematics' : 1,
        'DifferentialEquations': 1,
        'IntegralCalculus': 1
    }

constraints = [constraints_1mark,{},{},constraints_5mark,{}]
totals = [1,0,0,3,0]


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

for mark in mark_separation.keys():
    n = mark_separation.get(mark)
    if mark == '5' or mark == '1':
        prepare(mark,master_question_bank[n],totals[n],constraints[n])






