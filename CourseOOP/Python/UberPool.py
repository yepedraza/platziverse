from normalService import NormalService

class UberPool(NormalService):
    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver, brand, model)