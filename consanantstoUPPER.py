string = input()

vowels = "AEIOUaeiou"
result =" "

for i in string:
    if i not in vowels:
        result = result + i.upper()
    else:
        result = result + i

print(result)