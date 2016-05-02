import re

def user_input():
    print("\nType a phrase, sentence, or word here")
    phrase = input("and I'll tell you if it's a palindrome: ")
    return phrase

def is_palindrome(phrase):
    clean_phrase = phrase.lower()
    clean_phrase = re.sub(r'[^A-Za-z]', '', clean_phrase)
    if reverse(clean_phrase) == clean_phrase:
        print("\n{} is a palindrome! \nWay to go!".format(phrase))
        return True
    else:
        print("\n{} is not a palindrome. \nBetter luck next time.".format(phrase))
        return False

def reverse(phrase):
    return phrase [::-1]

def main():
    phrase = user_input()
    if phrase != '':
        is_palindrome(phrase)
    else:
        print("\nYou didn't type anything! \nCome back when you're ready to cooperate.")
        return False

if __name__ == '__main__':
    main()
