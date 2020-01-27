def prepare_constraints(mark_map):
    constraints = [{},{},{},{},{}]
    f = open("data/constraints.data","r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        tokens = line.split("=")
        no = int(tokens[1])
        tokens = tokens[0].split("-")
        chapter = tokens[0]
        mark = tokens[1]
        constraint = constraints[mark_map[mark]]
        constraint[chapter] = no
    return constraints


