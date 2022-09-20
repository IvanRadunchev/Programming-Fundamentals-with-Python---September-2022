# text = input()
# symbol = text[1]
# print(symbol * 2)
text = ""
while text != "End":
    text = input()
    if text == "SoftUni":
        continue
    elif text == "End":
        break
    for symbol in range(len(text)):
        print(text[symbol] * 2, end="")
    print()
