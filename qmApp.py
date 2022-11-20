import requests
from get_qmToken import get_qmToken
from config import read_token_file

tokens = read_token_file()
qmToken = tokens["qm"]
pass_push = "⭕签到成功"
fail_push = "❌签到失败，具体请查看日志信息"
already_push = "⭕今天已经签到了"
luckdraw_none_push = "⛔今日没有抽奖资格！"

# 逑美签到配置
url = "https://api.qiumeiapp.com/qm-activity/qdcj/signin"
headers = {
    "Connection": "keep-alive",
    "Host": "api.qiumeiapp.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K20 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "com.pifukezaixian.users",
    "Referer": "https://h5.qiumeiapp.com/"
}
data = {
    "qmUserToken": qmToken
}

def get_luckdraw():
    u_url = 'https://api.qiumeiapp.com/qm-activity/qdcj/getUserSigninInfo'
    u_res = requests.post(url=u_url, headers=headers, data=data).json()
    if u_res["code"] == 702:
        data["qmUserToken"] = get_qmToken()
        tokens["qm"] = data["qmUserToken"]
        with open("./data/config.ini", "w") as files:
            files.write(str(tokens))
        u_res = requests.post(url=u_url, headers=headers, data=data).json()
    else:
        pass
    zige = u_res['data']['haveLuckyDraw']
    if zige == 1:
        # 抽奖
        print("开始抽奖")
        c_url = "https://api.qiumeiapp.com/qm-activity/qdcj/luckyDraw"
        c_res = requests.post(url=c_url, headers=headers, data=data).json()
        c_msg = c_res['msg']
        # 获取抽奖结果
        if c_res['code'] == 200:
            print('获得:' + c_res['data']['prizeName'])
            result = str("🎉获得" + c_res['data']['prizeName'])
            return result
        else:
            print(c_res)
            result = "🩸抽奖异常，具体请查看日志信息"
            return result
    elif zige == 0:
        result = "⛔今日没有抽奖资格"
        return result

def qm_sign(qm_url,qm_headers,qm_data):
    res = requests.post(url=qm_url, headers=qm_headers, data=qm_data).json()
    msg = res['msg']  # 获取msg信息
    code = res['code']
    return msg,code,res

def qm_signin():
    res = qm_sign(url,headers,data)
    msg = res[0]
    code = res[1]
    # 获取抽奖结果
    luckdraw = get_luckdraw()
    if code == 200:
        return msg, pass_push, luckdraw   # 返回msg信息，推送信息，抽奖信息

    elif msg == "用户不存在!":
        print(res)
        print("Token失效，尝试重新获取Token")
        if get_qmToken() is False:
            fail = "token获取失败，具体查看日志"
            return fail
        else:
            new_token = get_qmToken()
            tokens["qm"] = new_token
            # 写入新的token到配置文件
            with open("./data/config.ini", "w") as files:
                files.write(str(tokens))
            print(f"qm获取到Token：{new_token}")
            resign_data = {"qmUserToken": new_token}
            print("qm尝试重新签到")
            res1 = qm_sign(url,headers,resign_data)
            msg1 = res1[0]
            code1 = res1[1]
            luckdraw = get_luckdraw()
            if code1 == 200:
                return msg1, pass_push, luckdraw
            elif msg1 == "你今天已经签到过了！":
                return msg1, already_push, luckdraw
            else:
                return res1, fail_push, luckdraw

    # 正常签到
    elif msg == "你今天已经签到过了！":
        return msg, already_push, luckdraw
    else:
        return res, fail_push, luckdraw