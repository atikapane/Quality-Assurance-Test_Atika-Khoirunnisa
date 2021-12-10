import selenium
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class PopUp(BasePage):
    def is_popup_closed(self):
        driver = self.driver
        try:
            driver.find_element(*PopUpLocators.POPUP_WRAPPER)
        except NoSuchElementException:
            return True
        return False

    def input_email(self, email):
        driver = self.driver
        driver.find_element(*PopUpLocators.EMAIL_FIELD).click()
        driver.find_element(*PopUpLocators.EMAIL_FIELD).clear()
        driver.find_element(*PopUpLocators.EMAIL_FIELD).send_keys(email)

    def click_close_button(self):
        element = self.driver.find_element(*PopUpLocators.CLOSE_BUTTON)
        element.click()

    def click_subscribe_button(self):
        element = self.driver.find_element(*PopUpLocators.SUBSCRIBE_BUTTON)    
        element.click()

class HomePage(BasePage):
    # Banner
    def is_banner_prev(self, a, b):
        if a == 1 and b == 5:
            return True
        elif b == a-1 and 1<=b<=5 :
            return True
        else :
            return False
    
    def is_banner_next(self, a, b):
        if a == 5 and b == 1:
            return True
        elif b == a+1 and 1<=b<=5 :
            return True
        else :
            return False

    def banner_number(self):
        number_seq = self.driver.find_element(*BannerLocators.BANNER_SLIDER_NUMBER).text
        number = number_seq.split()[0]
        return number

class HeaderPage(BasePage):
    def get_page_title(self):
        return self.driver.title
    
    def is_page_opened(self, exp):
        # check if button opens the right page by checking tab title
        title = self.get_page_title()
        if exp in title :
            return True
        else :
            return False

    def click_wishlist_button(self):
        element = self.driver.find_element(*HeaderLocators.WISHLIST_BUTTON)
        element.click()
    
    def click_profile_button(self):
        element = self.driver.find_element(*HeaderLocators.PROFILE_BUTTON)
        element.click()

