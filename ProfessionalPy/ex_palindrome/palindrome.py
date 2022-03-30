def is_palindrome(string: str) -> bool:

    string = string.replace(" ", "").lower() #Cleaning empty spaces and lower method
    return string == string[::-1] #Slices use for verification

def run():

    print(is_palindrome("ana"))

if __name__ == '__main__':
    
    run()