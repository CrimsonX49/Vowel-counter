print("Welcome to my Vowel counter!")

def vowel_counter(user_input):
    count = 0
    vowels = ("AEIOUaeiou")
    user_input = input("Please enter a word, phrase, or paragraph: ")
    if user_input == "" or None:
        raise ValueError("Please enter a word!")
    for letter in user_input:
         if letter in vowels:
             count = count + 1
    print(f"Number of vowels: {count}!")
    while True:
        next_query = input("Count more vowels? Y/N?")
        if next_query == "Y" or next_query == "y":
            break
        elif next_query == "N" or next_query == "n":
            print("Goodbye! :)")
            break 

vowel_counter(()) 