# Explanation:    
    # Write a function to find the longest common prefix string amongst an array of strings.
    # If there is no common prefix, return an empty string "".



# Solution1: || the 1st brute force solution came to my mind || spen around 40 mins
strs = ['jacob', 'jackson', 'jacin', 'jash']

def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    prefix = {}
    fel = min(strs, key=len)
    try:
        for index in range(len(fel)):
            prefix[index] = fel[:index+1]
            for x in strs:
                if prefix[index] != x[:index+1]:
                    return result
            result = prefix[index]
        return result
    except IndexError:
        return result

# Runtime: 39ms, |beats 51.72% :(
# M:14: |Beats 41.33 :(

# Solution2: || I tried to opotimize it by myself, 
                # First i found the element with least number of chars in the list, divided it into prefixes.

def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    prefix = {}
    fel = min(strs, key=len)
    try:
        for index in range(len(fel)):
            prefix[index] = fel[:index+1]
            for x in strs:
                if prefix[index] != x[:index+1]:
                    return result
            result = prefix[index]
        return result
    except IndexError:
        return result

# Runtime: 35ms, |beats 73.06% :)
# M:13.8: |Beats 81.80 :)

# try to optmize it more   
