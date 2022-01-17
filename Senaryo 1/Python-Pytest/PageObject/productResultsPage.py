from Utils.locators import *
from Utils.helpers import *

class ProductsPage():

    def __init__(self, driver):
        self.driver = driver

        self.product_prices_css = Locators.productPrices_css
        self.sort_xpath = Locators.sortItemMenu_xpath
        self.products_found_xpath = Locators.productsFound_xpath



    def checkExistenceOfProduct(self, itemNumber): # Checks if product number exists. Returns True or False.
        helpers = Helpers(self.driver)
        return helpers.checkElementExistence("xpath", f"//a[@data-sequence='{itemNumber}']")

    def sort(self, sortingType):  # Sorts the product with chosen type of sorting.
        helpers = Helpers(self.driver)
        helpers.locateAndClick("xpath", self.sort_xpath)  # Open sort drop down menu.
        helpers.locateAndClick("xpath", f"//label[text()='{sortingType}']")  # Choose type of sorting.
        time.sleep(0.4)

    def scrollUntilPage(self, pageNumber):  # Scrolls down until desired page number.
        helpers = Helpers(self.driver)
        time.sleep(1)
        for x in range(2, pageNumber + 1):
            product_xpath = f"//a[@data-sequence='{(x - 1) * 60}']"
            helpers.waitElementToBeLocated('xpath', product_xpath)
            helpers.scrollToElement('xpath', product_xpath)  # Scroll down to the last element of current page in order to trigger the responsive page load.


    def loadAllProducts(self):  # Loads all of the products by scrolling down until last page.
        helpers = Helpers(self.driver)
        productsAtPage = helpers.getText("xpath", self.products_found_xpath)
        lastPage = int(int(productsAtPage)/60) + 1
        self.scrollUntilPage(lastPage)


    def getProductPrice(self, element, currency):  # Returns price of a product.
        return int(element.get_attribute("textContent").replace(" ", "").replace("\n", "").split(currency)[-1].replace(",","").replace(".", ""))  # Last index of split list returns the current price if there is a discount available on product.


    def getAllProductPricesAsList(self, currency):  # Returns prices of all loaded products as a list.
        productPriceElements = self.driver.find_elements_by_css_selector(self.product_prices_css)  # Get product prices as a list.
        productPrices = []
        for element in productPriceElements:
            productPrices.append(self.getProductPrice(element, currency))
        return productPrices


    def checkIfSortedCorrectly(self, sortingType, currency):  # Checks if sorting algorithm works correctly. Returns True or False.
        self.sort(sortingType)
        self.loadAllProducts()
        productPrices = self.getAllProductPricesAsList(currency)

        sortedCorrectly = True
        for x, y in zip(productPrices, productPrices[1:]):  # Group the prices in two pieces like: 174900 151900 and 151900 150900. So all of the prices gets compared.

            if x >= y:  # >= operator must be used for High to Low sorting, <= operator for Low to High sorting.
                pass
            else:
                sortedCorrectly = False
                break  # End the loop if there is an issue with sorting to save time.

        return sortedCorrectly

