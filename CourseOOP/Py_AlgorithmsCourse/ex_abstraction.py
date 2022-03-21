
class Washing_machine:

    def __init__(self):
        pass

    def wash(self, temperature='cold'):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_water_tank(self, temperature):
        print(f'Filling the tank with {temperature} water')

    def _add_soap(self):
        print('Adding soap')
    
    def _wash(self):
        print('Washing the clothes')

    def _centrifuge(self):
        print('Centrifuging the clothes')

if __name__ == '__main__':
    washing_machine = Washing_machine()
    washing_machine.wash()