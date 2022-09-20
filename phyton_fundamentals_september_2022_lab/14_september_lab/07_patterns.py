number = int(input())
for loop in range(1, number + 1):
    print(loop * "*")
for second_loop in range(number - 1, 0, -1):
    print(second_loop * "*")
