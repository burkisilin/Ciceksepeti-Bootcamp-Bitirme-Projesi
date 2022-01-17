from Utils.locators import *
from Utils.helpers import *

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.popup_xpath = Locators.popup_xpath
        self.main_menu_class = Locators.main_menu_class
        self.main_menu_xpath = Locators.main_menu_xpath
        self.main_menu_items_class = Locators.main_menu_items_class
        self.inner_menu_xpath = Locators.inner_menu_xpath

    def closePopUp(self):
        self.driver.find_element_by_xpath(self.popup_xpath).click()


    def hoverOnAllMenuItems(self):  # Hovers at all of the menu items in order to trigger loading of responsive inner menu links.
        helpers = Helpers(self.driver)
        upperMenuElems = helpers.returnChildElements("class_name", self.main_menu_class, "class_name", self.main_menu_items_class)
        threeLayerInnerMenus = self.driver.find_elements_by_xpath(self.inner_menu_xpath)

        for upperMenuElem in upperMenuElems:
            helpers.hoverOnElement(upperMenuElem)
            time.sleep(0.3)  # Wait for inner menu to show up.

            for index in range(0, len(threeLayerInnerMenus)):
                innerMenu = threeLayerInnerMenus[index].find_elements_by_tag_name("a")
                for elem in innerMenu:
                    try:
                        helpers.hoverOnElement(elem)
                    except:
                        break

    def getMenuLinks(self):  # Returns all available links located at menu bar as a list.
        topmenu = self.driver.find_element_by_xpath(self.main_menu_xpath)

        linkElements = topmenu.find_elements_by_tag_name("a")

        links = []
        for elem in linkElements:
            links.append(elem.get_property("href"))  # Get links.
        links = list(dict.fromkeys(links))  # Remove duplicates.
        links.pop(links.index('javascript:void(0)'))  # Remove js function from links list.
        return links
