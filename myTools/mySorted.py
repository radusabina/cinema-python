def mySorted(it, *, key=lambda x: x, reverse=False):
    for i in range(len(it) - 1):
        for j in range(i + 1, len(it)):
            if key(it[i]) > key(it[j]) and not reverse:
                it[i], it[j] = it[j], it[i]
            if key(it[i]) < key(it[j]) and reverse:
                it[i], it[j] = it[j], it[i]
    return it
