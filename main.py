import unittest
import page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from locators import *
import time

class MakeOverAll(unittest.TestCase):
    def setUp(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        s = Service(PATH)
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://www.makeoverforall.com/")
        self.driver.implicitly_wait(30)

    # POP UP
    def test_close_popup(self):
        # close pop up by clicking close (X)
        driver = self.driver
        popup = page.PopUp(self.driver)
        popup.click_close_button()
        # pop up should be closed
        assert popup.is_popup_closed(), "button (X) did not close the pop up"
    
    def test_close_popup2(self):
        # close pop up by clicking close (X)
        driver = self.driver
        popup = page.PopUp(self.driver)
        popup.click_close_button()
        # pop up should be closed
        assert popup.is_popup_closed(), "button (X) did not close the pop up"
    

    def test_subscribe_without_email(self):
        # click subscribe button without entering email address
        driver = self.driver
        popup = page.PopUp(self.driver)
        popup.click_subscribe_button()
        # pop up should not be closed
        assert False == popup.is_popup_closed(), "user could subscribe without entering email address"

    def test_input_invalid_email(self):
        # subscribe with invalid email
        driver = self.driver
        popup = page.PopUp(self.driver)
        popup.input_email("abcdef")
        popup.click_subscribe_button()
        # pop up should not be closed
        assert False == popup.is_popup_closed(), "user could subscribe using invalid email address"

    def test_input_valid_email(self):
        # subscribe with valid email
        driver = self.driver
        popup = page.PopUp(self.driver)
        popup.input_email("emailku@gmail.com")
        popup.click_subscribe_button()
        # pop up should be closed
        assert popup.is_popup_closed(), "could not subscribe with valid email"

    # BANNER
    def test_round_prev_button(self):
        # change image to previous image in banner using pink button
        driver = self.driver
        banner = page.HomePage(self.driver)
        self.close_popup()
        number_before = banner.banner_number()
        driver.find_element(*BannerLocators.ROUND_PREV_BUTTON).click()
        number_after = banner.banner_number()
        assert banner.is_banner_prev(int(number_before), int(number_after)), "could not go to previous image in banner"
    
    def test_round_next_button(self):
        # change image to next image in banner using pink button
        driver = self.driver
        banner = page.HomePage(self.driver)
        self.close_popup()
        number_before = banner.banner_number()
        driver.find_element(*BannerLocators.ROUND_NEXT_BUTTON).click()
        number_after = banner.banner_number()
        assert banner.is_banner_next(int(number_before), int(number_after)), "could not go to next image in banner"
    
    def test_arrow_prev_button(self):
        # change image to prev image in banner using arrow button
        driver = self.driver
        banner = page.HomePage(self.driver)
        self.close_popup()
        number_before = banner.banner_number()
        driver.find_element(*BannerLocators.ARROW_PREV_BUTTON).click()
        number_after = banner.banner_number()
        assert banner.is_banner_prev(int(number_before), int(number_after)), "could not go to previous image in banner"

    def test_arrrow_next_button(self):
        # change image to next image in banner using arrow button
        driver = self.driver
        banner = page.HomePage(self.driver)
        self.close_popup()
        number_before = banner.banner_number()
        driver.find_element(*BannerLocators.ARROW_NEXT_BUTTON).click()
        number_after = banner.banner_number()
        assert banner.is_banner_next(int(number_before), int(number_after)), "could not go to next image in banner"

    # HEADER
    def test_virtual_try_on(self):
        # open virtual try on page using button on header
        driver = self.driver
        header = page.HeaderPage(driver)
        self.close_popup()
        driver.find_element(*HeaderLocators.VIRTUAL_TRY_ON).click()
        assert header.is_page_opened("Virtual Try On"), "'Virtual Try On' button did not open the intended page"

    def test_complexion_finder(self):
        # open complexion finder page using button on header
        driver = self.driver
        header = page.HeaderPage(driver)
        self.close_popup()
        driver.find_element(*HeaderLocators.COMPLEXION_FINDER).click()
        assert header.is_page_opened("Complexion Finder"), "'Complexion Finder' button did not open the intended page"

    def test_wishlist_not_login(self):
        # open wishlist when user is not logged in
        driver = self.driver
        header = page.HeaderPage(driver)
        self.close_popup()
        header.click_wishlist_button()
        # when button clicked, Login page should be opened
        assert header.is_page_opened("Login"), "wishlist button did not open login page"

    def test_profile_not_login(self):
        # open profile when user is not logged in
        driver = self.driver
        header = page.HeaderPage(driver)
        self.close_popup()
        header.click_profile_button()
        # when button clicked, Login page should be opened
        assert header.is_page_opened("Login"), "wishlist button did not open login page"

    def close_popup(self):
        popup = page.PopUp(self.driver)
        popup.click_close_button()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()