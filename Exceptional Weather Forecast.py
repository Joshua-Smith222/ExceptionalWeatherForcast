def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    return (fahrenheit - 32) * 5/9

def main():
    try:
        # Task 1: Ask the user to enter the temperature in Fahrenheit
        fahrenheit = input("Please enter the temperature in Fahrenheit: ")
        fahrenheit = float(fahrenheit)  # Convert input to a float
    except ValueError:
        # Handle the case where the user does not enter a valid number
        print("Error: Invalid input. Please enter a numeric value for the temperature.")
    else:
        # Task 2: Temperature conversion
        celsius = fahrenheit_to_celsius(fahrenheit)
        # Task 3: User Experience - Display the result in a user-friendly format
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        # Task 4: Finally block - Thank the user
        print("Thank you for using the weather forecast application!")

# Run the application
main()
