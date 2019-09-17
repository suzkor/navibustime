import datetime
from navibustime.navibustime import Navibustime

bus = Navibustime("00139514", "00043845", "00032186")
print(bus.nextbus(datetime.datetime.now()))
