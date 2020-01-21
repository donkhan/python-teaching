
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


from os import listdir
from os.path import isfile, join
files = [f for f in listdir(".") if isfile(join(".", f)) and not f.endswith(".py")]
Q5 = []

for file in files:
    f = open(file,"r")
    for line in f:
        line = line.strip()

        if line.endswith("5"):
            if line.startswith("["):
                Q5.extend(get_questions(line,file))
            else:
                Q5.append(file + " " +  line)

    f.close()

print(Q5)




