def task_33(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.readline().rstrip("\n")
    except FileNotFoundError:
        return ""