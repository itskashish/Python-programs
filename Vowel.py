
a = input("Enter your word: ")

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in a:
    if i.lower() in vowels:  # Convert i to lowercase to handle both lowercase and uppercase vowels
        count += 1

if count == 0:
    print("No vowels found in the word.")
else:
    print("Number of vowels in the word is:", count)


