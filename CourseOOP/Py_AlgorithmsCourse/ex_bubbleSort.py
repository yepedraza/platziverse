import random
from socket import if_nameindex

def BubbleSort(list):

    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n**2)

            if list[j] > list [j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

if __name__ == '__main__':

    listSize = int(input('How big will the list be?'))

    list = [random.randint(0,100) for i in range(listSize)]
    print(list)

    orderedList = BubbleSort(list)
    print(orderedList)