import unittest
from vehicle import Car, Motorcycle
from parking_space import ParkingSpace

class TestParkingSpace(unittest.TestCase):

    def test_max_parking_lots(self):
        max_car = 3
        max_motorcycle = 4
        parking_space = ParkingSpace(max_car, max_motorcycle)
        max_car_allowed = parking_space.get_max_vehicle_lots('car')
        self.assertEqual(max_car_allowed, max_car)
        max_motorcycle_allowed = parking_space.get_max_vehicle_lots('motorcycle')
        self.assertEqual(max_motorcycle_allowed, max_motorcycle)

    def test_max_parking_lots(self):
        max_car = 3
        max_motorcycle = 4
        parking_space = ParkingSpace(max_car, max_motorcycle)

        lot_number = parking_space.enter(Motorcycle('SGX1234A'), 1613541902)
        self.assertEqual(lot_number, 1)

        lot_number = parking_space.enter(Car('SGF9283P'), 1613541902)
        self.assertEqual(lot_number, 1)
        
        kind, lot_number, fee = parking_space.exit('SGX1234A', 1613545602)
        self.assertEqual(kind, 'motorcycle')
        self.assertEqual(lot_number, 1)
        self.assertEqual(fee, 2)

        lot_number = parking_space.enter(Car('SGP2937F'), 1613546029)
        self.assertEqual(lot_number, 2)

        lot_number = parking_space.enter(Car('SDW2111W'), 1613549730)
        self.assertEqual(lot_number, 3)

        lot_number = parking_space.enter(Car('SSD9281L'), 1613549740)
        self.assertEqual(lot_number, False)

        kind, lot_number, fee = parking_space.exit('SDW2111W', 1613559745)
        self.assertEqual(kind, 'car')
        self.assertEqual(lot_number, 3)
        self.assertEqual(fee, 6)
 

if __name__ == '__main__':
    unittest.main()