
class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'resting'
        self._motor = Motor(cylinders=4)

    def accelerate(self, a_type='slow'):
        if a_type == 'fast':
            self._motor.inyect_gasoline(10)
        else:
            self._motor.inyect_gasoline(3)
        
        self._state = 'moving'

class Motor:

    def __init__(self, cylinders, c_type='gasoline'):
        self.cylinders = cylinders
        self.c_type = c_type
        self._temperature = 0

    def inyect_gasoline(self, quantity):
        pass
