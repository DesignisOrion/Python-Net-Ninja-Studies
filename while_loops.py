age = 25
num = 0

# while num < age:
#     print(num)
#     num += 1

# If we wanted to print even numbers but only go to 10 because of break.
# while num < age:
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1

# Learning about the continue keyword.
while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
