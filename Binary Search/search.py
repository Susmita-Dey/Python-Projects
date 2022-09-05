# Binary Search Algorithm
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# (first+last)/2 = (0+9)/2

# Algorithm:
# function that takes a list and target parameter
# multiples variables: middle, start, endd, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Step", steps, ":", str(list[start:end+1]))
        steps = steps+1
        middle = (start+end)//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle-1
        else:
            start = middle+1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 12
target = int(input("Enter a number you want to search in the list: "))

binary_search(my_list, target)
# f = binary_search(my_list, target)
# print(f)
