
class Vehicle:
    def __init__(self, kind, license_plate):
        self.kind = kind
        self.license_plate = license_plate
        
    def get_license_plate(self):
        return self.license_plate

    def get_kind(self):
        return self.kind


class Car(Vehicle):
    def __init__(self, license_plate):
        Vehicle.__init__(self, 'car', license_plate)


class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        Vehicle.__init__(self, 'motorcycle', license_plate)
