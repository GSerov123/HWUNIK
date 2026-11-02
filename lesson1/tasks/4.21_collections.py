def task_21(a, b):
    return {
        "union": sorted(a | b),
        "intersection": sorted(a & b),
        "a_minus_b": sorted(a - b),
    }