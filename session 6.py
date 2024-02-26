# animals = [
#
# {'species': 'zebra', 'name': 'Penelope'},
#
# {'species': 'penguin', 'name': 'Jenn'},
#
# {'species': 'elephant', 'name': 'Harris'},
#
# {'species': 'flamingo', 'name': 'Florence'},
#
# ]
#
# for animal in animals:
#  print(animal['species'])


#Reading a file (r) or write a file (w+)
# with open('people.txt' , 'w+') as text_file:
#
#      people='Joanne  \nSusan \nAmina'
#
#      text_file.write(people)

# with open('people.txt' , 'r') as text_file:
#      contents=text_file.read()
#
# print(contents)


# # Step 1: Ask the user to input a new to-do item
# new_item = input("Enter a new to-do item: ")
#
# # Step 2: Read the contents of the existing to-do items
#
# with open("todo.txt", "r") as todo_file:
#     todo=todo_file.read()
# print(todo)
#
# # Step 3: Add the new to-do item to the existing to-do items
# todo=todo+ new_item +'\n'
#
# # Step 4: Save the updated to-do list
# with open("todo.txt", "w+") as todo_file:
#         todo_file.write(todo)
#
# with open("todo.txt", "r") as todo_file:
#     todo=todo_file.read()
# print(todo)

#Writing and Reading into a CSV file
# import csv
#
# field_names=['name' , 'age']
#
# data = [
#     {'name': 'Jill', 'age': 32},
#     {'name': 'Sara', 'age': 28},
#
# ]
#
# with open('team.csv', 'w+', newline="") as csv_file:
#
#     spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
#     spreadsheet.writeheader()
#     spreadsheet.writerows(data)

# # Reading a CSV
# import csv
#
# with open('team.csv', 'r') as csv_file:
#
#     spreadsheet= csv.DictReader(csv_file)
#
#     for row in spreadsheet:
#         print(dict(row))

# import csv
#
# with open('trees.csv', 'r') as csv_file:
#
#     spreadsheet=csv.DictReader(csv_file)
#
#     heights = []
#
# for row in spreadsheet:
#
#     tree_height = row['height']
#
# heights.append(tree_height)
#
# shortest_height = min(heights)
#
# print(shortest_height)

# Using PIP
