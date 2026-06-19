import json
import urllib.request
from datetime import datetime, timezone, timedelta

url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw|tse_00631L.tw&json=1&delay=0'
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())

stocks = {}
for s in data.get('msgArray', []):
    code = s['c'].upper()
    z = s.get('z', '-')
    y = s.get('y', '0')
    price = float(z) if z and z != '-' else float(y)
    prev = float(y) if y else price
    stocks[code] = {'price': price, 'prev': prev}

tw = datetime.now(timezone(timedelta(hours=8)))
result = {'updated': tw.strftime('%Y-%m-%d %H:%M'), 'stocks': stocks}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)

print(json.dumps(result, ensure_ascii=False))
