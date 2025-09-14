# 1. Boss Rush

#Create a program that checks if inputs are valid. On the first line, you will receive a number that indicates how many inputs you will receive on the following lines.

#You will read lines with a boss name and title, and you should check if they are valid, considering the following rules:
# •	Boss - the name should be
#   o	In upper case letters
#   o	Minimum four letters long
#   o	Surrounded by "|"
# •	Title – should:
#   o	It contains exactly 2 words, and they contain only alphabetical letters and 1 whitespace between them.
#   o	Surrounded by "#"
# •	The name and title should be split by a single ":"
#Example for a valid input:  |GEORGI|:#Lead architect#
#If the input is valid. Print in the following format:

#"{boss name}, The {title}

#>> Strength: {length of the name}
#>> Armor: {length of the title}"

#If the input is invalid, print "Access denied!"

#Input / Constraints
# •	On the 1st line, you will receive the number of inputs.
# •	On the following n lines, you will have to check if a boss has a valid name and title.

#Output
#•	Print the output with the format described above.

# CODE:

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    input_line = input()

    if ":" not in input_line:
        print("Access denied!")
        continue

    tokens = input_line.split(":", 1)

    if len(tokens) != 2:
        print("Access denied!")
        continue

    name = tokens[0]
    title = tokens[1]

    if not (name.startswith("|") and name.endswith("|")):
        print("Access denied!")
        continue

    boss_name = name[1:-1]

    if not (boss_name.isupper() and boss_name.isalpha() and len(boss_name) >= 4):
        print("Access denied!")
        continue

    if not (title.startswith("#") and title.endswith("#")):
        print("Access denied!")
        continue

    title_body = title[1:-1]

    title_words = title_body.split(" ")

    if len(title_words) != 2 or not all(word.isalpha() for word in title_words):
        print("Access denied!")
        continue

    print(f"{boss_name}, The {title_body}")
    print(f">> Strength: {len(boss_name)}")
    print(f">> Armor: {len(title_body)}")
