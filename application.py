from vehicle import Car, Motorcycle
from parking_space import ParkingSpace

class Application:
    parking_space = None

    def run(self, max_car, max_motorcycle, events):
        self.parking_space = ParkingSpace(max_car, max_motorcycle)
        for event in events:
            event_data = event.split(' ')
            if event_data[0] == 'Enter':
                _, kind, licence_plate, timestamp = event_data
                self.event_enter(kind, licence_plate, timestamp)
            else:
                _, licence_plate, timestamp = event_data
                self.event_exit(licence_plate, timestamp)
            
    def event_exit(self, licence_plate, timestamp):
        kind, lot_number, fee = self.parking_space.exit(licence_plate, int(timestamp))
        print('{}Lot{} {}'.format(kind.capitalize(), lot_number, fee))

    def event_enter(self, kind, licence_plate, timestamp):
        vehicle = self.set_vehicle(kind, licence_plate)
        lot_number = self.parking_space.enter(vehicle,int(timestamp))
        if lot_number:
            print('Accept {}Lot{}'.format(kind.capitalize(), lot_number))
        else:
            print('Reject')

    def set_vehicle(self,  kind, licence_plate):
        if kind == 'car':
            vehicle = Car(licence_plate)
        elif kind == 'motorcycle':
            vehicle = Motorcycle(licence_plate)

        return vehicle


def multi_input():
    try:
        while True:
            data = input()
            if not data: break
            yield data
    except EOFError:
        return


if __name__ == '__main__':
    user_input = list(multi_input())
    lots = user_input[0].split(' ')
    max_car = lots[0] # space for Cars
    max_motorcycle = lots[1] # space for Motorcycles
    user_input.pop(0)
    app =  Application()
    app.run(int(max_car), int(max_motorcycle), user_input)