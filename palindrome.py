# cheking if the  given number is palindrome or not

def is_palindrome(number):
    print("String:", number)
    # reverse the given string
    reversed_number = number[::-1]
    # check if the original string is equal to its reverse
    if number == reversed_number:
        print("Given string is a palindrome")
    # if not then print that the given string is not a palindrome
    else:
        print("Given string is not a palindrome")

is_palindrome("2002")
is_palindrome("2004")