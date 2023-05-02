def naive_pattern_matching(text, pattern):
    S = len(text)
    R = len(pattern)
    MAX = S - R + 1
    l = 0
    # Loop through each position in the text where the pattern could start
    while l <= MAX:
        # Check if the pattern matches starting from this position
        match = True
        for j in range(R):
            if text[l+j] != pattern[j]:
                match = False
                break
        # If the pattern matches, record the position of the match
        if match:
            return l
        l += 1
    return "no match"

print(naive_pattern_matching('james', 'me'))

