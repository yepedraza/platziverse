from car import Car
from account import Account

if __name__ == "__main__":
    print('Hola mundo')

    car = Car("AMS234", Account("Yery Pedraza", "ABC123"))
    print(vars(car))
    print(vars(car.driver))

    # car2 = Car()
    # car2.license = "QWE567"
    # car2.driver = "Agusto Agudelo"
    # car2.passenger = 3
    # print(vars(car2))