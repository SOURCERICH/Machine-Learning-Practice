'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''

s = "abcabcbbd"

subs = []
count = 0
x = 0
for i in s:
    while i in subs:
        subs.pop(0)
        x -= 1
    else:
        subs.append(i)
        x += 1
        count = max(count,x)
print(count)