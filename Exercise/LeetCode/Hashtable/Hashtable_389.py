'''
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.
'''
# date 12.04.2020

def findeDifference(s, t):
    return set(t)-set(s)

s = input('s :')
t = input('t :')

print(findeDifference(s, t))
