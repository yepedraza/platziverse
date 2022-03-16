import random

def MergeSort(list):

    if len(list) > 1:

        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print(left, '*' * 5, right)

        #Recursive call each half
        MergeSort(left)
        MergeSort(right)

        #Sublists
        i = 0
        j = 0
        #Main list
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        
        print(f'Left {left}, Right {right}')
        print(list)
        print('-' * 50)

    return list


if __name__ == '__main__':

    listSize = int(input('How big will the list be?'))

    list = [random.randint(0,100) for i in range(listSize)]
    print(list)
    print('-' * 20)

    orderedList = MergeSort(list)
    print(orderedList)
