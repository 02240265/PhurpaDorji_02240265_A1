#Part A :Python Functions Assignment
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def Calulating_the_sum_of_prime_number(start, end):
    return sum(num for num in range(start, end + 1) if is_prime(num))

def length_converter(value, direction):
    if direction == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # Feet to meters
    else:
        raise ValueError("Invalid choice physco. Use 'M' for meters to feet or 'F' for feet to meters.")

def counting_consonants(text):
    consonants = "abcdefghijklmnopqrstuvwxyz"
    return sum(1 for char in text if char in consonants)

def min_max_finder(numbers):
    return min(numbers), max(numbers)

def iChecking_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char != ' ')
    return cleaned_text == cleaned_text[::-1]

def word_counting(text):
    words_to_count = ["the", "was", "and"]
    text_lower = text.lower()
    return {word: text_lower.split().count(word) for word in words_to_count}

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_menu():
    print("\nSelect a number (1-6):")
    print("1. Calculate the sum of prime numbers")
    print("2. Convert length units")
    print("3. Count consonants in string")
    print("4. Find min and max numbers")
    print("5. Check for palindrome")
    print("6. Word Counter")
    print("0. Exit program")

def main():
    while True:
        display_menu()
        choice = get_integer_input("Enter your choice: ")

        if choice == 0:
            print("Exit the progranm. Thank you for ur the time and Goodbye!")
            break
        elif choice == 1:
            start = get_integer_input("Enter the start of the range: ")
            end = get_integer_input("Enter the end of the range: ")
            if start > end:
                print("Invalid range. Start must be less than or equal to end.")
            else:
                print(f"Sum of prime numbers between {start} and {end}: {Calulating_the_sum_of_prime_number(start, end)}")
        elif choice == 2:
            value = get_float_input("Enter the length value: ")
            direction = input("Enter 'M' for meters to feet or 'F' for feet to meters: ").upper()
            try:
                print(f"Converted length: {length_converter(value, direction)}")
            except ValueError as e:
                print(e)
        elif choice == 3:
            text = input("Enter a string: ")
            print(f"Number of consonants: {counting_consonants(text)}")
        elif choice == 4:
            numbers = []
            count = get_integer_input("How many numbers do you want to enter charo? ")
            for i in range(count):
                num = get_float_input(f"Enter number {i + 1}: ")
                numbers.append(num)
            min_num, max_num = min_max_finder(numbers)
            print(f"Smallest: {min_num}, Largest: {max_num}")
        elif choice == 5:
            text = input("Enter a string: ")
            print(f"Is palindrome: {iChecking_palindrome(text)}")
        elif choice == 6:
            text = input("Enter a text: ")
            word_counts = word_counting(text)
            for word, count in word_counts.items():
                print(f"'{word}' occurs {count} times.")
        else:
            print("Invalid choice. Please select a number between 0 and 6.")

        if choice != 0:
            again = input("Would you like to try another function? (y/n): ").lower()
            if again != 'y':
                print("Exit the program. Thank you for ur time and Goodbye!")
                break

if __name__ == "__main__":
    main()