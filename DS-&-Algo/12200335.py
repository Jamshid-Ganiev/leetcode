TABLE_FOR_EVEN = {
        "q0": {"a": "q1", "b": "q0", "other": "q0"},
        "q1": {"a": "q2", "b": "q0", "other": "q0"},
        "q2": {"a": "q2", "b": "q3", "other": "q0"},
        "q3": {"a": "q1", "b": "q4", "other": "q0"},
        "q4": {"a": "q5", "b": "q0", "other": "q0"},
        "q5": {"a": "P", "b": "q0", "other": "q0"}
}

TABLE_FOR_ODD = {
        'q0': {'a': 'q1', 'b': 'q0', 'other': 'q0'},
        'q1': {'a': 'q2', 'b': 'q0', 'other': 'q0'},
        'q2': {'a': 'q2', 'b': 'q3', 'other': 'q0'},
        'q3': {'a': 'q4', 'b': 'q0', 'other': 'q0'},
        'q4': {'a': 'q2', 'b': 'q5', 'other': 'q0'},
        'q5': {'a': 'P', 'b': 'q0', 'other': 'q0'}
}

student_id = int(input("Enter your Student ID:"))

if (student_id % 100) % 2 == 0:
    Pattern = 'aabbaa'
    Table = TABLE_FOR_EVEN
else:
    Pattern = 'aababa'
    Table = TABLE_FOR_ODD


def pattern_matching(T, P, Q):
    # F = Table for pattern
    # T = Text
    # P = Pattern
    
    n = len(T)
    m = len(P)
    S = 'q0'  # initialize S1
    K = 1
    
    while S != 'P' and K <= n:
        Tk = T[K-1]
        Sk = Q[S].get(Tk, 'q0')  # compute Sk+1 using state transition table
        K += 1
        if Sk == 'P':
            INDEX = K - m - 1
            return f"==>Pattern: '{Pattern}'. Index:[{INDEX}:{INDEX + m}]"
        S = Sk
    
    return '==>No Match Found'  # no match found

TEXT_1 = 'abaabcaacbcaccaababaacabba'
TEXT_2 = 'abaabcaacbcaccaabbaacabba'

print(pattern_matching(T=TEXT_1, P=Pattern, Q=Table))
print(pattern_matching(T=TEXT_2, P=Pattern, Q=Table))