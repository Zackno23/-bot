import requests
import json
import sys
from get_wifi_SSID import WiFiUtil
import time
import subprocess

wifi_SSID = ''
counter = 0
while wifi_SSID == '':
    if counter == 10:
        sys.exit()
    time.sleep(2)
    counter += 1
    wifi_SSID = WiFiUtil.getUsingSSID()


def main():
    fname = "cfg.json"
    with open(fname, "r") as f:
        cfg = json.load(f)
        params = {"entry.{}".format(cfg["entry"][k]): cfg["output"][k] for k in cfg["entry"].keys()}
        res = requests.get(cfg["form_url"] + "formResponse", params=params)
    if res.status_code == 200:
        print("Done!")
    else:
        res.raise_for_status()
        print("Error")
    print(res.url)


if __name__ == '__main__':
    if wifi_SSID in ('kigyoshimin@member', 'kigyoshimin@guest'):
        main()
    else:
        sys.exit()
