def Capital_letter(func): #This function receive another function
    
    def Wrapper(text): 
        return func(text).upper()

    return Wrapper

@Capital_letter
def message(name):
    return f'{name}, you have received a message'

print(message('Yery'))