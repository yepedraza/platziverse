import random


def BinarySearch(list, start, end, objetive):

    if start > end:
        return False

    mid = (start + end) // 2

    if list[mid] == objective:
        return True
    elif list[mid] < objective:
        return BinarySearch(list, mid+1, end, objetive)
    else:
        return BinarySearch(list, start, mid-1, objective)

if __name__ == '__main__':
    listSize = int(input('How big will the list be?'))
    objective = int(input('What number do you want to find?'))

    list = [random.randint(0,100) for i in range(listSize)]

    found = BinarySearch(list, 0, len(list)-1, objective)
    print(list)
    print(f'The element {objective} {"is found" if found else "is not found"} in the list')