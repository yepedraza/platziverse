from functools import reduce

def Filter():

    #Filter with list comprehensions:
    my_list = [1,4,5,6,9,13,19,21]

    odd = [i for i in my_list if i % 2 != 0]

    #Filter function:
    odd2 = list(filter(lambda x: x % 2 != 0, my_list))

    print(odd, odd2)

def Map():
    
    #Map with list comprehensions:
    my_list = [1,2,3,4,5]

    squares = [i**2 for i in my_list]

    #Map function
    squares2 = list(map(lambda x: x**2, my_list))

    print(squares, squares2)

def Reduce():

    #Reduce with cycles
    my_list = [2,2,2,2,2]

    all_multiplied = 1

    for i in my_list:
        all_multiplied = all_multiplied * i
    
    #Reduce function
    all_multiplied2 = reduce(lambda a,b: a*b, my_list)

    print(all_multiplied, all_multiplied2)

def run():
    pass



if __name__ == '__main__':
    run()