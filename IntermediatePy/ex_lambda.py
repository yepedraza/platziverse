def run():
    palindrome = lambda word: word == word[::-1]

    print(palindrome('oso'))



if __name__ == '__main__':
    run()