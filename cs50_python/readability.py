import math

s = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"

# s = input("Iput sentence: ")

letter = 0
word = 0
sentence = 0
j = False

for i in range(len(s)):
    if s[i].isalpha():
        letter += 1
        j = True
    elif s[i] == " ":
        if j == True:
            word += 1
            j = False
    elif s[i] == "?" or "!" or ".":
        sentence += 1
        if j == False:
            word += 1
    else:
        continue

L = (letter * 100) / word
S = (sentence * 100) / word
grade = round(0.0588 * L - 0.296 * S - 15.8)

print(letter)
print(word)
print(sentence)
print(grade)

if grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade: {grade}")

