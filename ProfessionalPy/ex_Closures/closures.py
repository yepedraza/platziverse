def make_repeater_of(n):
    
    def repeater(string):
        assert type(string) == str, "You can only use strings"
        return string * n

    return repeater

def run():

    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hey"))

    repeat_3 = make_repeater_of(3)
    print(repeat_3("Yery"))

    repeat_6 = make_repeater_of(6)
    print(repeat_6("Platzi"))

if __name__ == '__main__':

    run()