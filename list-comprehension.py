h_letters = []

# creating a list from a string
for letter in 'human':
    h_letters.append(letter)

print(h_letters)


# creating a list using comprehension
h_letters = [letter for letter in 'human']
print(h_letters)


# conditionals in list comprehension
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# modifying the selector
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)


# transpose without comprehension
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


# transpose with comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
