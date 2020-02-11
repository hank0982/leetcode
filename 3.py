# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"   
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # string manipulation
        # find the longest non-repeated chars
        # raw idea -> using sliding window algorithm
        # set two pointers i, j as the window margins
        # l as a length of string
        i, j = 0, 0
        l = len(s)
        # using set to record whether there is a repeated char while traversing
        char_set = set()
        length = 0
        # start traversing
        while i < l and j < l:
            # if the set contains the char on most-right pointer
            if(s[j] in char_set):
                # delete the char on the most-left pointer in the set
                # move the most-left pointer to the right one poistion
                char_set.remove(s[i])
                i = i + 1
            # if the set dose not contain the char on most-right pointer
            else:
                # add the new char pointed by the most-right pointer to set
                char_set.add(s[j])
                # move the most-right pointer to the right one position
                j = j + 1
                # update the length
                length = max(j-i, length)
        return length
