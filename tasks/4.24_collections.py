def task_24(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))