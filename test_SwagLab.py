import time

from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_swaglablogin:
    def test_case001(self):
        Driver = webdriver.Firefox()


        # get url
        Driver.get("https://www.saucedemo.com/")
        # Enter username
        Driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("performance_glitch_user")
        # Enter Password
        Driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        # Click Login Button
        Driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        Driver.implicitly_wait(20)

        if Driver.title=="Swag Labs":
            print("You have login succefully")
            assert True
            Driver.close()
        else:
            print("Login Failed")
            Driver.close()
            assert False


class Test_sum:
    def test_add(self):
        a = 10
        b = 20
        if a + b ==30:
            print(a+b)
            assert True
        else:
            print("Addition is wrong")
            assert False





