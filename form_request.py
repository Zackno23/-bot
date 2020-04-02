import requests
import json
import sys
from get_wifi_SSID import WiFiUtil
import time
import datetime
import display_message
'''
時間の出力：main()と例外時に出力
'''
date_now, time_now = str(datetime.datetime.now()).split(' ')
year, month, date = date_now.split('-')
hour, minuits, second = time_now.split(':')
wifi_SSID = WiFiUtil.getUsingSSID()
counter = 0
ssid_txt = '/Users/yoshidachikara/PycharmProjects/slack_bot/SSID.txt'
entry_json = '/Users/yoshidachikara/PycharmProjects/slack_bot/entry.json'
message = ''


def output_CSV(message, year, month, date, hour, minuits):
    with open(ssid_txt, mode='a') as f:
        f.write(f"\n{year}年{month}月{date}日{hour}時{minuits}分\n{message}")



def main():
    # fname = "entry.json" <- 起動時にファイル名指定だと ファイルが見つからないと言われるのでフルパス指定
    with open(entry_json, "r") as f:
        entry = json.load(f)
        params = {"entry.{}".format(entry["entry"][k]): entry["output"][k] for k in entry["entry"].keys()}
        res = requests.get(entry["form_url"] + "formResponse", params=params)



if __name__ == '__main__':
    while wifi_SSID == '':
        if counter == 10:
            araguments = ("wifiにつながってません！！", year, month, date, hour, minuits)
            output_CSV(*araguments)
            result = display_message.MessageClass(*araguments)
            result.display()
            sys.exit()

        time.sleep(2)
        counter += 1
        wifi_SSID = WiFiUtil.getUsingSSID()
    if wifi_SSID in ('kigyoshimin@member', 'kigyoshimin@guest'):
        main()
        message = '入室しました！'
    else:
        message = f'SSIDが違います！\nSSID:{wifi_SSID}'
    arguments = (message, year, month, date, hour, minuits)
    output_CSV(*arguments)
    result = display_message.MessageClass(*arguments)
    result.display()

    sys.exit()
