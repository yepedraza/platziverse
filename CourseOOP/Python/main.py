from car import Car

if __name__ == "__main__":
    print('Hola mundo')

    car = Car()
    car.license = "AMS234"
    car.driver = "Yery Pedraza"
    car.passenger = 4
    print(vars(car))

    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Agusto Agudelo"
    car2.passenger = 3
    print(vars(car2))