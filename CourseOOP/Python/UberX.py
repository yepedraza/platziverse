from normalService import NormalService

class UberX(NormalService):

    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver, brand, model)