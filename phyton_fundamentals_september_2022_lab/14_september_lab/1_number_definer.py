number = float(input())
if number == 0:
    print('zero')
if 0 < number > 1 and number < 1000000:
    print("positive")
elif 0 < number < 1:
    print("small positive")
if number > 1000000:
    print("large positive")
# if number < 0:
#     print("negative")

if -1 < number < 0:
    print("small negative")
elif -1000000 < number < -1 and number < 0:
    print("negative")
elif number < -1000000:
    print("large negative")
