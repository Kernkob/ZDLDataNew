## Input ##
initial_victors = input("List the initial victors (sep by \", \"): ")
new_victors = input("List the GTR victors (sep by \", \"): ")

## List edit ##

initial_list = initial_victors.split(", ")
new_list = new_victors.split(", ")

for victor in new_list:
    if victor not in initial_list:
        initial_list.append(victor)

new_str = ", ".join(initial_list)
print()
print("New list: ")
print(new_str)

input()