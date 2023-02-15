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

# Solution2: || I tried to opotimize it by myself, 
                # First i found the element with least number of chars in the list, divided it into prefixes.

class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        result = ''
        prefix = {}
        shortest_word = min(strs, key=len)
        for index in range(len(shortest_word)):
            prefix[index] = shortest_word[:index+1]
            for x in strs:
                if prefix[index] != x[:index+1]:
                    return result
            result = prefix[index]
        return result

# Runtime: 31ms, |beats 89.51% :)
# M:13.9: |Beats 41.2% :)

# I'll try to optmize it more 

# Soluton3 || Binary Search | R: beats 51%: | M: 41%
# 
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        return self._longest_common_prefix(strs, 0, len(strs) - 1)

    def _longest_common_prefix(self, strs, l, r):
        if l == r:
            return strs[l]
        else:
            mid = (l + r) // 2
            lcp_left = self._longest_common_prefix(strs, l, mid)
            lcp_right = self._longest_common_prefix(strs, mid + 1, r)
            return self._common_prefix(lcp_left, lcp_right)

    def _common_prefix(self, left, right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]  
