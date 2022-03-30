from datetime import datetime

def execution_time(func):
    
    def wrapper(*args, **kwargs): # *args and **kwargs --> Doesn't matter the number of arguments
                                  #  or key arguments gived to the nested function
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")

    return wrapper

@execution_time
def Random_func():
    for _ in range(1, 10000000):
        pass

@execution_time
def Addition(a: int, b: int) -> int:
    return a + b

@execution_time
def Greeting(name = " "):
    print("Hey " + name + "!")

def run():
    Random_func()
    Addition(5, 5)
    Greeting("Yery")

if __name__ == '__main__':
    run()