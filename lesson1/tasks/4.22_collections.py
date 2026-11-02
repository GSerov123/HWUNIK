def task_22(text):
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq