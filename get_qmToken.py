import requests

# 在""里面输入你的手机号
phone = ""
# 在""里面输入你的密码
passwd = ""

def get_qmToken():
    qmlogin_url = "https://api.qiumeiapp.com/qm/10001/qmLogin"
    qmlogin_headers = {
        "appMarket": "android-qm",
        "appVersion": "7.1.0",
        # "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "api.qiumeiapp.com",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.11.0"
    }
    qmlogin_data = {
        "anonymousId": "390d3d712730b765",
        "appMarket": "android",
        "appVersion": "7.1.0",
        "deviceModel": "Redmi K20 Pro",
        "deviceNumber": "390d3d712730b765-unknown-null",
        "deviceToken": "Tk9SSUQuMSNmMzI3MWFjYzAyMzkxNTk4MmJjZDVmNDI2YmI5ODM4NS1oLTE2NjY1NDUxMzUyMzItODU4ZjFjZjc1NTFmNDAxZWI0YWQyYWViZWU4ZDczMzYjZWY4aFdKZHJMN1RPUU5zQWFtdTdUcWhuVkY0ZzJkTElXcDB1SDBnOUhzZDhFeUs3NlZvcEtLU0F0ZzR2VTUrRFJkcWVQQnhucGQ5SVd3L1ZQc3dLSFZocGdERFh4cStPUUMwUkR5ZDkvYVNONTRqQ0RsWkpUM1pSemFLcXNadytweERtUnY4NkFYbXdvM3hhbGZYaDJ1cndrRXVnMTVUczUrZ0dsWmo4Z0NSNXZUUXNDSDBSWGVjMFh5cXNLQ2RJWDh3VzlNVEdPeGtEZjNndWwyK0xPYXAwajB3UHdHWHVhYzdMdmVsa1B0S2UwQjNrR0JGNUgvYXlvL1h0dGxiK1FwdU5ZdHpVL1dxd1cwcHVBcUtDaENZUjFZNWk2ZFRtRWNFeEsrQ3JBSkFsci9tdWNpOEM4amFSWGltVWNoSGZGNE00VnNNNXZ0Q1hDcUZkcXhRY3NXb3pFWmpNd0cwM2gvazJxa29BYWRDOWllcmQrL1lUR3dNajB4OVNydVdhaUpSUWxVUjVCVmpjRGRXZ3F2RGYxSllZL2l3N1VtT2ZkakRwSG9KRnE3aGc5bmllY1J4Sjd3UU51TFpDYVh4NmIzLzYzWW84NGNZeXgvM2lHTEM3OE8rWnpzbTE5dS9LUWVFQk92SWthUjRLSG1hWU1IQUg0WjBmK2FwOTNoWnZUS0JlS2c5RnloejFycHlTcThPdHg5SWFmQS9oZjNGallUcGVXZFNSYmpGSXBQRmxCTGFmbUE0c1FCYm1YZWFoeVBaVkxKQXpicVVTOU5XeU1zM3FrYituTXl6MVZkYkZ4ZXdoWURzczFIcDhZckRBTWdXWFdpcW0jNTQuNjA3I0M0IzM2NzY5ZDVhNzQ5ZGI0OGQ0YmFmODhhMTlkNzQ3ZWE2",
        "phoneNumber": phone,
        "password": passwd,
        "sign": "85ae093177dfab94cc07c00cf77b436f"
    }
    qmlogin_res = requests.post(qmlogin_url, headers=qmlogin_headers, data=qmlogin_data).json()
    if qmlogin_res["code"] == 200:
        result = qmlogin_res["data"]["qmUserToken"]
        return result
    else:
        print("获取失败，返回结果：\n" + str(qmlogin_res))
        return False