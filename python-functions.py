# Challenges

# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.

def sum_to(n):
  sum = 0
  i = 0
  while i <= n:
    sum = sum + i
    i+=1
  return sum 
  
print(sum_to(10))
  




# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(n):
  n.sort()
  return n[-1]

print(largest([1, 2, 3, 4, 0]))



# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.


def occurences(str, arg):
  return str.count(arg)

print(occurences('zigg zouhrab', 'z'))


# 4 . Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  product = 1
  for i in args:
    product*=i
  return product

print(product(12, 12))