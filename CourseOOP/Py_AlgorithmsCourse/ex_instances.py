
class Coordinate:

    def __init__(self, x, y):

        self.x = x
        self.y = y
    
    def distancia(self, other_coord):
        x_diff = (self.x - other_coord.x)**2
        y_diff = (self.y - other_coord.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordinate(3, 30)
    coord_2 = Coordinate(4, 8)

    #print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordinate))