# 1 Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  if (n == 0):
    return 0
  elif (n == 1):
    return 1
  else:
    for i in range(1, n):
      n += i 
    return n

# 2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(*args):
  largest_num = 0 
  for number in args:
    if (largest_num < number):
      largest_num = number
  return largest_num
  
# 3 Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(str1, str2):
  return str1.count(str2)

# 4 Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  sum = 1
  for num in args: 
    sum *= num
  return sum

print(product(4, 0.5, 5))



