from typing import List, Any


def findFirstUnique(lst):
  # Write your code here
  j = 0
  for i in range(len(lst)):
    while j < len(lst):
      if (lst[i] == lst[j] and i != j):
         break
      j += 1
    if j == len(lst):
       return lst[i]
  return None



print(findFirstUnique([1,2,3,2,7]))


def findFirstUnique2(lst):
    counts = {}  # Creating a dictionary
    counts = counts.fromkeys(lst, 0)  # Initializing dictionary with pairs like (lst[i],0)
    for ele in lst:
        counts[ele] += 1  # Incrementing for every repitition
    for ele in lst:
        if counts[ele] <= 1:
            return ele
    return None


print(findFirstUnique2([1, 1, 1, 2]))