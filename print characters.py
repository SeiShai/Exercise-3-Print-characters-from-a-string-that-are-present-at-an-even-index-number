# Write a program to accept a string from the user and
# display characters that are present at an even index number.

# input
input_word = str(input('enter a word: '))
print('showing the even index characters of the word: ', input_word)

# calculate the length of the word
length = len(input_word)
for i in range(0, length, 2):
    print(input_word[i])
