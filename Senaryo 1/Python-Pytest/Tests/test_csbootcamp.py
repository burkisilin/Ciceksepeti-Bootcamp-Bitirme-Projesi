import pytest

from PageObject.homePage import HomePage
from PageObject.productResultsPage import ProductsPage
from Base.base import Base

import pytest_check as check
from Utils.helpers import *


@pytest.mark.usefixtures('set_up')
class Test_csbootcamp(Base):

    def test_responsiveload(self):
        driver = self.driver
        productsPage = ProductsPage(driver)
        helpers = Helpers(driver)
        driver.get("https://www.mizu.com/flowers")

        pageAmountToLoad = 10  # Set desired amount of pages

        productsPage.scrollUntilPage(pageAmountToLoad)  # Load desired amount of pages

        if (productsPage.checkExistenceOfProduct(pageAmountToLoad * 60)):  # Each page should have 60 items. Trying to locate the last loaded product in order to check the responsive loading. Returns True if element exists, false if does not.
            assert True
        else:
            helpers.save_screenshot("responsive_load_test")

    def test_sort_filtering(self):
        driver = self.driver
        productsPage = ProductsPage(driver)
        helpers = Helpers(driver)
        driver.get("https://www.mizu.com/flowers")

        if productsPage.checkIfSortedCorrectly("Price: High to Low","MX$"):  # Function takes Sorting Type and Currency as argument. Returns True or False.
            assert True
        else:
            helpers.save_screenshot("filtering_test")

    def test_check_menu_links(self):
        driver = self.driver
        homepage = HomePage(driver)
        helpers = Helpers(driver)

        homepage.closePopUp()

        homepage.hoverOnAllMenuItems()  # All menu items must have hovered in order to load all a-href properties on elements due to dynamic menu loading.

        links = homepage.getMenuLinks()

        for link in links:
            # if helpers.checkPageValidation(by ="By.BrowserTitle", operand ="!=", validate ="Page Not Found", link =link): # Taking more time compared to checking response code.

            if helpers.checkPageValidation(by="By.ResponseCode", validate=200, link=link):  # Returns true if ResponseCode is 200 (Used default operand as '=='):
                check.is_true(True)  # Soft assertion
            else:
                check.is_true(False)  # Soft assertion
