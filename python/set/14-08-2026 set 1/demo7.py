'''
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
'''
alpha = set("abcdefghijklmnopqrstuvwxyz")
n = ""
while True:
    print("\n===== MISSING ALPHABET FINDER =====")
    print("1. Enter sentence")
    print("2. Display Missing alphabets")
    print("3. Count Missing alphabets")
    print("4. Exit")
    choice = int(input("Enter the choice: "))
    match choice:
        case 1:
            n = input("Enter your sentence: ").lower()
            print("Your sentence is:", n)
        case 2:
            if n == "":
                print("Please enter a sentence first.")
            else:
                print("Missing alphabets are:", (alpha - set(n)))
        case 3:
            if n == "":
                print("Please enter a sentence first.")
            else:
                print("Missing alphabets are:", len(alpha -set(n)))
        case 4:
            print("Program ended.")
            break

        case _:
            print("Invalid choice!")