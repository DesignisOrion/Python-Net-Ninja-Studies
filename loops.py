students = ['ryu', 'crystal', 'yoshi', 'ken']

# for student in students:
#     print(student)


# looping through a section of the list
# for student in students[1:3]:
#     print(student)


for student in students:
    if student == 'yoshi':
        print(f'{student} - black belt')
        break  # This is how you break out of a loop
    else:
        print(student)
