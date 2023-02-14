# Explanation:    
    # Write a function to find the longest common prefix string amongst an array of strings.
    # If there is no common prefix, return an empty string "".



# Solution1: || the 1st brute force solution came to my mind || spen around 40 mins
strs = ['jacob', 'jackson', 'jacin', 'jash']

def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    prefix = {}
    fel = strs[0]
    for i in range(len(fel)):
        prefix[i] = fel[:i+1]
    try:
        i = 0
        for index in range(len(fel)):
            for x in strs:
                if prefix[i] != x[:index+1]:
                    return result
            result = prefix[i]
            i += 1
        return result
    except IndexError:
        return result

# Runtime: 39ms, |beats 51.72% :(
# M:14: |Beats 41.33 :(

# Solution2:
