# 1)  calculate Age of a person - User should enter the year of birth and the program should output the age.
dob = input("Enter your Date of birth: ")
age = (2021 - int(dob))
print(age)


# 2) Simple Calculator:- get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, power of the input numbers

digit_one =int(input("Enter your First number: "))
digit_second = int(input("Enter your second number: "))

print(digit_one + digit_second)
print(digit_one - digit_second)
print(digit_one * digit_second)
print(digit_one // digit_second)
print(digit_one / digit_second)
print(digit_one % digit_second)
print(digit_one ** digit_second)


# 3)  use string functions to count the occurrence of 'y' in a word given by user.

a = input("Enter your text: ")
print(a.count("y"))


# 4) take input of a string and print it's even indexed characters
text = input("Enter your text: ")
print(text[::2])


