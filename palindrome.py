import re

def user_input():
    print("\nType a phrase, sentence, or word here")
    phrase = input("and I'll tell you if it's a palindrome: ")
    print("\n")
    return phrase

def is_palindrome(phrase):
    phrase = phrase.lower()
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    if reverse(phrase) == phrase:
        print("It is a palindrome! Way to go!")
    else:
        print("It is not a palindrome. Better luck next time.")

def reverse(phrase):
    # reverse the phrase typed to check if its a palinderome
    phrase = phrase.lower()
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    if len(phrase) == 0:
        return ""
    return reverse(phrase[1:]) + phrase[0]

def main():
    phrase = user_input()
    if phrase != '':
        is_palindrome(phrase)
    else:
        print("You didn't type anything!")
        print("Come back when you're ready to cooperate.")
        return False
main()
