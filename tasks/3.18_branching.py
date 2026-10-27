def task_18(op, a, b_):
    if op == "+":
        return a + b_
    elif op == "-":
        return a - b_
    elif op == "*":
        return a * b_
    elif op == "/":
        if b_ == 0:
            return None
        return a / b_
    else:
        return None