import os
import requests
import json
import datetime
from DB import controller

headers = dict()
headers["user-agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
)
headers["referer"] = "https://edition.cnn.com"
headers["origin"] = "https://edition.cnn.com"
headers["accept"] = "*/*"

os.getenv("DB_PORT", "")

res = requests.get(
    "https://production.dataviz.cnn.io/index/fearandgreed/graphdata", headers=headers
)

try:
    data = json.loads(res.text)["fear_and_greed_historical"]["data"]

    for d in data:
        try:
            _date = datetime.date.fromtimestamp(int(d["x"]) / 1000)
            controller.insert(_date, int(d["y"]))
        except:
            pass  # pass duplicate keys
except Exception as e:
    pass