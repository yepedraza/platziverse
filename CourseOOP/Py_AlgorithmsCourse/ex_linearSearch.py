import random

def LinearSearch(list, objective):

    match = False

    for element in list:
        if element == objective:
            match = True
            break
    
    return match


if __name__ == '__main__':

    listSize = int(input('How big will the list be?'))
    objective = int(input('What number do you want to find?'))

    list = [random.randint(0,100) for i in range(listSize)]

    found = LinearSearch(list, objective)
    print(list)
    print(f'The element {objective} {"is found" if found else "is not found"} in the list')