def findSecondMaximum(lst):
  # Write your code here
  lst.sort()
  return lst[len(lst)-2]

  # if len(lst) >= 2:
  #   return lst[-2]
  # else:
  #   return None

print(findSecondMaximum([1,2,3,4,7,7,12]))

def findSecondMaximum2(lst):
  if (len(lst) < 2):
    return
  first = second = float('-inf')
  for i in range(len(lst)):
    if (lst[i] > first):
      second = first
      first = lst[i]
    elif (lst[i] > second and lst[i] != first):
      second = lst[i]
  if (second == float('-inf')):
      return
  else:
      return second

print(findSecondMaximum2([9,2,3,6]))