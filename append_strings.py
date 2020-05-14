s1=input('Enter string 1:')
s2=input('Enter string 2:')
def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
  print("After appending new string in middle", middleThree)
  
appendMiddle(s1,s2)
