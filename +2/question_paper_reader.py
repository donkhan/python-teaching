

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


