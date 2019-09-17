import json
import requests as rq
import datetime
from bs4 import BeautifulSoup


class Navibustime:
    url = ""
    deptime_list = []

    def __init__(self, departure, arrival, line,
                 date=datetime.datetime.now().strftime("%Y-%m-%d"), hour="0"):
        self.url = "https://www.navitime.co.jp/bus/diagram/timelist?hour=" + hour + "&departure=" + departure + "&arrival=" + arrival + "&line=" + line + "&date=" + date
        print(self.url)
        html = rq.get(self.url)
        try:
            soup = BeautifulSoup(html.text, "html.parser")
            timelist = soup.find("dl", attrs={"class", "time-list-frame"})
            deplist = timelist.find_all("span", attrs={"class", "time dep"})

            now = datetime.datetime.now().strftime("%Y/%m/%d ")
            for l in deplist:
                self.deptime_list.append([datetime.datetime.strptime(now + l.text, "%Y/%m/%d %H:%M"), l.text])
        except Exception as e:
            print(e)

    def nextbus(self, time,count=3):
        nextbustime = []
        for deptime in self.deptime_list:
            if deptime[0] > time:
                nextbustime.append(deptime[1])

        result = []
        try:
            for i in range(count):
                result.append(nextbustime[i])
        except Exception as e:
            print(e)
        return result
