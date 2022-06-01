'''
***PART 5***

Write a program that repeatedly prompts the user to enter numbers until the user enters 0. The program will then count how many of the nonzero inputs are even, and print the number of even inputs in a sentence.

(Hint: For this part, it's likely that you will have an if block inside a while loop. Pay careful attention to the levels of indentation when that happens.)

Example of what should appear on the console when this part runs:

Enter a number or enter 0 to stop: 1
Enter a number or enter 0 to stop: 2
Enter a number or enter 0 to stop: 5
Enter a number or enter 0 to stop: 6
Enter a number or enter 0 to stop: 9
Enter a number or enter 0 to stop: 10
Enter a number or enter 0 to stop: 7
Enter a number or enter 0 to stop: 0
Number of evens: 3

'''

num_int = None
even_count = 0

while num_int != 0:
    num_str = input("Enter a number or enter 0 to stop: ")
    num_int = int(num_str)
    if num_int < 0:
        continue
    if num_int % 2 == 0:
        even_count += 1

print("Even count:", even_count)

# i think it counts 0 as an even number