def task_06(name: str) -> str:
    name = name.strip()
    words = name.split()
    normalized_words = [word.capitalize() for word in words]
    return " ".join(normalized_words)
