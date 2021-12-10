from selenium.webdriver.common.by import By

class PopUpLocators(object):
    POPUP_WRAPPER = (By.CLASS_NAME, "ReactModal__Overlay ReactModal__Overlay--after-open")
    CLOSE_BUTTON = (By.CLASS_NAME, "close")
    SUBSCRIBE_BUTTON = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Email address'])[4]/following::button[1]")
    EMAIL_FIELD = (By.XPATH, "//div[2]/div/div/form/div/div/div/input")

class BannerLocators(object):
    ROUND_PREV_BUTTON = (By.XPATH, "//div[@id='__next']/main/div[2]/div/div")
    ROUND_NEXT_BUTTON = (By.XPATH, "//div[@id='__next']/main/div[2]/div/div[3]")
    BANNER_SLIDER_NUMBER = (By.CLASS_NAME, "box-slider-number")
    ARROW_PREV_BUTTON = (By.CLASS_NAME, "box-slider-arrow-prev")
    ARROW_NEXT_BUTTON = (By.CLASS_NAME, "box-slider-arrow-next")

class HeaderLocators(object):
    VIRTUAL_TRY_ON = (By.LINK_TEXT, "Virtual Try On")
    COMPLEXION_FINDER = (By.LINK_TEXT, "Complexion Finder")
    WISHLIST_BUTTON = (By.XPATH, "//div[@id='__next']/div[2]/nav/div/div[2]/div/div/div/ul[2]/li/a/i")
    PROFILE_BUTTON = (By.XPATH, "//div[@id='__next']/div[2]/nav/div/div[2]/div/div/div/ul[2]/li/a/i")