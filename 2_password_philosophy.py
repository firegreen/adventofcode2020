from password_philosophy_input import input

result = 0
for password in input:
    rule, password = password.split(": ")
    occurence, char = rule.split(" ")
    min, max = [int(value)-1 for value in occurence.split('-')]
    if (password[min] == char) != (password[max] == char):
        result += 1

print(result)
