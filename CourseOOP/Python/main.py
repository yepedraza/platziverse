from UberBlack import UberBlack
from UberX import UberX
from normalService import NormalService
from car import Car
from account import Account

if __name__ == "__main__":
    print('Hola mundo')

    # car = Car("AMS234", Account("Yery Pedraza", "ABC123"))
    # print(vars(car))
    # print(vars(car.driver))

    uberX = UberX("TYU159", Account("Agusto Pedraza", "AW123"), "Subaru", "Impreza")
    print(vars(uberX))

    uberBlack = UberBlack("GBN761", Account("Yery Pedraza", "GH894"), "Audi_A6", "Leather")
    print(vars(uberBlack))

    # car2 = Car()
    # car2.license = "QWE567"
    # car2.driver = "Agusto Agudelo"
    # car2.passenger = 3
    # print(vars(car2))