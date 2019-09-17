import datetime
from navibustime.navibustime import Navibustime

bus = Navibustime("00016409", "00016648", "00004254")
print(bus.nextbus(datetime.datetime.now()))
