# Challenge 9: Rearrange Positive & Negative Values
# Given a list, can you re-arrange its elements in such a way that the negative elements appear at one side
# and positive elements appear in the other?
# Solve this problem in Python and see if your code runs correctly!

def reArrange(lst):
  # Write your code here
  neg = []
  pos = []
  i = 0
  j = 0
  for elem in lst:
    if elem < 0:
      neg.append(elem)
    else: pos.append(elem)

  return neg + pos

print(reArrange([1,-3,4,-1,10,-12]))