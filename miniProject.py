
   
numbers = []  # List to store the numbers

while True: 
    userInput = input("Enter a number: ")

    if userInput.isdigit():  # Optional: make sure it's a number
        num = int(userInput)
        numbers.append(num)  # Add number to the list

        if num % 2 == 0:
            print("Even number")
            break # break the loop if the number is even
        else: 
            print(f"Odd number, {num}")
    else:
        print("Please enter a valid number.")

print("All entered numbers:", numbers)
