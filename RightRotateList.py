def rightRotate(lst, n):
    # Write your code here
    print(len(lst))
    print(n)
    print(n % len(lst))


    if n > len(lst):
        n = n % len(lst)
    lst = lst[-n:] + lst[:-n]
    return lst


print(rightRotate([1,2,3,4,5], 6))
print(rightRotate(['13', 'a', 'Python'], 5))


def rightRotate2(lst, n):
  n = n%len(lst)
  rotatedList = []
  for item in range(len(lst) - n, len(lst)):
    rotatedList.append(lst[item])
  for item in range(0, len(lst) - n):
    rotatedList.append(lst[item])
  return rotatedList 

print(rightRotate2([1,2,3,4,5], 3))