import datetime

from zgxcx import xcx_signin
zgxcx = xcx_signin()
zglog = f"{str(datetime.datetime.now())}  专柜小程序开始签到： {zgxcx[0]}"
print(zglog)

# time.sleep(1)

from web import mobile_web_signin_action
web = mobile_web_signin_action()
weblog = f"{str(datetime.datetime.now())}  移动网页端开始签到： {web[0]}"
print(weblog)

# time.sleep(3)

from gfxcx import gfxcx_signin
gfxcx = gfxcx_signin()
gfxcxlog = f"{str(datetime.datetime.now())}  官方小程序开始签到： {gfxcx[0]}"
print(gfxcxlog)

# time.sleep(1)

from qmApp import qm_signin
qm = qm_signin()
qmlog = f"{str(datetime.datetime.now())}  逑美 APP  开始签到： {qm[0]}\n{str(datetime.datetime.now())}  逑美 APP  抽奖情况：{qm[-1]}"
print(qmlog)

# from serverJ import serverJ
# server酱推送
# msg = f'专柜小程序：{zgxcx[1]}\n\n移动网页端：{web[1]}\n\n官方小程序：{gfxcx[1]}\n\n逑  美 APP ：{qm[1]}\n\n逑美APP抽奖情况：{qm[-1]}'
# push = f'serverJ推送日志：{serverJ(msg)}'

# 写入日志文件
with open("./data/log.txt", "a", encoding="UTF-8") as file:
    file.write(f'\n{zglog}\n{weblog}\n{gfxcxlog}\n{qmlog}\n')  # {push}\n
