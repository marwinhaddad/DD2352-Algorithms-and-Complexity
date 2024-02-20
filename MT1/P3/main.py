
n = 3
P = [[0.50, 0.50, 0.0],
     [0.25, 0.25, 0.5]]
O = [['s', 'n', 'z'],
     ['o', 'o', 'w']]

S = "nnw"

def check(n, P, O, word):
    state = n-1
    word_list = list(word)
    while word_list:
        char = word_list.pop()
        found = 0
        for i, row in enumerate(O):
            if row[state] == char and P[i][state] != 0:
                state = i
                found = 1
                break
        if found == 0:
            return False
    return True

print(check(n, P, O, S))
