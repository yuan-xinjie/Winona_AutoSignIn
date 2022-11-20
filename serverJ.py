import requests

def serverJ(msg):
    try:
        with open("./data/serverJ", "r") as f:
            serverJtoken = f.read()
    except:
        print("没有配置文件")
        return False
    sUrl = f"https://sctapi.ftqq.com/{serverJtoken}.send"
    sData = {
        "title": "薇诺娜签到推送",
        "desp": msg
    }
    res = requests.post(sUrl,sData).json()
    return res

if __name__ == "__main__":
    pass