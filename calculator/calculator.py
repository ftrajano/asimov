# calculator.py
# A program that simulates a calculator.

# Importing the necessary modules.
import os
# os.system('cls' if os.name == 'nt' else 'clear')




#################### FUNCTIONS ####################

# function that prints the menu
def menu():
	print('#######################')
	print('### CALCULATOR 1.0 ####')
	print('#######################')
	print('')
	print("Choose an operation:")
	print("0 - for addition.")
	print("1 - for subtraction.")
	print("2 - for multiplication.")
	print("3 - for division.")
	print('')

def first_number():
	num1 = float(input("type the first number:"))
	return num1

def second_number():
	num2 = float(input("type the second number:"))
	return num2

def continue_program():
	option = input("Do you want to continue? (y/n)")
	if option == 'y':
		start = True
		os.system('cls' if os.name == 'nt' else 'clear')
	else:
		start = False
		print("Goodbye!")

def get_operation():
	print('')
	op = int(input("Digite a operação desejada: "))
	print('')
	return op
 
def operate():
	if op == 0:
		result = num1 + num2
		print("The result is: ", result)
	elif op == 1:
		result = num1 - num2
		print("The result is: ", result)
	elif op == 2:
		result = num1 * num2
		print("The result is: ", result)
	elif op == 3:
		result = num1 / num2
		print("The result is: ", result)
	else:
		print("Invalid operation!")

#################### MAIN ####################
start  = True

while(start):
	menu()
	op = get_operation()
	num1 = first_number()
	num2 = second_number()
	operate()
	continue_program()




