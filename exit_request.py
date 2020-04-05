import requests
import json
import display_message
import datetime
from get_wifi_SSID import WiFiUtil
import sys

wifi_ssid = WiFiUtil.getUsingSSID()
print(wifi_ssid)
# if wifi_ssid not in ('kigyoshimin@member', 'kigyoshimin@guest'):
#     sys.exit()

exit_json = '/Users/yoshidachikara/PycharmProjects/slack_bot/exit.json'


def main():
    message = "退出しますか？"
    date_now, time_now = str(datetime.datetime.now()).split(' ')
    year, month, date = date_now.split('-')
    hour, minuits, second = time_now.split(':')
    arguments = (message, year, month, date, hour, minuits)
    display_message.MessageClass(*arguments).display()
    # exit()

# def exit():
#     with open(exit_json, "r") as f:
#         entry = json.load(f)
#         params = {"entry.{}".format(entry["entry"][k]): entry["output"][k] for k in entry["entry"].keys()}
#         requests.get(entry["form_url"] + "formResponse", params=params)


if __name__ == '__main__':
    main()
