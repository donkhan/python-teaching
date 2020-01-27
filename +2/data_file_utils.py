from os import listdir

def find_files():
    return [f for f in listdir("./data/") if not f.endswith(".data")]
