import time
from selenium import webdriver
from configuration import Configuration


config = Configuration()


class AutoCheck(Configuration):
    def __init__(self):
        super().__init__()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", self.useragent)
        # self.dr = webdriver.Firefox(firefox_profile=profile)
        self.dr = webdriver.Edge(executable_path="./msedgedriver.exe")

    def login(self):
        self.dr.get(self.login_website)
        time.sleep(2)
        username = self.dr.find_element_by_xpath("//input[@type='text']")
        username.send_keys(self.username)
        password = self.dr.find_element_by_xpath("//input[@type='password']")
        password.send_keys(self.password)
        time.sleep(1)

        self.dr.find_element_by_class_name("btn").click()
        time.sleep(3)

    def click(self, ele):
        self.dr.execute_script("arguments[0].click()", ele)

    def fuck(self):
        ele = self.dr.find_elements_by_xpath("//span[contains(@class, 'choose-wapper')]")[1]
        # self.click(ele)
        time.sleep(3)

    def checker(self, at_school):
        if at_school:
            # in campus
            active = self.dr.find_elements_by_xpath("//span[@class='choose-wapper active']")
            for i in active:
                self.click(i)
            time.sleep(1)

            gps = self.dr.find_element_by_xpath("//input[@placeholder='点击获取位置']")
            gps.click()
            time.sleep(7)

            submit = self.dr.find_element_by_class_name("sub-info")
            print(submit.text)
            if submit.text != "提交":
                print("提交失败")
                return
            submit.click()
            time.sleep(2)
            verify = self.dr.find_element_by_xpath("//div[@class='wapcf-btn wapcf-btn-ok']")
            print(verify.text + '?')
            verify.click()
            time.sleep(3)
        else:
            print("NOT SUPPORTED IN THIS VERSION!")

    def operate(self, at_school=True):
        try:
            self.login()
            self.checker(at_school)
            # self.fuck()
            self.dr.quit()
            print("打卡成功")
        except Exception as e:
            print(e.args)
            self.dr.quit()


if __name__ == '__main__':
    check = AutoCheck()
    check.operate()