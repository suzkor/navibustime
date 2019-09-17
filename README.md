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
サンプルは以下
```python
import datetime
from navibustime.navibustime import Navibustime


bus = Navibustime("00139514", "00043845", "00032186")
print(bus.nextbus(datetime.datetime.now()))

```
