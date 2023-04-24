import sys
from collections import *

class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = deque()
    def pushCharacter(self, c):
        self.stack.append(c)
    def enqueueCharacter(self, c):
         self.queue.append(c)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.popleft()

s = input()
obj = Solution()
l = len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
isPalindrome = True
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
