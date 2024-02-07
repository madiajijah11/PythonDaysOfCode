# Create a program that removes the nth element from a list.


def remove_nth_element():
    user_list = input("Enter a list of numbers separated by a space: ")
    user_list = user_list.split()
    n = int(input("Enter the index of the element to remove: "))
    user_list.pop(n)
    print(user_list)


remove_nth_element()
