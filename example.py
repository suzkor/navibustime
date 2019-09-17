import datetime
from navibustime.navibustime import Navibustime

# サンプル1
bus = Navibustime("00016409", "00016648", "00004254")
print(bus.nextbus(datetime.datetime.now()))
# return ['19:05', '19:25', '19:45']

# サンプル2
bus = Navibustime("00016409", "00016648", "00004254", date="2019-09-22")
print(bus.nextbus(datetime.datetime.now(), count=6))
# return ['19:05', '19:25', '19:45', '20:10', '20:40', '21:10']
