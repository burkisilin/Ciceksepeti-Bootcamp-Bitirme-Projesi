from datetime import datetime, time

import pytest
from selenium import webdriver

class Base:



    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initializing Chrome driver")
        self.driver = webdriver.Chrome(executable_path= "C:/Users/bbayr/Desktop/Python/AUTOSBC PRIVATE/chromedriver_autoinstaller/97/chromedriver.exe")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(4)
        self.driver.get("https://www.mizu.com/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Test is finished")
            self.driver.close()
            self.driver.quit()

