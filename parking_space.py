from vehicle import Vehicle
import math

class ParkingLot():
    FEES = {
        'car': 2,
        'motorcycle': 1,
    }

    def __init__(self, vehicle: Vehicle, timestamp):
        self.vehicle = vehicle
        self.timestamp = timestamp

    def get_fee(self, timestamp):
        kind =  self.vehicle.get_kind()
        fee_per_hour = self.FEES[kind]
        hours = math.ceil((timestamp - self.timestamp)/3600)

        return fee_per_hour * hours

    def get_timestamp(self):
        return self.timestamp

class ParkingSpace:
    parking_lots = {}
    vehicles = {}

    def __init__(self, max_cars, max_motorcycle):
        self.max_cars = max_cars
        self.max_motorcycle = max_motorcycle
        self.init_vieachel_lots('car', max_cars)
        self.init_vieachel_lots('motorcycle', max_motorcycle)

    def init_vieachel_lots(self, kind, max):
        """ 
        Setup parking log for cars and motorcycles.
        Initial value is None, means empty lot
        """
        self.parking_lots[kind] = [None for _ in range(max)]
    
    def get_max_vehicle_lots(self, kind):
        return len(self.parking_lots[kind])

    def enter(self, vehicle: Vehicle, timestamp):
        license_plate = vehicle.get_license_plate()
        if not self.valid_to_enter(license_plate):
            return False

        kind = vehicle.get_kind()
        lot = self.get_available_lot(kind)
        if lot < 0:
            return False

        self.parking_lots[kind][lot] = ParkingLot(vehicle, timestamp)

        self.vehicles[license_plate] = { 
            'lot': lot,
            'kind': kind
        }
        lot_number = lot+1
        return lot_number

    def exit(self, license_plate, timestamp):
        if not self.valid_to_exit(license_plate):
            return False

        kind = self.vehicles[license_plate]['kind']
        lot = self.vehicles[license_plate]['lot']

        parking_lot = self.parking_lots[kind][lot]
        self.remove_vehicle(kind, lot, license_plate)
        fee =  parking_lot.get_fee(timestamp)
        lot_number = lot+1
        
        return kind, lot_number, fee

    def valid_to_enter(self, license_plate):
        if license_plate in self.vehicles:
            return False

        return True

    def valid_to_exit(self, license_plate):
        if license_plate in self.vehicles:
            return True

        return False

    def get_available_lot(self, kind):
        lots = self.parking_lots[kind]
        for index, lot in enumerate(lots):
            if not lot:
                return index

        return -1
    
    def remove_vehicle(self, kind, lot, license_plate):
        self.parking_lots[kind][lot] = None
        del self.vehicles[license_plate]