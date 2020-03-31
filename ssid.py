from get_wifi_SSID import WiFiUtil
import datetime
id = WiFiUtil.getUsingSSID()
t = str(datetime.datetime.now())

with open('SSID.txt', mode='w') as f:
    string = id + t
    f.write(string)
