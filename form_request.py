import requests
import json
import sys
from get_wifi_SSID import WiFiUtil
import time
import datetime

'''
時間の出力：main()と例外時に出力
'''
date_now, time_now = datetime.datetime.now().split(' ')
year, month, date = date_now.split('-')
hour, minuits, second = time_now.split('-')
wifi_SSID = ''
counter = 0
while wifi_SSID == '':
    if counter == 10:
        sys.exit()
    time.sleep(2)
    counter += 1
    wifi_SSID = WiFiUtil.getUsingSSID()


def main():
    # fname = "entry.json" <- 起動時にファイル名指定だと ファイルが見つからないと言われるのでフルパス指定
    with open('/Users/yoshidachikara/PycharmProjects/slack_bot/entry.json', "r") as f:
        entry = json.load(f)
        params = {"entry.{}".format(entry["entry"][k]): entry["output"][k] for k in entry["entry"].keys()}
        res = requests.get(entry["form_url"] + "formResponse", params=params)
    with open('/Users/yoshidachikara/PycharmProjects/slack_bot/SSID.txt', mode="w") as f:
        f.write(f"{year}年{month}月{date}日{time}時{minuits}分\n入室ボタンを押しました！\nSSIDは{wifi_SSID}です！")




if __name__ == '__main__':
    if wifi_SSID in ('kigyoshimin@member', 'kigyoshimin@guest'):
        main()
    else:
        with open('/Users/yoshidachikara/PycharmProjects/slack_bot/SSID.txt', mode="w") as f:
            f.write(f'ssidは{wifi_SSID}です\n時間は{year}年{month}月{date}日{time}時{minuits}分です')
    sys.exit()
