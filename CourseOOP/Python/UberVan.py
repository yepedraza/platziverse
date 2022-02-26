from especialService import EspecialService

class UberVan(EspecialService):
    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver, typeCarAccepted, seatsMaterial)