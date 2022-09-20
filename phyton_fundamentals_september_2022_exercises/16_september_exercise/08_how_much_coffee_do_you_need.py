# command = ""
# cap_of_coffee = 0
# while command != "END":
#     command = input()
#     if command == "coding" or command == "dog" or command == "cat" or command == "movie":
#         cap_of_coffee += 1
#     elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
#         cap_of_coffee += 2
#     else:
#         continue
# if cap_of_coffee > 5:
#     print("You need extra sleep")
# else:
#     print(cap_of_coffee)

# ВТОРИ НАЧИН - КАКТО ГО РЕШИ ЛЕКТОРА
command = input()
cap_of_coffee = 0
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            cap_of_coffee += 1
        else:
            cap_of_coffee += 2
    command = input()
if cap_of_coffee > 5:
    print("You need extra sleep")
else:
    print(cap_of_coffee)
