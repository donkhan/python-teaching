def read_total_questions():
    totals = []
    f = open("data/total_questions.data", "r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        totals.append(int(line))
    return totals
