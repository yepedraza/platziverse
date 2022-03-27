# HOW TO BUILD AN ITERATOR?

class EvenNumbers:
    """
    Class that implements an iterator of all even numbers, or even numbers up to a maximum value
    """

    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration