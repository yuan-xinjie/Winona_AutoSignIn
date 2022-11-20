import os

def read_token_file():
    if os.path.exists("data") is True:
        pass
    else:
        os.mkdir("data")
        print("创建配置文件")
    try:
        with open("./data/config.ini", "r", encoding="UTF-8") as file:
            tokens = eval(file.read())
    except:
        print("从文件获取token失败，内容错误，请重新获取token")
        with open("./data/config.ini", "w", encoding="UTF-8") as files:
            strTokens = '{' + f'"web": "none","qm": "none"' + '}'
            files.write(strTokens)
            tokens = eval(strTokens)
            print(tokens)
    return tokens

if __name__ == "__main__":
    # token = eval(get_config_file())
    # print(token["web"])
    a = read_token_file()
    print(a,type(a))