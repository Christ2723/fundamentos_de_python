# Print characters from a string that are present at an even index number

given_string = input('Enter a string: ')

even_chars = []
odd_chars = []

for i in range(len(given_string)):
    if i % 2 == 0:
        even_chars.append(given_string[i])
    else:
        odd_chars.append(given_string[i])

print('Odd characters: {}'.format(odd_chars))
print('Even characters: {}'.format(even_chars))