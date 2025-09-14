# 1. String Game

#Create a program that executes changes over a string. On the first line, you are going to receive the string. On the following lines, you will be receiving commands until the "Done" command. There are six possible commands:
# •	"Change {char} {replacement}"
#   o	Replace all occurrences of the char with the given replacement, then print the string.
# •	"Includes {substring}"
#   o	Check if the string includes the given substring with and print "True" or "False".
# •	"End {substring}"
#   o	Check if the string ends with the given substring and print "True" or "False".
# •	"Uppercase"
#   o	Make the whole string uppercased, then print it.
# •	"FindIndex {char}"
#   o	Find the index of the first occurrence of the given char, then print it.
# •	"Cut {startIndex} {count}"
#   o	Remove all characters from the string, except those starting from the given start index and the next count of characters. Print only the cut chars.
#Input
# •	On the first line, you are going to receive the string.
# •	On the following lines, until the "Done" command is received, you will be receiving commands.
# •	All commands are case-sensitive.
# •	The input will always be valid.
# Output
# •	Print the output of every command in the format described above.

# CODE:

given_string = input()

while True:
    command = input()
    if command == "Done":
        break

    command_split = command.split()
    operation = command_split[0]

    if operation == "Change":
        char = command_split[1]
        replace = command_split[2]
        given_string = given_string.replace(char, replace)
        print(given_string)

    elif operation == "Includes":
        substring = " ".join(command_split[1:])
        print("True" if substring in given_string else "False")

    elif operation == "End":
        substring = " ".join(command_split[1:])
        print("True" if given_string.endswith(substring) else "False")

    elif operation == "Uppercase":
        given_string = given_string.upper()
        print(given_string)

    elif operation == "FindIndex":
        char = command_split[1]
        print(given_string.find(char))

    elif operation == "Cut":
        starting_index = int(command_split[1])
        count = int(command_split[2])
        ending_index = starting_index + count
        cut_text = given_string[starting_index:ending_index]
        print(cut_text)
