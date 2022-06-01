'''
***PART 4***

Write a program that repeatedly prompts the user to enter numbers until the user enters 0. The program calculate the product of all of the entered numbers and prints the product.

Example of what should appear when this part runs:

Enter a number or enter 0 to stop: 2
Enter a number or enter 0 to stop: 3
Enter a number or enter 0 to stop: 10
Enter a number or enter 0 to stop: 0
Product: 60

'''

num_str = input("Enter a number or enter 0 to stop: ")
num_int=int(num_str)
total = 0


while num_int != 0:
  total = total*num_int
  num = int(input("Enter a number or enter 0 to stop: "))
    
print("Product: ", total)
