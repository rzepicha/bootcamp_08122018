class ElectricCar:
    def __init__(self,zasieg):
        self.zasieg=zasieg
        self._traveled_distance=0

    def drive(self, dystans):
        if self._traveled_distance+dystans>self.zasieg:
            to_travel=self.zasieg-self._traveled_distance
            self._traveled_distance=self.zasieg
            return to_travel
        else:
            self._traveled_distance+=dystans
            return dystans

    def charge(self):
        self._traveled_distance=0




def test_electric_car_init():
    car=ElectricCar(100)
    assert car.zasieg==100

def test_electric_car_drive():
    car=ElectricCar(100)
    assert car.drive(50)==50
    assert car.drive(50)==50
    assert car.drive(50)==0

def test_electric_drive_over_zasieg():
    car=ElectricCar(100)
    assert car.drive(130)==100

def testelectric_car_charge():
    car=ElectricCar(100)
    assert car.drive(100)==100
    assert car.drive(1)==0
    car.charge()
    assert car.drive(1)==1




#mój
# def drive2(dystans, zasieg):
#     if dystans in range (0,zasieg):
#         zasieg-=dystans
#         print(f"zostało: {zasieg} km zasięgu ")
#     if dystans>zasieg:
#         dystans -= zasieg
#         print(f"brakuje ci: {dystans} km")
#
# print(drive2(20,100))
# print(drive2(120,100))
