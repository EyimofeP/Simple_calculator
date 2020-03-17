'''Code by Eyimofe Ayo Pinnick
Aka The Geekish Nerd
Alias Pinnick_Jnr'''

#While Loop to create options
while True:
	print("A Simple Calculator")
	print("Developed by Pinnick_Jnr")
	print("""User Input options are as follows
			 Type "add" for addition of two numbers
			 Type "sub" for subtraction of two numbers
			 Type "divide" for the division of two numbers
			 Type "multiply" for multiplication of two numbers
			 Type "quit" to leave 
		""")
	#Defining a user input
	user_input = input("What is your option: ")
	#Creating a code block to quit program
	if user_input == "quit":
		break
	#Creating a code block to add numbers	
	elif user_input == "add":
		num1 = float(input("What is the first number?: "))
		num2 = float(input("What is the second number?: "))
		result = str(num1 + num2)
		print(f"The addition of {num1} and {num2} is {result}")
	#Creating a code block to subtract numbers	
	elif user_input == "sub":
		num1 = float(input("What is the first number?: "))
		num2 = float(input("What is the second number?: "))
		result = str(num1 - num2)
		print(f"The subtraction of {num1} and {num2} is {result}")
	#Creating a code block to divide numbers
	elif user_input == "divide":
		num1 = float(input("What is the first number?: "))
		num2 = float(input("What is the second number?: "))
		result = str(num1 / num2)
		print(f"The divison of {num1} and {num2} is {result}")
	#Creating a code block to multiply numbers
	elif user_input == "multiply":
		num1 = float(input("What is the first number?: "))
		num2 = float(input("What is the second number?: "))
		result = str(num1 * num2)
		print(f"The multiplication of {num1} and {num2} is {result}")
	#Creating a code block for non parameters
	else:
		print("Unknown Input")
		