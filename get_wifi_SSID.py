import subprocess
import re


class WiFiUtil:
    """Wi-Fi関連ユーティリティ
    """

    @staticmethod
    def getUsingSSID():
        """接続中のWi-FiのSSIDを取得する

        Returns:
            str -- SSID
        """

        cmd = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I']
        cmd_res = subprocess.run(cmd, stdout=subprocess.PIPE)
        output = cmd_res.stdout.decode('utf-8')
        matchs = re.findall(r' +SSID: .+', output)
        res = ""
        if len(matchs) > 0:
            res = matchs[0]
            res = re.sub(r'^ +SSID: ', '', res)
            res = res.rstrip()
        return res


if __name__ == '__main__':
    res = WiFiUtil.getUsingSSID()
    print(res)  # SSIDが出力される
    if res in ('kigyoshimin@member', 'kigyoshimin@guest'):
        print("you are at KigyoShiminCenter")

