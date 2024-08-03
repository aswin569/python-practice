array = input("Enter an array:")
print(array)
count  =0
for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        if array[i] == array[j] and array[i] != " " and array[j] != " ":
            count = count +1
print(count)