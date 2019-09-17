# navibustime
次のバスの時間を教えてくれるやつ  

## 仕様
NAVITIMEのページからスクレイピングしてる  
日付、時間選択可能  
NAVITIMEでの出発停留所コード、到着停留所コード、路線コードを入れて使う   

## 使い方
まずは各コードを調べる  
例：秋葉原駅前 ⇒ 葛西駅前（都営バス）  
https://www.navitime.co.jp/bus/diagram/timelist?departure=00016409&arrival=00016648&line=00004254  
このdepartureが秋葉原駅前のコード、arrivalが葛西駅前のコード、lineが都営バス秋26の路線コードになってる

これがわかれば取得可能  
サンプルは以下の通り
```python
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
```
コンストラクタの引数は出発停留所コード、到着停留所コード、路線コードの順になってます  
また`date`を渡すことで日付の指定も可能

`next_bus`は何時以降のバスを知りたいかを渡す  
何個知りたいかも`count`で指定可能