import requests
import json


def sync_log_es():
    log_pat = "data_utf8.json"
    with open(log_path, "rb") as f:
        count = 0
        for line in f:
            data = json.loads(line)
            res = requests.put("http://114.215.104.130:9200/zhidao", data=data)
            print res
            count += 1
    print "over!!"
