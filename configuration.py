import pandas as pd

class Configuration:
    def __init__(self):
        info = pd.read_json("account_info.json")
        self.username = str(info.get("username")[0])
        self.password = info.get("password")[0]
        # print(type(self.password))
        self.login_website = "https://app.buaa.edu.cn/uc/wap/" \
                             "login?redirect=https%3A%2F%2Fapp.buaa.edu.cn%2Fsite%2FbuaaStudentNcov%2Findex"
        self.website = "https://app.buaa.edu.cn/site/buaaStudentNcov/index"
        self.useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.17(0x18001122) NetType/4G Language/zh_CN"

if __name__ == "__main__":
    config = Configuration()
