def task_27(n):
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((i + 1) * (j + 1))
        table.append(row)
    return table