class Route:
    id = int
    start = []
    end = []

    def __init__(self, start, end):
        self.start = start
        self.end = end