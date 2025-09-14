# 1. Messages Manager

#Create a program that manages messages sent and received by users. You need to keep information about username, their sent and received messages. 
#On the first line, you will receive the capacity of possible messages (total of send and received) kept at once per user. Next, you will be receiving lines with commands until you receive the "Statistics" command. There are three possible commands:
# •	"Add={username}={sent}={received}":
#   o	Add the username and the number of already sent and received messages to your records. 
#   o	If the person with the given username already exists, ignore the line.
# •	"Message={sender}={receiver}":
#   o	If both usernames exist, increase the sender's sent messages by 1 and the receiver's received messages by 1. 
#   o	If anyone reaches the capacity (first check the sender), he/she should be removed from the record, and you should print the following message:
#	"{username} reached the capacity!"
# •	"Empty={username}":
#   o	Delete all records of the given user if he exists. 
#   o	If "All" is given as username - delete all records you have.
#Finally, print the total number of users. On the following lines, print each person with the sum of their sent and received messages.
#Input
# •	On the first line, you will receive the capacity - an integer number in the range [1-10000].
# •	You will be receiving lines until you receive the "Statistics" command.
# •	The initial messages (sent and received) will always be below the capacity.
# •	The input will always be valid.

#Output
# •	Print the appropriate message after the "Message" command if someone reaches the capacity.
# •	Print the users with their messages in the following format: 
# "Users count: {count}
# {username1} - {number of messages}
# {username2} - {number of messages}
#…
#{usernameN} - {number of messages}"

# CODE:

capacity = int(input())
users = {}

while True:
    command = input()
    if command == "Statistics":
        break

    tokens = command.split("=")
    operation = tokens[0]

    if operation == "Add":
        username = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])
        if username not in users:
            users[username] = {"sent": sent, "received": received}

    elif operation == "Message":
        sender = tokens[1]
        recipient = tokens[2]
        if sender in users and recipient in users:
            users[sender]["sent"] += 1
            users[recipient]["received"] += 1

            if users[sender]["sent"] + users[sender]["received"] >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]

            if recipient in users and users[recipient]["sent"] + users[recipient]["received"] >= capacity:
                print(f"{recipient} reached the capacity!")
                del users[recipient]

    elif operation == "Empty":
        username = tokens[1]
        if username == "All":
            users.clear()
        elif username in users:
            del users[username]

print(f"Users count: {len(users)}")
for username in users:
    messages_total = users[username]["sent"] + users[username]["received"]
    print(f"{username} - {messages_total}")
