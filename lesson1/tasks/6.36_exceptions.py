def task_36(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return None